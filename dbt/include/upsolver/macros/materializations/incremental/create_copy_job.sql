{% macro get_create_copy_job_sql(target_relation, sql, into_relation, sync, options, source, target_connection, target_type) -%}

    {% set connection_identifier = adapter.get_connection_from_sql(sql) %}
    {% set job_options, source_options = adapter.separate_options(options, source) %}
    {% set target_options = adapter.enrich_options(options, target_type, 'target_options') %}

    CREATE
    {% if sync %}
      SYNC
    {% endif %}
    JOB {{target_relation.job_identifier}}
    {{ render_options(job_options, 'create') }}
    {{ render_options(target_options, 'create') }}
    AS COPY FROM {{source}} {{connection_identifier}}
    {{ render_options(source_options, 'create') }}
    INTO
    {% if target_type == 'snowflake' %}
      {{target_type}}
    {% endif %}
      {{into_relation}}

{%- endmacro %}
