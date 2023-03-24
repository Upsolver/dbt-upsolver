{{ config(  materialized='incremental',
            sync=True,
            map_columns_by_name=True,
            incremental_strategy='merge',
            options={
              	'START_FROM': 'BEGINNING',
                'ADD_MISSING_COLUMNS': True,
                'RUN_INTERVAL': '1 MINUTE'
            	},
            primary_key=[{'field':'customer_email', 'type':'string'}],
            delete_condition='SUM(nettotal) < 0'
          )
}}

SELECT customer.email AS customer_email,
   COUNT(DISTINCT orderid) AS number_of_orders,
   SUM(nettotal) AS total_sales,
	 MIN(orderdate) AS first_purchase,
   MAX(orderdate) AS last_purchase,
   SUM(nettotal) < 0 as is_delete__placeholder
FROM {{ ref('orders_raw_data_for_upsert_2') }}
WHERE $event_time BETWEEN run_start_time() AND run_end_time()
GROUP BY 1
HAVING COUNT(DISTINCT orderid) > 1
