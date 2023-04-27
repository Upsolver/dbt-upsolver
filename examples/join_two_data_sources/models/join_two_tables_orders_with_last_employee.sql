{{ config(  materialized='incremental',
            map_columns_by_name=True,
            incremental_strategy='insert',
            options={
              	'START_FROM': 'BEGINNING',
                'ADD_MISSING_COLUMNS': True,
                'RUN_INTERVAL': '1 MINUTE'
            }
          )
}}

SELECT
   s.orderid,
   mv.employeeid AS employeeid,
   mv.firstname AS firstname,
   mv.lastname AS lastname
FROM {{ ref('load_orders_raw_data_from_s3') }} as s
LEFT JOIN {{ ref('physical_store_orders_materialized_view') }} AS mv
ON mv.orderid = s.orderid
WHERE mv.source = 'Store'
AND $commit_time between run_start_time() AND run_end_time();
