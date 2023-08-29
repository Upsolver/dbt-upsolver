{{ config(  materialized='incremental',
            sync=True,
            source = 'postgres',
        	  options={
            'table_include_list': ('regexFilter1', 'regexFilter2'),
            'column_exclude_list': ('regexFilter1'),
            'heartbeat_table': 'heartbeat_table_value',
            'skip_snapshots': True,
            'publication_name': 'publication_name_value',
            'end_at': 'NOW',
            'start_from': 'BEGINNING',
            'comment': 'comment_value',
            'parse_json_columns': True,
            'exclude_columns': ('exclude_column'),
            'column_transformations': {'hashed_email' : 'MD5(customer.email)'},
            'snapshot_parallelism': 1
            },
        	partition_by=[{'field':'$event_date'}]
      	)
}}
SELECT * FROM {{ ref('postgres_connection_example') }}
