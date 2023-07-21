---
title: "Upsolver configurations"
id: "upsolver-configs"
description: "Upsolver Configurations - Read this in-depth guide to learn about configurations in dbt."
---

## Supported Upsolver SQLake functionality:
| COMMAND | STATE | MATERIALIZED |
| ------ | ------ | ------ |
| SQL compute cluster| not supported | - |
| SQL connections| supported | connection |
| SQL copy job | supported | incremental |
| SQL merge job | supported | incremental |
| SQL insert job | supported | incremental |
| SQL materialized views | supported | materializedview |


## Configs materialization

| Config | Required | Materialization | Description | Example |
| ------ | --------- | --------------- | ---------- | ------- |
| connection_type | Yes | connection | Connection identifier: S3/GLUE_CATALOG/KINESIS | connection_type='S3' |
| connection_options | Yes | connection | Dictionary of options supported by selected connection |           connection_options={ 'aws_role': 'aws_role', 'external_id': 'SAMPLES', 'read_only': True } |
| incremental_strategy | No | incremental | Define one of incremental strategies: merge/copy/insert. Default: copy | incremental_strategy='merge' |
| source | No | incremental | Define source to copy from: S3/KAFKA/KINESIS | source = 'S3' |
| target_type | No | incremental | Define supported target to copy into. Default: copy into a table created in a metastore connection | target_type='Snowflake' |
| target_schema | Yes/No | incremental | Define target schema. Required if target_type not table created in a metastore connection | target_schema = 'your_schema' |
| target_connection | Yes/No | incremental | Define target connection. Required if target_type not table created in a metastore connection | target_connection = 'your_snowflake_connection' |
| target_table_alias | Yes/No | incremental | Define target table. Required if target_type not table created in a metastore connection | target_table_alias = 'target_table' |
| delete_condition | No | incremental | Records that match the ON condition and a delete condition can be deleted | delete_condition='nettotal > 1000' |
| partition_by | No | incremental | List of dictionaries to define partition_by for target metastore table | partition_by=[{'field':'$field_name'}] |
| primary_key | No | incremental | List of dictionaries to define partition_by for target metastore table  | primary_key=[{'field':'customer_email', 'type':'string'}] |
| map_columns_by_name | No | incremental | Maps columns from the SELECT statement to the table. Boolean. Default: False | map_columns_by_name=True |
| sync | No | incremental/materializedview | Boolean option to define if job is synchronized or non-msynchronized. Default: False | sync=True |
| options | No | incremental/materializedview | Dictionary of job options | options={ 'START_FROM': 'BEGINNING', 'ADD_MISSING_COLUMNS': True } |



## Connection options





## SQL connections

Connections are used to provide Upsolver with the proper credentials to bring your data into SQLake as well as to write out your transformed data to various services. More details on ["Upsolver SQL connections"](https://docs.upsolver.com/sqlake/sql-command-reference/sql-connections)
As a dbt model connection is a model with materialized='connection'
```sql
{{ config(
        materialized='connection',
        connection_type={ 'S3' | 'GLUE_CATALOG' | 'KINESIS' | 'KAFKA'| 'SNOWFLAKE' },
        connection_options={}
    	)
}}
```
Running this model will compile CREATE CONNECTION(or ALTER CONNECTION if exists) SQL and send it to Upsolver engine. Name of the connection will be name of the model.


## SQL copy job

A COPY FROM job allows you to copy your data from a given source into a table created in a metastore connection. This table then serves as your staging table and can be used with SQLake transformation jobs to write to various target locations. More details on ["Upsolver SQL copy-from"](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/copy-from)

As a dbt model copy job is model with materialized='incremental'
```sql
{{ config(  materialized='incremental',
            sync=True|False,
            source = 'S3'| 'KAFKA' | ... ,
        	options={
              	'option_name': 'option_value'
            },
        	partition_by=[{}]
      	)
}}
SELECT * FROM {{ ref(<model>) }}
```
Running this model will  compile CREATE TABLE SQL(or ALTER TABLE if exists) and CREATE COPY JOB(or ALTER COPY JOB if exists) SQL and send it to Upsolver engine. Name of the table will be name of the model. Name of the job will be name of the model plus '_job'


## SQL insert job

An INSERT job defines a query that pulls in a set of data based on the given SELECT statement and inserts it into the designated target. This query is then run periodically based on the RUN_INTERVAL defined within the job. More details on ["Upsolver SQL insert"](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/sql-transformation-jobs/insert).

As a dbt model insert job is model with materialized='incremental' and incremental_strategy='insert'
```sql
{{ config(  materialized='incremental',
            sync=True|False,
            map_columns_by_name=True|False,
            incremental_strategy='insert',
            options={
              	'option_name': 'option_value'
            },
            primary_key=[{}]
          )
}}
SELECT ...
FROM {{ ref(<model>) }}
WHERE ...
GROUP BY ...
HAVING COUNT(DISTINCT orderid::string) ...
```
Running this model will compile CREATE TABLE SQL(or ALTER TABLE if exists) and CREATE INSERT JOB(or ALTER INSERT JOB if exists) SQL and send it to Upsolver engine. Name of the table will be name of the model. Name of the job will be name of the model plus '_job'


## SQL merge job

A MERGE job defines a query that pulls in a set of data based on the given SELECT statement and inserts into, replaces, or deletes the data from the designated target based on the job definition. This query is then run periodically based on the RUN_INTERVAL defined within the job. More details on ["Upsolver SQL merge"](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/sql-transformation-jobs/merge).

As a dbt model merge job is model with materialized='incremental' and incremental_strategy='merge'
```sql
{{ config(  materialized='incremental',
            sync=True|False,
            map_columns_by_name=True|False,
            incremental_strategy='merge',
            options={
              	'option_name': 'option_value'
            },
            primary_key=[{}]
          )
}}
SELECT ...
FROM {{ ref(<model>) }}
WHERE ...
GROUP BY ...
HAVING COUNT ...
```
Running this model will compile CREATE TABLE SQL(or ALTER TABLE if exists) and CREATE MERGE JOB(or ALTER MERGE JOB if exists) SQL and send it to Upsolver engine. Name of the table will be name of the model. Name of the job will be name of the model plus '_job'


## SQL materialized views

When transforming your data, you may find that you need data from multiple source tables in order to achieve your desired result.
In such a case, you can create a materialized view from one SQLake table in order to join it with your other table (which in this case is considered the main table). More details on ["Upsolver SQL materialized views"](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/sql-transformation-jobs/sql-materialized-views).

As a dbt model materialized views  is model with materialized='materializedview'.
```sql
{{ config(  materialized='materializedview',
            sync=True|False,
            options={'option_name': 'option_value'}
        )
}}
SELECT ...
FROM {{ ref(<model>) }}
WHERE ...
GROUP BY ...
```
Running this model will compile CREATE MATERIALIZED VIEW SQL(or ALTER MATERIALIZED VIEW if exists) and send it to Upsolver engine. Name of the materializedview  will be name of the model.


## Projects examples

> projects examples link: [github.com/dbt-upsolver/examples/](https://github.com/Upsolver/dbt-upsolver/tree/main/examples)



## Connection options

| Option | Storage    | Type | Editable | Optional | Config Syntax |
| --------| --------- | ---- | -------- | -------- | ------------- |
| aws_role | s3 | text | True | True | 'aws_role': '<aws_role>' |
| external_id | s3 | text | True | True | 'external_id': '<external_id>' |
| aws_access_key_id | s3 | text | True | True | 'aws_access_key_id': '<aws_access_key_id>' |
| aws_secret_access_key_id | s3 | text | True | True | 'aws_secret_access_key_id': '<aws_secret_access_key_id>' |
| path_display_filter | s3 | text | True | True | 'path_display_filter': '<path_display_filter>' |
| path_display_filters | s3 | list | True | True | 'path_display_filters': ('<filter>', ...) |
| read_only | s3 | boolean | True | True | 'read_only': True/False |
| encryption_kms_key | s3 | text | True | True | 'encryption_kms_key': '<encryption_kms_key>' |
| encryption_customer_kms_key | s3 | text | True | True | 'encryption_customer_kms_key': '<encryption_customer_kms_key>' |
| comment | s3 | text | True | True | 'comment': '<comment>' |
| host | kafka | text | False | False | 'host': '<host>' |
| hosts | kafka | list | False | False | 'hosts': ('<host>', ...) |
| consumer_properties | kafka | text | True | True | 'consumer_properties': '<consumer_properties>' |
| version | kafka | value | False | True | 'version': '<value>' |
| require_static_ip | kafka | boolean | True | True | 'require_static_ip': True/False |
| ssl | kafka | boolean | True | True | 'ssl': True/False |
| topic_display_filter | kafka | text | True | True | 'topic_display_filter': '<topic_display_filter>' |
| topic_display_filters | kafka | list | True | True | 'topic_display_filter': ('<filter>', ...) |
| comment | kafka | text | True | True | 'comment': '<comment>' |
| aws_role | glue_catalog | text | True | True | 'aws_role': '<aws_role>' |
| external_id | glue_catalog | text | True | True | 'external_id': '<external_id>' |
| aws_access_key_id | glue_catalog | text | True | True | 'aws_access_key_id': '<aws_access_key_id>' |
| aws_secret_access_key | glue_catalog | text | True | True | 'aws_secret_access_key': '<aws_secret_access_key>' |
| default_storage_connection | glue_catalog | identifier | False | False | 'default_storage_connection': '<default_storage_connection>' |
| default_storage_location | glue_catalog | text | False | False | 'default_storage_location': '<default_storage_location>' |
| region | glue_catalog | text | False | True | 'region': '<region>' |
| database_display_filter | glue_catalog | text | True | True | 'database_display_filter': '<database_display_filter>' |
| database_display_filters | glue_catalog | list | True | True | 'database_display_filters': ('<filter>', ...) |
| comment | glue_catalog | text | True | True | 'comment': '<comment>' |
| aws_role | kinesis | text | True | True | 'aws_role': '<aws_role>' |
| external_id | kinesis | text | True | True | 'external_id': '<external_id>' |
| aws_access_key_id | kinesis | text | True | True | 'aws_access_key_id': '<aws_access_key_id>' |
| aws_secret_access_key | kinesis | text | True | True | 'aws_secret_access_key': '<aws_secret_access_key>' |
| region | kinesis | text | False | False | 'region': '<region>' |
| read_only | kinesis | boolean | False | True | 'read_only': True/False |
| max_writers | kinesis | integer | True | True | 'max_writers': <integer> |
| stream_display_filter | kinesis | text | True | True | 'stream_display_filter': '<stream_display_filter>' |
| stream_display_filters | kinesis | list | True | True | 'stream_display_filters': ('<filter>', ...) |
| comment | kinesis | text | True | True | 'comment': '<comment>' |
| connection_string | snowflake | text | True | False | 'connection_string': '<connection_string>' |
| user_name | snowflake | text | True | False | 'user_name': '<user_name>' |
| password | snowflake | text | True | False | 'password': '<password>' |
| max_concurrent_connections | snowflake | integer | True | True | 'max_concurrent_connections': <integer> |
| comment | snowflake | text | True | True | 'comment': '<comment>' |
| connection_string | redshift | text | True | False | 'connection_string': '<connection_string>' |
| user_name | redshift | text | True | False | 'user_name': '<user_name>' |
| password | redshift | text | True | False | 'password': '<password>' |
| max_concurrent_connections | redshift | integer | True | True | 'max_concurrent_connections': <integer> |
| comment | redshift | text | True | True | 'comment': '<comment>' |
| connection_string | mysql | text | True | False | 'connection_string': '<connection_string>' |
| user_name | mysql | text | True | False | 'user_name': '<user_name>' |
| password | mysql | text | True | False | 'password': '<password>' |
| comment | mysql | text | True | True | 'comment': '<comment>' |
| connection_string | postgres | text | True | False | 'connection_string': '<connection_string>' |
| user_name | postgres | text | True | False | 'user_name': '<user_name>' |
| password | postgres | text | True | False | 'password': '<password>' |
| comment | postgres | text | True | True | 'comment': '<comment>' |
| connection_string | elasticsearch | text | True | False | 'connection_string': '<connection_string>' |
| user_name | elasticsearch | text | True | False | 'user_name': '<user_name>' |
| password | elasticsearch | text | True | False | 'password': '<password>' |
| comment | elasticsearch | text | True | True | 'comment': '<comment>' |


## Target options

| Option | Storage    | Type | Editable | Optional | Config Syntax |
| --------| --------- | ---- | -------- | -------- | ------------- |
| globally_unique_keys | datalake | boolean | False | True | 'globally_unique_keys': True/False |
| storage_connection | datalake | identifier | False | True | 'storage_connection': '<storage_connection>' |
| storage_location | datalake | text | False | True | 'storage_location': '<storage_location>' |
| compute_cluster | datalake | identifier | True | True | 'compute_cluster': '<compute_cluster>' |
| compression | datalake | value | True | True | 'compression': 'SNAPPY/GZIP' |
| compaction_processes | datalake | integer | True | True | 'compaction_processes': <integer> |
| disable_compaction | datalake | boolean | True | True | 'disable_compaction': True/False |
| retention_date_partition | datalake | identifier | False | True | 'retention_date_partition': '<column>' |
| table_data_retention | datalake | identifier | True | True | 'table_data_retention': '<N DAYS>' |
| column_data_retention | datalake | dict | True | True | 'column_data_retention': {'COLUMN' : '<column>','DURATION': N DAYS} |
| comment | datalake | text | True | True | 'comment': '<comment>' |
| storage_connection | materialized_view | identifier | False | True | 'storage_connection': '<storage_connection>' |
| storage_location | materialized_view | text | False | True | 'storage_location': '<storage_location>' |
| max_time_travel_duration | materialized_view | identifier | True | True | 'max_time_travel_duration': '<N DAYS>' |
| compute_cluster | materialized_view | identifier | True | True | 'compute_cluster': '<compute_cluster>' |
| column_transformations | snowflake | dict | False | True | 'column_transformations': {'<column>' : '<expression>' , ...} |
| deduplicate_with | snowflake | dict | False | True | 'deduplicate_with': {'COLUMNS' : ['col1', 'col2'],'WINDOW': 'N HOURS'} |
| exclude_columns | snowflake | list | False | True | 'exclude_columns': ('<exclude_column>', ...) |
| create_table_if_missing | snowflake | boolean | False | True | 'create_table_if_missing': True/False} |
| run_interval | snowflake | integer | False | True | 'run_interval': '<N MINUTES/HOURS/DAYS>' |


## Transformation options

| Option | Storage    | Type | Editable | Optional | Config Syntax |
| --------| --------- | ---- | -------- | -------- | ------------- |
| run_interval | s3 | ineger | False | True | 'run_interval': '<N MINUTES/HOURS/DAYS>' |
| start_from | s3 | value | False | True | 'start_from': '<timestamp>/NOW/BEGINNING' |
| end_at | s3 | value | True | True | 'end_at': '<timestamp>/NOW' |
| compute_cluster | s3 | identifier | True | True | 'compute_cluster': '<compute_cluster>' |
| comment | s3 | text | True | True | 'comment': '<comment>' |
| allow_cartesian_products | s3 | boolean | False | True | 'allow_cartesian_products': True/False |
| aggregation_parallelism | s3 | integer | True | True | 'aggregation_parallelism': <integer> |
| run_parallelism | s3 | integer | True | True | 'run_parallelism': <integer> |
| file_format | s3 | value | False | False | 'file_format': 'CSV/TSV ...' |
| compression | s3 | value | False | True | 'compression': 'SNAPPY/GZIP ...' |
| date_pattern | s3 | text | False | True | 'date_pattern': '<date_pattern>' |
| output_offset | s3 | identifier | False | True | 'output_offset': '<N MINUTES/HOURS/DAYS>' |
| location | s3 | text | False | False | 'location': '<location>' |
| run_interval | elasticsearch | identifier | False | True | 'run_interval': '<N MINUTES/HOURS/DAYS>' |
| start_from | elasticsearch | value | False | True | 'start_from': '<timestamp>/NOW/BEGINNING' |
| end_at | elasticsearch | value | True | True | 'end_at': '<timestamp>/NOW' |
| compute_cluster | elasticsearch | identifier | True | True | 'compute_cluster': '<compute_cluster>' |
| allow_cartesian_products | elasticsearch | boolean | False | True | 'allow_cartesian_products': True/False |
| aggregation_parallelism | elasticsearch | integer | True | True | 'aggregation_parallelism': <integer> |
| run_parallelism | elasticsearch | integer | True | True | 'run_parallelism': <integer> |
| bulk_max_size_bytes | elasticsearch | integer | True | True | 'bulk_max_size_bytes': <integer> |
| index_partition_size | elasticsearch | value | True | True | 'index_partition_size': 'HOURLY/DAILY ...' |
| comment | elasticsearch | text | True | True | 'comment': '<comment>' |
| custom_insert_expressions | snowflake | dict | True | True | 'custom_insert_expressions': {'INSERT_TIME' : 'CURRENT_TIMESTAMP()','MY_VALUE': '<value>'} |
| custom_update_expressions | snowflake | dict | True | True | 'custom_update_expressions': {'UPDATE_TIME' : 'CURRENT_TIMESTAMP()','MY_VALUE': '<value>'} |
| keep_existing_values_when_null | snowflake | boolean | True | True | 'keep_existing_values_when_null': True/False |
| add_missing_columns | snowflake | boolean | False | True | 'add_missing_columns': True/False |
| run_interval | snowflake | identifier | False | True | 'run_interval': '<N MINUTES/HOURS/DAYS>' |
| start_from | snowflake | value | False | True | 'start_from': '<timestamp>/NOW/BEGINNING' |
| end_at | snowflake | value | True | True | 'end_at': '<timestamp>/NOW' |
| compute_cluster | snowflake | identifier | True | True | 'compute_cluster': '<compute_cluster>' |
| allow_cartesian_products | snowflake | boolean | False | True | 'allow_cartesian_products': True/False |
| aggregation_parallelism | snowflake | integer | True | True | 'aggregation_parallelism': <integer> |
| run_parallelism | snowflake | integer | True | True | 'run_parallelism': <integer> |
| comment | snowflake | text | True | True | 'comment': '<comment>' |
| add_missing_columns | datalake | boolean | False | True | 'add_missing_columns': True/False |
| run_interval | datalake | identifier | False | True | 'run_interval': '<N MINUTES/HOURS/DAYS>' |
| start_from | datalake | value | False | True | 'start_from': '<timestamp>/NOW/BEGINNING' |
| end_at | datalake | value | True | True | 'end_at': '<timestamp>/NOW' |
| compute_cluster | datalake | identifier | True | True | 'compute_cluster': '<compute_cluster>' |
| allow_cartesian_products | datalake | boolean | False | True | 'allow_cartesian_products': True/False |
| aggregation_parallelism | datalake | integer | True | True | 'aggregation_parallelism': <integer> |
| run_parallelism | datalake | integer | True | True | 'run_parallelism': <integer> |
| comment | datalake | text | True | True | 'comment': '<comment>' |
| run_interval | redshift | identifier | False | True | 'run_interval': '<N MINUTES/HOURS/DAYS>' |
| start_from | redshift | value | False | True | 'start_from': '<timestamp>/NOW/BEGINNING' |
| end_at | redshift | value | True | True | 'end_at': '<timestamp>/NOW' |
| compute_cluster | redshift | identifier | True | True | 'compute_cluster': '<compute_cluster>' |
| allow_cartesian_products | redshift | boolean | False | True | 'allow_cartesian_products': True/False |
| aggregation_parallelism | redshift | integer | True | True | 'aggregation_parallelism': <integer> |
| run_parallelism | redshift | integer | True | True | 'run_parallelism': <integer> |
| skip_failed_files | redshift | boolean | False | True | 'skip_failed_files': True/False |
| fail_on_write_error | redshift | boolean | False | True | 'fail_on_write_error': True/False |
| comment | redshift | text | True | True | 'comment': '<comment>' |


## Copy options

| Option | Storage    | Category | Type | Editable | Optional | Config Syntax |
| -------| ---------- | -------- | -----| -------- | -------- | ------------- |
| topic | kafka | source_options | text | False | False | 'comment': '<comment>' |
| exclude_columns | kafka | job_options | list | False | True | 'exclude_columns': ('<exclude_column>', ...) |
| deduplicate_with | kafka | job_options | dict | False | True | 'deduplicate_with': {'COLUMNS' : ['col1', 'col2'],'WINDOW': 'N HOURS'} |
| consumer_properties | kafka | job_options | text | True | True | 'comment': '<comment>' |
| reader_shards | kafka | job_options | integer | True | True | 'reader_shards': <integer> |
| store_raw_data | kafka | job_options | boolean | False | True | 'store_raw_data': True/False |
| start_from | kafka | job_options | value | False | True | 'start_from': 'BEGINNING/NOW' |
| end_at | kafka | job_options | value | True | True | 'end_at': '<timestamp>/NOW' |
| compute_cluster | kafka | job_options | identifier | True | True | 'compute_cluster': '<compute_cluster>' |
| run_parallelism | kafka | job_options | integer | True | True | 'run_parallelism': <integer> |
| content_type | kafka | job_options | value | True | True | 'content_type': 'AUTO/CSV/...' |
| compression | kafka | job_options | value | False | True | 'compression': 'AUTO/GZIP/...' |
| comment | kafka | job_options | text | True | True | 'comment': '<comment>' |
| table_include_list | mysql | source_options | list | True | True | 'table_include_list': ('<regexFilter>', ...) |
| column_exclude_list | mysql | source_options | list | True | True | 'column_exclude_list': ('<regexFilter>', ...) |
| exclude_columns | mysql | job_options | list | False | True | 'exclude_columns': ('<exclude_column>', ...) |
| column_transformations | mysql | job_options | dict | False | True | 'column_transformations': {'<column>' : '<expression>' , ...} |
| skip_snapshots | mysql | job_options | boolean | True | True | 'skip_snapshots': True/False |
| end_at | mysql | job_options | value | True | True | 'end_at': '<timestamp>/NOW' |
| compute_cluster | mysql | job_options | identifier | True | True | 'compute_cluster': '<compute_cluster>' |
| comment | mysql | job_options | text | True | True | 'comment': '<comment>' |
| table_include_list | postgres | source_options | list | False | False | 'table_include_list': ('<regexFilter>', ...) |
| column_exclude_list | postgres | source_options | list | False | True | 'column_exclude_list': ('<regexFilter>', ...) |
| heartbeat_table | postgres | job_options | text | False | True | 'heartbeat_table': '<heartbeat_table>' |
| skip_snapshots | postgres | job_options | boolean | False | True | 'skip_snapshots': True/False |
| publication_name | postgres | job_options | text | False | False | 'publication_name': '<publication_name>' |
| end_at | postgres | job_options | value | True | True | 'end_at': '<timestamp>/NOW' |
| start_from | postgres | job_options | value | False | True | 'start_from': '<timestamp>/NOW/BEGINNING' |
| compute_cluster | postgres | job_options | identifier | True | True | 'compute_cluster': '<compute_cluster>' |
| comment | postgres | job_options | text | True | True | 'comment': '<comment>' |
| parse_json_columns | postgres | job_options | boolean | False | False | 'parse_json_columns': True/False |
| column_transformations | postgres | job_options | dict | False | True | 'column_transformations': {'<column>' : '<expression>' , ...} |
| exclude_columns | postgres | job_options | list | False | True | 'exclude_columns': ('<exclude_column>', ...) |
| location | s3 | source_options | text | False | False | 'location': '<location>' |
| date_pattern | s3 | job_options | text | False | True | 'date_pattern': '<date_pattern>' |
| file_pattern | s3 | job_options | text | False | True | 'file_pattern': '<file_pattern>' |
| initial_load_pattern | s3 | job_options | text | False | True | 'initial_load_pattern': '<initial_load_pattern>' |
| initial_load_prefix | s3 | job_options | text | False | True | 'initial_load_prefix': '<initial_load_prefix>' |
| delete_files_after_load | s3 | job_options | boolean | False | True | 'delete_files_after_load': True/False |
| deduplicate_with | s3 | job_options | dict | False | True | 'deduplicate_with': {'COLUMNS' : ['col1', 'col2'],'WINDOW': 'N HOURS'} |
| end_at | s3 | job_options | value | True | True | 'end_at': '<timestamp>/NOW' |
| start_from | s3 | job_options | value | False | True | 'start_from': '<timestamp>/NOW/BEGINNING' |
| compute_cluster | s3 | job_options | identifier | True | True | 'compute_cluster': '<compute_cluster>' |
| run_parallelism | s3 | job_options | integer | True | True | 'run_parallelism': <integer> |
| content_type | s3 | job_options | value | True | True | 'content_type': 'AUTO/CSV...' |
| compression | s3 | job_options | value | False | True | 'compression': 'AUTO/GZIP...' |
| comment | s3 | job_options | text | True | True | 'comment': '<comment>' |
| column_transformations | s3 | job_options | dict | False | True | 'column_transformations': {'<column>' : '<expression>' , ...} |
| exclude_columns | s3 | job_options | list | False | True | 'exclude_columns': ('<exclude_column>', ...) |
| stream | kinesis | source_options | text | False | False | 'stream': '<stream>' |
| reader_shards | kinesis | job_options | integer | True | True | 'reader_shards': <integer> |
| store_raw_data | kinesis | job_options | boolean | False | True | 'store_raw_data': True/False |
| start_from | kinesis | job_options | value | False | True | 'start_from': '<timestamp>/NOW/BEGINNING' |
| end_at | kinesis | job_options | value | False | True | 'end_at': '<timestamp>/NOW' |
| compute_cluster | kinesis | job_options | identifier | True | True | 'compute_cluster': '<compute_cluster>' |
| run_parallelism | kinesis | job_options | integer | False | True | 'run_parallelism': <integer> |
| content_type | kinesis | job_options | value | True | True | 'content_type': 'AUTO/CSV...' |
| compression | kinesis | job_options | value | False | True | 'compression': 'AUTO/GZIP...' |
| comment | kinesis | job_options | text | True | True | 'comment': '<comment>' |
| column_transformations | kinesis | job_options | text | True | True | 'column_transformations': {'<column>' : '<expression>' , ...} |
| deduplicate_with | kinesis | job_options | dict | False | True | 'deduplicate_with': {'COLUMNS' : ['col1', 'col2'],'WINDOW': 'N HOURS'} |
| exclude_columns | kinesis | job_options | list | False | True | 'exclude_columns': ('<exclude_column>', ...) |
