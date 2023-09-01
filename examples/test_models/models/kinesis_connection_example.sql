{{ config(
        	materialized='connection',
        	connection_type='kinesis',
          connection_options={
            'aws_role': 'arn:aws:iam::949275490180:role/upsolver_samples_role',
            'external_id': 'external_id_value',
            'read_only': True,
            'region': 'region_value',
            'aws_access_key_id': 'aws_access_key_id_value',
            'aws_secret_access_key': 'aws_secret_access_key_value',
            'max_writers': 2,
            'stream_display_filters': ('s3://bucket1/', 's3://bucket2/folder-path/'),
            'ENCRYPTION_KMS_KEY': 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
            'encryption_customer_managed_key': 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
          }
    	)
}}
