{% macro upsolver__get_catalog(information_schema, schemas)-%}
  {{ log("information_schema " ~ information_schema ) }}
  {{ log("schemas " ~ schemas ) }}

  {%- if (schemas | length) == 0 -%}
   {%set msg -%}
    There is no schemas
   {%endset-%}
  {%- else -%}
  {%- set query -%}
    SELECT
      catalog as "table_database",
      schema as "table_schema",
      'table_name' as "table_name",
      name as "column_name",
      data_type as "column_type",
      'table_type' as "table_type",
      'table_owner' as "table_owner",
      10 as "column_index",
      'column_comment' as "column_comment"
    FROM system.information_schema.columns
    WHERE catalog = 'default_glue_catalog' AND
    {%- for schema in schemas %}
      schema = '{{ schema }}'{%- if not loop.last %} or {% endif -%}
    {%- endfor %}
  {%- endset -%}
  {%- endif -%}

  {{ return(run_query(query)) }}

{% endmacro %}
