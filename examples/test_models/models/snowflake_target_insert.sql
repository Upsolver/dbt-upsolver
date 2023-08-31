{{ config(  materialized='incremental',
            incremental_strategy='insert',
            sync=True,
            target_type = 'snowflake',
            map_columns_by_name=True,
            options={
                'custom_insert_expressions': {'INSERT_TIME' : 'CURRENT_TIMESTAMP()','MY_VALUE': 'MY_VALUE'},
                'custom_update_expressions': {'UPDATE_TIME' : 'CURRENT_TIMESTAMP()','MY_VALUE': 'MY_VALUE'},
                'keep_existing_values_when_null': True,
                'add_missing_columns': True,
                'commit_interval': '1 MINUTE',
              	'start_from': 'BEGINNING',
                'end_at': 'NOW',
                'run_interval': '1 MINUTE',
                'aggregation_parallelism': 1,
                'run_parallelism': 1,
                'comment': 'comment_value',
                'skip_validations': ('ALLOW_CARTESIAN_PRODUCT')
            	},
            primary_key=[{'field':'partition_date', 'type':'date'}]
          )
}}

SELECT *
 FROM {{ ref('s3_source_copy')}}
 WHERE ordertype = 'SHIPPING'
 AND $event_time BETWEEN run_start_time() AND run_end_time()
