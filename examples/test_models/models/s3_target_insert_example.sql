{{ config(  materialized='incremental',
            incremental_strategy='insert',
            sync=True,
            target_type = 's3',
            database = 's3_connection_example',
            target_location = 's3://your-bucket-name/path/to/folder/',
            map_columns_by_name=True,
            options={
              	'start_from': 'BEGINNING',
                'end_at': 'NOW',
                'run_interval': '1 MINUTE',
                'compression': 'GZIP',
                'date_pattern': 'yyyy-MM-dd-HH-mm',
                'file_format': '(type = CSV)',
                'aggregation_parallelism': 1,
                'run_parallelism': 1,
                'output_offset': '1 MINUTE',
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
