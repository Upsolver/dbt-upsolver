{% macro get_create_copy_job_sql(job_identifier, sql, into_relation, sync, options, source, target_type) -%}

    {% set connection_identifier = adapter.get_connection_from_sql(sql) %}
    {% set job_options, source_options = adapter.separate_options(options, source) %}
    {%- if target_type != 'datalake' -%}
      {% set target_options = adapter.enrich_options(options, target_type, 'target_options') %}
    {%- else -%}
      {% set target_options = {} %}
      {% set target_type = '' %}
    {%- endif -%}

    CREATE
    {% if sync %}
      SYNC
    {% endif %}
    JOB {{job_identifier}}
    {{ render_options(job_options, 'create') }}
    {{ render_options(target_options, 'create') }}
    AS COPY FROM {{source}} {{connection_identifier}}
    {{ render_options(source_options, 'create') }}
    INTO {{target_type}} {{into_relation}}

{%- endmacro %}
