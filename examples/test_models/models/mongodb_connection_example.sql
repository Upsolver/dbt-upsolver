{{ config(
        	materialized='connection',
        	connection_type='MONGODB',
          connection_options={
            'connection_string': 'connection_string_value',
            'user_name': 'user_name_value',
            'password': 'password_value',
            'timeout': "INTERVAL '4' SECONDS",
            'comment': 'comment_value'
          }
    	)
}}
