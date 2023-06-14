from dbt.adapters.sql import SQLAdapter as adapter_cls
from dbt.adapters.upsolver import UpsolverConnectionManager
from dbt.events import AdapterLogger
from dbt.adapters.upsolver.relation import UpsolverRelation
from typing import List, Optional, Dict, Any, Set
from dbt.adapters.base.meta import available
from dbt.adapters.base.impl import ConstraintSupport
from dbt.contracts.graph.nodes import ColumnLevelConstraint, ConstraintType, ModelLevelConstraint
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

    CONSTRAINT_SUPPORT = {
        ConstraintType.check: ConstraintSupport.ENFORCED,
        ConstraintType.not_null: ConstraintSupport.ENFORCED,
        ConstraintType.unique: ConstraintSupport.NOT_SUPPORTED,
        ConstraintType.primary_key: ConstraintSupport.NOT_SUPPORTED,
        ConstraintType.foreign_key: ConstraintSupport.NOT_SUPPORTED,
    }

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
    def render_columns_names(self, list_dict):
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

    def render_raw_columns_from_columns(self, raw_columns: Dict[str, Dict[str, Any]]) -> List:
        rendered_columns = []
        columns = []
        for v in raw_columns.values():
            rendered_column = f"{v['name']} {v['data_type']}"
            rendered_columns.append(rendered_column)

        return rendered_columns

    def render_columns_from_config(self, list_dict: List[Dict])-> List:
        res = []
        for col in list_dict:
            if col.get('type'):
                res.append(f"{col['field']} {col['type']}")
        return res

    @available
    def render_columns(self, raw_columns_from_columns: Dict[str, Dict[str, Any]], raw_columns_from_config: List[Dict]) -> Set:
        columns_from_columns = self.render_raw_columns_from_columns(raw_columns_from_columns)
        columns_from_config = self.render_columns_from_config(raw_columns_from_config)
        return ', '.join(set(columns_from_columns + columns_from_config))

    @available
    @classmethod
    def render_raw_columns_constraints(cls, raw_columns: Dict[str, Dict[str, Any]]) -> List:
        rendered_column_constraints = []

        for v in raw_columns.values():
            for con in v.get("constraints", None):
                constraint = cls._parse_column_constraint(con)
                c = cls.process_parsed_constraint(constraint, cls.render_column_constraint)
                if c is not None:
                    rendered_column_constraint = c
                rendered_column_constraints.append(rendered_column_constraint)

        return rendered_column_constraints

    @classmethod
    def render_model_constraint(cls, constraint: ModelLevelConstraint) -> Optional[str]:
        constraint_prefix = f"WITH EXPECTATION {constraint.name}"
        column_list = ", ".join(constraint.columns)
        if constraint.type == ConstraintType.check and constraint.expression:
            return f"{constraint_prefix} EXPECT {constraint.expression} ON VIOLATION WARN"
        else:
            return None

    @classmethod
    def render_column_constraint(cls, constraint: ColumnLevelConstraint) -> Optional[str]:
        constraint_expression = constraint.expression or ""
        column_name = 'dddddd'
        rendered_column_constraint = None
        if constraint.type == ConstraintType.check and constraint_expression:
            constraint_prefix = f"WITH EXPECTATION {constraint.name}" if constraint.name else ""
            rendered_column_constraint = f"{constraint_prefix} EXPECT {constraint_expression} ON VIOLATION WARN"
        elif constraint.type == ConstraintType.not_null:
            constraint_prefix = f"WITH EXPECTATION {constraint.name}" if constraint.expression else f"WITH EXPECTATION not_null__{column_name}"
            rendered_column_constraint = f"{constraint_prefix} EXPECT {column_name} IS NOT NULL ON VIOLATION WARN"

        if rendered_column_constraint:
            rendered_column_constraint = rendered_column_constraint.strip()
        return rendered_column_constraint
