{{ config(
        	materialized='connection',
        	connection_type='MSSQL',
          connection_options={
            'CONNECTION_STRING': 'CONNECTION_STRING',
            'USER_NAME': 'USER_NAME',
            'PASSWORD': 'PASSWORD',
            'COMMENT': 'COMMENT'
          }
    	)
}}
