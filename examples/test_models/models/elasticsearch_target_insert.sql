{{ config(  materialized='incremental',
            incremental_strategy='insert',
            sync=True,
            target_type = 'elasticsearch',
            database = 'elasticsearch_connection_example',
            target_prefix = 'orders',
            map_columns_by_name=True,
            options={
              	'start_from': 'BEGINNING',
                'routing_field_name': 'routing_field_name_value',
                'end_at': 'NOW',
                'run_interval': '1 MINUTE',
                'aggregation_parallelism': 1,
                'run_parallelism': 1,
                'comment': 'comment_value',
                'bulk_max_size_bytes': 3,
                'skip_validations': ('ALLOW_CARTESIAN_PRODUCT'),
                'index_partition_size': 'HOURLY'
            	},
            primary_key=[{'field':'partition_date', 'type':'date'}]
          )
}}

SELECT *
 FROM {{ ref('s3_source_copy')}}
 WHERE ordertype = 'SHIPPING'
 AND $event_time BETWEEN run_start_time() AND run_end_time()
