{{ config(
        on_schema_change='fail',
         materialized='incremental',
         sync=True,
         source = 'S3',
          options={
           'CONTENT_TYPE': 'JSON',
           'LOCATION': 's3://upsolver-samples/orders/'
         },
          partition_by=[{'field':'event_date', 'type': 'date'}],
          primary_key=[{'field':'order_id', 'type': 'string'}]
        )
}}
SELECT * FROM {{ ref('s3_connection') }}
