{{ config(  materialized='incremental',
            sync=True,
            source = 'mysql',
        	  options={
            'table_include_list': ('regexFilter1', 'regexFilter2'),
            'column_exclude_list': ('regexFilter1'),
            'exclude_columns': ('exclude_column'),
            'column_transformations': {'hashed_email' : 'MD5(customer.email)'},
            'skip_snapshots': True,
            'end_at': 'NOW',
            'comment': 'comment_value',
            'snapshot_parallelism': 1,
            'ddl_filters': ('filter1', 'filter2')
            },
        	partition_by=[{'field':'$event_date'}]
      	)
}}
SELECT * FROM {{ ref('mysql_connection_example') }}
