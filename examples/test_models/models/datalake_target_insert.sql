{{ config(  materialized='incremental',
            incremental_strategy='insert',
            sync=True,
            map_columns_by_name=True,
            options={
                'add_missing_columns': True,
              	'start_from': 'BEGINNING',
                'end_at': 'NOW',
                'run_interval': '1 MINUTE',
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
