from dbt.adapters.sql import SQLAdapter as adapter_cls
from dbt.adapters.upsolver import UpsolverConnectionManager
from dbt.events import AdapterLogger
from dbt.adapters.upsolver.relation import UpsolverRelation
from typing import List
from dbt.adapters.base.meta import available
from dbt.adapters.upsolver.options.copy_options import Copy_options
from dbt.adapters.upsolver.options.connection_options import Connection_options
from dbt.adapters.upsolver.options.transformation_options import Transformation_options
from dbt.adapters.upsolver.options.target_options import Target_options
import agate
import datetime
import re
import dbt

logger = AdapterLogger("Upsolver")
LIST_RELATION_MACRO_NAME = "list_relation_without_caching"


class UpsolverAdapter(adapter_cls):
    """
    Controls actual implmentation of adapter, and ability to override certain methods.
    """

    ConnectionManager = UpsolverConnectionManager
    Relation = UpsolverRelation

    @classmethod
    def date_function(cls):
        """
        Returns canonical date func
        """
        return "datenow()"

    def debug_query(self) -> None:
        self.execute('SELECT * FROM system.information_schema.jobs limit1;')


    def create_schema(self, relation: UpsolverRelation) -> None:
        pass

    def drop_schema(self, relation: UpsolverRelation) -> None:
        pass

    @available
    def get_connection_from_sql(self, sql):
        try:
            connection_identifier = re.search('"(.*)"', sql).group().split('.')[2] \
                                      .translate(str.maketrans({'\"':'', '\'':''}))
            return connection_identifier
        except Exception:
            raise dbt.exceptions.ParsingError(f"Error while parsing connection name from sql: {sql}")

    @available
    def get_columns_names_with_types(self, list_dict):
        res = []
        for col in list_dict:
            if col.get('type'):
                res.append(f"{col['field']} {col['type']}")
        return ', '.join(set(res))

    @available
    def get_columns_names(self, list_dict):
        res = []
        for col in list_dict:
            res.append(col['field'])
        return ', '.join(set(res))

    @available
    def separate_options(self, config_options, source):
        job_options = self.enrich_options(config_options, source, 'job_options')
        source_options = self.enrich_options(config_options, source, 'source_options')
        return job_options, source_options

    def render_option_from_dict(self, option_value):
        try:
            res = []
            for key, value in option_value.items():
                item = [f'{key}=']
                if isinstance(value, list):
                    item.append('(')
                    item.append(' ,'.join(value))
                    item.append(')')
                else:
                    item.append(value)
                res.append(''.join(item))
            return f"({' ,'.join(res)})"
        except Exception:
            raise dbt.exceptions.ParsingError(f"Error while parsing value: {value}. Expected type: dictionary")

    def render_option_from_list(self, option_value):
        try:
            if isinstance(option_value, list) and len(option_value) > 1:
                return tuple(i for i in option_value)
            else:
                return f"('{''.join(option_value)}')"
        except Exception:
            raise dbt.exceptions.ParsingError(f"Error while parsing value: {value}. Expected type: list of strings")

    @available
    def enrich_options(self, config_options, source, options_type):
        options = self.get_options(source, options_type)
        enriched_options = {}
        for option, value in config_options.items():
            find_value = options.get(option.lower(), None)
            if find_value:
                if options[option.lower()]['type'] == 'list':
                    value = self.render_option_from_list(value)
                elif options[option.lower()]['type'] == 'dict':
                    value = self.render_option_from_dict(value)
                enriched_options[option] = find_value
                enriched_options[option]['value'] = value
            else:
                logger.warning(f"Options not found: {option}")
        return enriched_options

    @available
    def filter_options(self, options, parametr):
        editable = {key:val for key, val in options.items() if val[parametr] == True}
        return editable

    @available
    def get(self, config, key, default=None):
        config = {k.lower(): v for k, v in config.items()}
        value = config.get(key, default)
        return value

    @available
    def require(self, config, key):
        config = {k.lower(): v for k, v in config.items()}
        value = config.get(key, None)
        if value:
            return value
        else:
            raise dbt.exceptions.ParsingError(f"Required option is missing: {key}")


    def get_options(self, source, options_type):
        try:
            if options_type == 'connection_options':
                options = Connection_options[source.lower()]
            elif options_type == 'transformation_options':
                options = Transformation_options[source.lower()]
            elif options_type == 'target_options':
                options = Target_options[source.lower()]
            else:
                options = Copy_options[source.lower()][options_type]
            return options
        except Exception:
            raise dbt.exceptions.ParsingError(f"Undefined option value: {source}")

    @available
    def merge_tables(self, tables):
        return agate.Table.merge(tables)

    @available
    def trim_quotes(self, value):
        return value.replace('"', '')

    def list_relations_without_caching(
        self,
        schema_relation: UpsolverRelation,
        ) -> List[UpsolverRelation]:
        materializations = ["table", "job", "connection", "view"]
        results = agate.Table([],[])
        for type in materializations:
            kwargs = {"schema_relation": schema_relation, "relation_type": type}
            result = self.execute_macro(LIST_RELATION_MACRO_NAME, kwargs=kwargs)
            results = agate.Table.merge([results, result])
        relations = []
        quote_policy = {"database": True, "schema": True, "identifier": True}
        for _database, name, _schema, _type in results:
            try:
                _type = self.Relation.get_relation_type(_type)
            except ValueError:
                _type = self.Relation.External
            relations.append(
                self.Relation.create(
                    database=_database,
                    schema=_schema,
                    identifier=name,
                    quote_policy=quote_policy,
                    type=_type,
                )
            )
        return relations
