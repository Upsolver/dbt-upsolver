{{ config(  materialized='incremental',
            incremental_strategy='merge',
            map_columns_by_name=True,
            sync=True,
            options={'START_FROM': 'NOW',
              'ADD_MISSING_COLUMNS': True,
              'RUN_INTERVAL': '1 MINUTE'},
            primary_key=[{'field':'orderid', 'type':'string'}],
            delete_condition='nettotal > 1000' )
}}

SELECT
 *
FROM {{ source('upsert_records_new', 'orders_raw_data_for_upsert') }}
WHERE $event_time BETWEEN run_start_time() AND run_end_time()
