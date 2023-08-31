{{ config(  materialized='incremental',
            incremental_strategy='insert',
            sync=True,
            target_type = 'redshift',
            database = 'redshift_connection_example',
            map_columns_by_name=True,
            options={
              	'start_from': 'BEGINNING',
                'end_at': 'NOW',
                'run_interval': '1 MINUTE',
                'skip_failed_files': True,
                'fail_on_write_error': True,
                'aggregation_parallelism': 1,
                'run_parallelism': 1,
                'skip_validations': ('ALLOW_CARTESIAN_PRODUCT'),
                'comment': 'comment_value'
            	},
            primary_key=[{'field':'partition_date', 'type':'date'}]
          )
}}

SELECT *
 FROM {{ ref('s3_source_copy')}}
 WHERE ordertype = 'SHIPPING'
 AND $event_time BETWEEN run_start_time() AND run_end_time()
