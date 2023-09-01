{{ config(
        	materialized='connection',
        	connection_type='mysql',
          connection_options={
            'connection_string': 'connection_string_value',
            'user_name': 'user_name_value',
            'password': 'password_value',
            'comment': 'comment_value'
          }
    	)
}}
