{{% macro upsolver__get_catalog(information_schema, schemas)-%}}
  {{ log("information_schema " ~ information_schema ) }}
  {{ log("schemas " ~ schemas ) }}

  {%- if (schemas | length) == 0 -%}
   {{%set msg -%}}
    There is no schemas
   {{%endset-%}}
  {%- else -%}
  {%- set query -%}

  {%- endset -%}

  {%- endif -%}
    select * from system.information_schema.columns
    WHERE catalog = 'default_glue_catalog' AND
    {%- for schema in schemas -%}
    schema = '{{ schema }}'{%- if not loop.last %} or {% endif -%}

  {{ return(run_query(query)) }}

{{% endmacro %}}
