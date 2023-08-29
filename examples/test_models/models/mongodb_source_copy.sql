{{ config(  materialized='incremental',
            sync=True,
            source = 'mongodb',
        	  options={
            'collection_include_list': ('regexFilter1', 'regexFilter2'),
            'exclude_columns': ('exclude_column'),
            'column_transformations': {'hashed_email' : 'MD5(customer.email)'},
            'end_at': 'NOW',
            'start_from': 'BEGINNING',
            'comment': 'comment_value',
            'snapshot_parallelism': 1,
            'skip_snapshots': True
            },
        	partition_by=[{'field':'$event_date'}]
      	)
}}
SELECT * FROM {{ ref('mongodb_connection_example') }}
