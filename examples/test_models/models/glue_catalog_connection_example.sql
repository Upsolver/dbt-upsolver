{{ config(
        	materialized='connection',
        	connection_type='glue_catalog',
          connection_options={
            'aws_role': 'arn:aws:iam::949275490180:role/upsolver_samples_role',
            'external_id': 'external_id_value',
            'aws_access_key_id': 'aws_access_key_id_value',
            'aws_secret_access_key': 'aws_secret_access_key_value',
            'default_storage_connection': 'default_storage_connection_value',
            'default_storage_location': 's3://<bucket>/<folder-path>/',
            'region': 'region_value',
            'database_display_filters': ('database_name1', 'database_name2'),
            'comment': 'comment_value'
          }
    	)
}}
