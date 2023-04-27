{{ config(materialized='materializedview') }}

SELECT orderid,
   LAST(saleinfo.source) as source,
   LAST(saleinfo.store.location.country) as country,
   LAST(saleinfo.store.location.name) as name,
   LAST(saleinfo.store.servicedby.employeeid) as employeeid,
   LAST(saleinfo.store.servicedby.firstname) as firstname,
   LAST(saleinfo.store.servicedby.lastname) as lastname
FROM {{ ref('load_sales_info_raw_data_from_s3') }}
GROUP BY orderid
