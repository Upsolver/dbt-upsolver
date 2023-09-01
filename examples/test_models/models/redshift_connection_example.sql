{{ config(
        	materialized='connection',
        	connection_type='redshift',
          connection_options={
            'connection_string': 'connection_string_value',
            'user_name': 'user_name_value',
            'password': 'password_value',
            'max_concurrent_connections': 2,
            'comment': 'comment_value'
          }
    	)
}}
