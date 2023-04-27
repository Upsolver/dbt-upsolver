{{ config(materialized='incremental',
          source = 'S3',
      	  options={
        	'CONTENT_TYPE': 'JSON',
          'LOCATION': 's3://upsolver-samples/sales_info/'
          },
      	  partition_by=[{'field':'$event_date'}]
    	)
}}

SELECT * FROM {{ ref('upsolver_s3_samples') }}
