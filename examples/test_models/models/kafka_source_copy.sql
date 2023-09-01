{{ config(  materialized='incremental',
            sync=True,
            source = 'kafka',
        	  options={
            'topic': 'orders',
            'consumer_properties': 'consumer_properties_value',
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
            'exclude_columns': ('exclude_column'),
            'reader_shards': 1,
            'store_raw_data': True
            },
        	partition_by=[{'field':'$event_date'}]
      	)
}}
SELECT * FROM {{ ref('kafka_connection_example') }}
