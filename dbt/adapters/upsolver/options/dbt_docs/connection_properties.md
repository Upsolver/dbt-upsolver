

## Connection options

| Option | Storage   | Editable | Optional | Config Syntax |
| -------| --------- | -------- | -------- | ------------- |
| aws_role | s3 | True | True | 'aws_role': `'<aws_role>'` |
| external_id | s3 | True | True | 'external_id': `'<external_id>'` |
| aws_access_key_id | s3 | True | True | 'aws_access_key_id': `'<aws_access_key_id>'` |
| aws_secret_access_key_id | s3 | True | True | 'aws_secret_access_key_id': `'<aws_secret_access_key_id>'` |
| path_display_filter | s3 | True | True | 'path_display_filter': `'<path_display_filter>'` |
| path_display_filters | s3 | True | True | 'path_display_filters': (`'<filter>'`, ...) |
| read_only | s3 | True | True | 'read_only': True/False |
| encryption_kms_key | s3 | True | True | 'encryption_kms_key': `'<encryption_kms_key>'` |
| encryption_customer_kms_key | s3 | True | True | 'encryption_customer_kms_key': `'<encryption_customer_kms_key>'` |
| comment | s3 | True | True | 'comment': `'<comment>'` |
| host | kafka | False | False | 'host': `'<host>'` |
| hosts | kafka | False | False | 'hosts': (`'<host>'`, ...) |
| consumer_properties | kafka | True | True | 'consumer_properties': `'<consumer_properties>'` |
| version | kafka | False | True | 'version': `'<value>'` |
| require_static_ip | kafka | True | True | 'require_static_ip': True/False |
| ssl | kafka | True | True | 'ssl': True/False |
| topic_display_filter | kafka | True | True | 'topic_display_filter': `'<topic_display_filter>'` |
| topic_display_filters | kafka | True | True | 'topic_display_filter': (`'<filter>'`, ...) |
| comment | kafka | True | True | 'comment': `'<comment>'` |
| aws_role | glue_catalog | True | True | 'aws_role': `'<aws_role>'` |
| external_id | glue_catalog | True | True | 'external_id': `'<external_id>'` |
| aws_access_key_id | glue_catalog | True | True | 'aws_access_key_id': `'<aws_access_key_id>'` |
| aws_secret_access_key | glue_catalog | True | True | 'aws_secret_access_key': `'<aws_secret_access_key>'` |
| default_storage_connection | glue_catalog | False | False | 'default_storage_connection': `'<default_storage_connection>'` |
| default_storage_location | glue_catalog | False | False | 'default_storage_location': `'<default_storage_location>'` |
| region | glue_catalog | False | True | 'region': `'<region>'` |
| database_display_filter | glue_catalog | True | True | 'database_display_filter': `'<database_display_filter>'` |
| database_display_filters | glue_catalog | True | True | 'database_display_filters': (`'<filter>'`, ...) |
| comment | glue_catalog | True | True | 'comment': `'<comment>'` |
| aws_role | kinesis | True | True | 'aws_role': `'<aws_role>'` |
| external_id | kinesis | True | True | 'external_id': `'<external_id>'` |
| aws_access_key_id | kinesis | True | True | 'aws_access_key_id': `'<aws_access_key_id>'` |
| aws_secret_access_key | kinesis | True | True | 'aws_secret_access_key': `'<aws_secret_access_key>'` |
| region | kinesis | False | False | 'region': `'<region>'` |
| read_only | kinesis | False | True | 'read_only': True/False |
| max_writers | kinesis | True | True | 'max_writers': `<integer>` |
| stream_display_filter | kinesis | True | True | 'stream_display_filter': `'<stream_display_filter>'` |
| stream_display_filters | kinesis | True | True | 'stream_display_filters': (`'<filter>'`, ...) |
| comment | kinesis | True | True | 'comment': `'<comment>'` |
| connection_string | snowflake | True | False | 'connection_string': `'<connection_string>'` |
| user_name | snowflake | True | False | 'user_name': `'<user_name>'` |
| password | snowflake | True | False | 'password': `'<password>'` |
| max_concurrent_connections | snowflake | True | True | 'max_concurrent_connections': `<integer>` |
| comment | snowflake | True | True | 'comment': `'<comment>'` |
| connection_string | redshift | True | False | 'connection_string': `'<connection_string>'` |
| user_name | redshift | True | False | 'user_name': `'<user_name>'` |
| password | redshift | True | False | 'password': `'<password>'` |
| max_concurrent_connections | redshift | True | True | 'max_concurrent_connections': `<integer>` |
| comment | redshift | True | True | 'comment': `'<comment>'` |
| connection_string | mysql | True | False | 'connection_string': `'<connection_string>'` |
| user_name | mysql | True | False | 'user_name': `'<user_name>'` |
| password | mysql | True | False | 'password': `'<password>'` |
| comment | mysql | True | True | 'comment': `'<comment>'` |
| connection_string | postgres | True | False | 'connection_string': `'<connection_string>'` |
| user_name | postgres | True | False | 'user_name': `'<user_name>'` |
| password | postgres | True | False | 'password': `'<password>'` |
| comment | postgres | True | True | 'comment': `'<comment>'` |
| connection_string | elasticsearch | True | False | 'connection_string': `'<connection_string>'` |
| user_name | elasticsearch | True | False | 'user_name': `'<user_name>'` |
| password | elasticsearch | True | False | 'password': `'<password>'` |
| comment | elasticsearch | True | True | 'comment': `'<comment>'` |


## Target options

| Option | Storage   | Editable | Optional | Config Syntax |
| -------| --------- | -------- | -------- | ------------- |
| globally_unique_keys | datalake | False | True | 'globally_unique_keys': True/False |
| storage_connection | datalake | False | True | 'storage_connection': `'<storage_connection>'` |
| storage_location | datalake | False | True | 'storage_location': `'<storage_location>'` |
| compute_cluster | datalake | True | True | 'compute_cluster': `'<compute_cluster>'` |
| compression | datalake | True | True | 'compression': 'SNAPPY/GZIP' |
| compaction_processes | datalake | True | True | 'compaction_processes': `<integer>` |
| disable_compaction | datalake | True | True | 'disable_compaction': True/False |
| retention_date_partition | datalake | False | True | 'retention_date_partition': `'<column>'` |
| table_data_retention | datalake | True | True | 'table_data_retention': `'<N DAYS>'` |
| column_data_retention | datalake | True | True | 'column_data_retention': ({'COLUMN' : `'<column>'`,'DURATION': `'<N DAYS>'`}) |
| comment | datalake | True | True | 'comment': `'<comment>'` |
| storage_connection | materialized_view | False | True | 'storage_connection': `'<storage_connection>'` |
| storage_location | materialized_view | False | True | 'storage_location': `'<storage_location>'` |
| max_time_travel_duration | materialized_view | True | True | 'max_time_travel_duration': `'<N DAYS>'` |
| compute_cluster | materialized_view | True | True | 'compute_cluster': `'<compute_cluster>'` |
| column_transformations | snowflake | False | True | 'column_transformations': {`'<column>'` : `'<expression>'` , ...} |
| deduplicate_with | snowflake | False | True | 'deduplicate_with': {'COLUMNS' : ['col1', 'col2'],'WINDOW': 'N HOURS'} |
| exclude_columns | snowflake | False | True | 'exclude_columns': (`'<exclude_column>'`, ...) |
| create_table_if_missing | snowflake | False | True | 'create_table_if_missing': True/False} |
| run_interval | snowflake | False | True | 'run_interval': `'<N MINUTES/HOURS/DAYS>'` |


## Transformation options

| Option | Storage   | Editable | Optional | Config Syntax |
| -------| --------- | -------- | -------- | ------------- |
| run_interval | s3 | False | True | 'run_interval': `'<N MINUTES/HOURS/DAYS>'` |
| start_from | s3 | False | True | 'start_from': `'<timestamp/NOW/BEGINNING>'` |
| end_at | s3 | True | True | 'end_at': `'<timestamp/NOW>'` |
| compute_cluster | s3 | True | True | 'compute_cluster': `'<compute_cluster>'` |
| comment | s3 | True | True | 'comment': `'<comment>'` |
| allow_cartesian_products | s3 | False | True | 'allow_cartesian_products': True/False |
| aggregation_parallelism | s3 | True | True | 'aggregation_parallelism': `<integer>` |
| run_parallelism | s3 | True | True | 'run_parallelism': `<integer>` |
| file_format | s3 | False | False | 'file_format': 'CSV/TSV ...' |
| compression | s3 | False | True | 'compression': 'SNAPPY/GZIP ...' |
| date_pattern | s3 | False | True | 'date_pattern': `'<date_pattern>'` |
| output_offset | s3 | False | True | 'output_offset': `'<N MINUTES/HOURS/DAYS>'` |
| location | s3 | False | False | 'location': `'<location>'` |
| run_interval | elasticsearch | False | True | 'run_interval': `'<N MINUTES/HOURS/DAYS>'` |
| start_from | elasticsearch | False | True | 'start_from': `'<timestamp/NOW/BEGINNING>'` |
| end_at | elasticsearch | True | True | 'end_at': `'<timestamp/NOW>'` |
| compute_cluster | elasticsearch | True | True | 'compute_cluster': `'<compute_cluster>'` |
| allow_cartesian_products | elasticsearch | False | True | 'allow_cartesian_products': True/False |
| aggregation_parallelism | elasticsearch | True | True | 'aggregation_parallelism': `<integer>` |
| run_parallelism | elasticsearch | True | True | 'run_parallelism': `<integer>` |
| bulk_max_size_bytes | elasticsearch | True | True | 'bulk_max_size_bytes': `<integer>` |
| index_partition_size | elasticsearch | True | True | 'index_partition_size': 'HOURLY/DAILY ...' |
| comment | elasticsearch | True | True | 'comment': `'<comment>'` |
| custom_insert_expressions | snowflake | True | True | 'custom_insert_expressions': {'INSERT_TIME' : 'CURRENT_TIMESTAMP()','MY_VALUE': `'<value>'`} |
| custom_update_expressions | snowflake | True | True | 'custom_update_expressions': {'UPDATE_TIME' : 'CURRENT_TIMESTAMP()','MY_VALUE': `'<value>'`} |
| keep_existing_values_when_null | snowflake | True | True | 'keep_existing_values_when_null': True/False |
| add_missing_columns | snowflake | False | True | 'add_missing_columns': True/False |
| run_interval | snowflake | False | True | 'run_interval': `'<N MINUTES/HOURS/DAYS>'` |
| start_from | snowflake | False | True | 'start_from': `'<timestamp/NOW/BEGINNING>'` |
| end_at | snowflake | True | True | 'end_at': `'<timestamp/NOW>'` |
| compute_cluster | snowflake | True | True | 'compute_cluster': `'<compute_cluster>'` |
| allow_cartesian_products | snowflake | False | True | 'allow_cartesian_products': True/False |
| aggregation_parallelism | snowflake | True | True | 'aggregation_parallelism': `<integer>` |
| run_parallelism | snowflake | True | True | 'run_parallelism': `<integer>` |
| comment | snowflake | True | True | 'comment': `'<comment>'` |
| add_missing_columns | datalake | False | True | 'add_missing_columns': True/False |
| run_interval | datalake | False | True | 'run_interval': `'<N MINUTES/HOURS/DAYS>'` |
| start_from | datalake | False | True | 'start_from': `'<timestamp/NOW/BEGINNING>'` |
| end_at | datalake | True | True | 'end_at': `'<timestamp/NOW>' |
| compute_cluster | datalake | True | True | 'compute_cluster': `'<compute_cluster>'` |
| allow_cartesian_products | datalake | False | True | 'allow_cartesian_products': True/False |
| aggregation_parallelism | datalake | True | True | 'aggregation_parallelism': `<integer>` |
| run_parallelism | datalake | True | True | 'run_parallelism': `<integer>` |
| comment | datalake | True | True | 'comment': `'<comment>'` |
| run_interval | redshift | False | True | 'run_interval': `'<N MINUTES/HOURS/DAYS>'` |
| start_from | redshift | False | True | 'start_from': `'<timestamp/NOW/BEGINNING>'` |
| end_at | redshift | True | True | 'end_at': `'<timestamp/NOW'>` |
| compute_cluster | redshift | True | True | 'compute_cluster': `'<compute_cluster>'` |
| allow_cartesian_products | redshift | False | True | 'allow_cartesian_products': True/False |
| aggregation_parallelism | redshift | True | True | 'aggregation_parallelism': `<integer>` |
| run_parallelism | redshift | True | True | 'run_parallelism': `<integer>` |
| skip_failed_files | redshift | False | True | 'skip_failed_files': True/False |
| fail_on_write_error | redshift | False | True | 'fail_on_write_error': True/False |
| comment | redshift | True | True | 'comment': `'<comment>'` |


## Copy options

| Option | Storage    | Category | Editable | Optional | Config Syntax |
| -------| ---------- | -------- | -------- | -------- | ------------- |
| topic | kafka | source_options | False | False | 'comment': `'<comment>'` |
| exclude_columns | kafka | job_options | False | True | 'exclude_columns': (`'<exclude_column>'`, ...) |
| deduplicate_with | kafka | job_options | False | True | 'deduplicate_with': {'COLUMNS' : ['col1', 'col2'],'WINDOW': 'N HOURS'} |
| consumer_properties | kafka | job_options | True | True | 'comment': `'<comment>'` |
| reader_shards | kafka | job_options | True | True | 'reader_shards': `<integer>` |
| store_raw_data | kafka | job_options | False | True | 'store_raw_data': True/False |
| start_from | kafka | job_options | False | True | 'start_from': 'BEGINNING/NOW' |
| end_at | kafka | job_options | True | True | 'end_at': `'<timestamp/NOW>'` |
| compute_cluster | kafka | job_options | True | True | 'compute_cluster': `'<compute_cluster>'` |
| run_parallelism | kafka | job_options | True | True | 'run_parallelism': `<integer>` |
| content_type | kafka | job_options | True | True | 'content_type': 'AUTO/CSV/...' |
| compression | kafka | job_options | False | True | 'compression': 'AUTO/GZIP/...' |
| comment | kafka | job_options | True | True | 'comment': `'<comment>'` |
| table_include_list | mysql | source_options | True | True | 'table_include_list': (`'<regexFilter>'`, ...) |
| column_exclude_list | mysql | source_options | True | True | 'column_exclude_list': (`'<regexFilter>'`, ...) |
| exclude_columns | mysql | job_options | False | True | 'exclude_columns': (`'<exclude_column>'`, ...) |
| column_transformations | mysql | job_options | False | True | 'column_transformations': {`'<column>'` : `'<expression>'` , ...} |
| skip_snapshots | mysql | job_options | True | True | 'skip_snapshots': True/False |
| end_at | mysql | job_options | True | True | 'end_at': `'<timestamp/NOW>'` |
| compute_cluster | mysql | job_options | True | True | 'compute_cluster': `'<compute_cluster>'` |
| comment | mysql | job_options | True | True | 'comment': `'<comment>'` |
| table_include_list | postgres | source_options | False | False | 'table_include_list': (`'<regexFilter>'`, ...) |
| column_exclude_list | postgres | source_options | False | True | 'column_exclude_list': (`'<regexFilter>'`, ...) |
| heartbeat_table | postgres | job_options | False | True | 'heartbeat_table': `'<heartbeat_table>'` |
| skip_snapshots | postgres | job_options | False | True | 'skip_snapshots': True/False |
| publication_name | postgres | job_options | False | False | 'publication_name': `'<publication_name>'` |
| end_at | postgres | job_options | True | True | 'end_at': `'<timestamp/NOW>'` |
| start_from | postgres | job_options | False | True | 'start_from': `'<timestamp/NOW/BEGINNING>'` |
| compute_cluster | postgres | job_options | True | True | 'compute_cluster': `'<compute_cluster>'` |
| comment | postgres | job_options | True | True | 'comment': `'<comment>'` |
| parse_json_columns | postgres | job_options | False | False | 'parse_json_columns': True/False |
| column_transformations | postgres | job_options | False | True | 'column_transformations': {`'<column>'` : `'<expression>'` , ...} |
| exclude_columns | postgres | job_options | False | True | 'exclude_columns': (`'<exclude_column>'`, ...) |
| location | s3 | source_options | False | False | 'location': `'<location>'` |
| date_pattern | s3 | job_options | False | True | 'date_pattern': `'<date_pattern>'` |
| file_pattern | s3 | job_options | False | True | 'file_pattern': `'<file_pattern>'` |
| initial_load_pattern | s3 | job_options | False | True | 'initial_load_pattern': `'<initial_load_pattern>'` |
| initial_load_prefix | s3 | job_options | False | True | 'initial_load_prefix': `'<initial_load_prefix>'` |
| delete_files_after_load | s3 | job_options | False | True | 'delete_files_after_load': True/False |
| deduplicate_with | s3 | job_options | False | True | 'deduplicate_with': {'COLUMNS' : ['col1', 'col2'],'WINDOW': 'N HOURS'} |
| end_at | s3 | job_options | True | True | 'end_at': `'<timestamp/NOW>'` |
| start_from | s3 | job_options | False | True | 'start_from': `'<timestamp/NOW/BEGINNING>'` |
| compute_cluster | s3 | job_options | True | True | 'compute_cluster': `'<compute_cluster>'` |
| run_parallelism | s3 | job_options | True | True | 'run_parallelism': <integer> |
| content_type | s3 | job_options | True | True | 'content_type': 'AUTO/CSV...' |
| compression | s3 | job_options | False | True | 'compression': 'AUTO/GZIP...' |
| comment | s3 | job_options | True | True | 'comment': `'<comment>'` |
| column_transformations | s3 | job_options | False | True | 'column_transformations': {`'<column>'` : `'<expression>'` , ...} |
| exclude_columns | s3 | job_options | False | True | 'exclude_columns': (`'<exclude_column>'`, ...) |
| stream | kinesis | source_options | False | False | 'stream': `'<stream>'` |
| reader_shards | kinesis | job_options | True | True | 'reader_shards': `<integer>` |
| store_raw_data | kinesis | job_options | False | True | 'store_raw_data': True/False |
| start_from | kinesis | job_options | False | True | 'start_from': `'<timestamp/NOW/BEGINNING>'` |
| end_at | kinesis | job_options | False | True | 'end_at': `'<timestamp/NOW>'` |
| compute_cluster | kinesis | job_options | True | True | 'compute_cluster': `'<compute_cluster>'` |
| run_parallelism | kinesis | job_options | False | True | 'run_parallelism': `<integer>` |
| content_type | kinesis | job_options | True | True | 'content_type': 'AUTO/CSV...' |
| compression | kinesis | job_options | False | True | 'compression': 'AUTO/GZIP...' |
| comment | kinesis | job_options | True | True | 'comment': `'<comment>'` |
| column_transformations | kinesis | job_options | True | True | 'column_transformations': {`'<column>'` : `'<expression>'` , ...} |
| deduplicate_with | kinesis | job_options | False | True | 'deduplicate_with': {'COLUMNS' : ['col1', 'col2'],'WINDOW': 'N HOURS'} |
| exclude_columns | kinesis | job_options | False | True | 'exclude_columns': (`'<exclude_column>'`, ...) |
