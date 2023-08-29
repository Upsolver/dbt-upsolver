{{ config(  materialized='incremental',
            sync=True,
            source = 'mssql',
        	  options={
            'table_include_list': ('regexFilter1', 'regexFilter2'),
            'column_exclude_list': ('regexFilter1'),
            'exclude_columns': ('exclude_column'),
            'column_transformations': {'hashed_email' : 'MD5(customer.email)'},
            'skip_snapshots': True,
            'end_at': 'NOW',
            'start_from': 'BEGINNING',
            'comment': 'comment_value',
            'snapshot_parallelism': 1,
            'parse_json_columns': True
            },
        	partition_by=[{'field':'$event_date'}]
      	)
}}
SELECT * FROM {{ ref('mssql_connection_example') }}
