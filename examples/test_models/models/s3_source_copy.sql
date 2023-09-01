{{ config(  materialized='incremental',
            sync=True,
            source = 'S3',
        	  options={
            'location': 's3://upsolver-samples/orders/',
            'date_pattern': 'yyyy/MM/dd/HH/mm',
            'file_pattern': 'file_pattern_value',
            'initial_load_pattern': 'initial_load_pattern_value',
            'initial_load_prefix': 'initial_load_prefix_value',
            'delete_files_after_load': False,
            'deduplicate_with': {'COLUMNS' : ['col1', 'col2'],'WINDOW': 'N HOURS'},
            'end_at': 'NOW',
            'start_from': 'BEGINNING',
            'run_parallelism': 3,
            'content_type': 'JSON',
            'compression': 'GZIP',
            'comment': 'comment_value',
            'column_transformations': {'hashed_email' : 'MD5(customer.email)'},
            'commit_interval': '5 MINUTES',
            'skip_validations': ('EMPTY_PATH', 'EMPTY_PATH'),
            'skip_all_validations': True,
            'exclude_columns': ('exclude_column')
            },
        	partition_by=[{'field':'$event_date'}]
      	)
}}
SELECT * FROM {{ ref('s3_connection_example') }}
