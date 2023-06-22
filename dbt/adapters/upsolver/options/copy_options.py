Copy_options = {
  "kafka": {
    "source_options": {
        "topic": {"type": "text", "editable": False, "optional": False,
            "description":"""The topic to read from."""
        }
    },
    "job_options": {
        "exclude_columns": {"type": "list", "editable": False, "optional": True,
            "description":"""The EXCLUDE_COLUMNS option tells Upsolver to ignore data in the columns specified in this list, and the column is not created on the target. To exclude columns, provide a single column or a list of column names, or use a glob pattern.
            When you simply don't need columns, you want to save storage space, or maintain a clean data structure, use EXCLUDE_COLUMNS and the specified columns will be ignored. This option gives you control over the width of the target table by enabling you to manage how many columns are created. If your target system has a limit on the number of columns it supports, continuously adding columns can cause issues.
            Furthermore, columns containing sensitive information can be excluded, ensuring private data is not copied downstream to a staging table in your data lake, or directly into your target."""
        },
        "deduplicate_with": {"type": "dict", "editable": False, "optional": True,
            "description":"""You can use DEDUPLICATE_WITH to prevent duplicate rows arriving in your target. One or more columns can be supplied in the column list to act as a key so that all events within the timeframe specified in the WINDOW value are deduplicated.
            For example, if you have a third-party application that sends the same event multiple times a day, you can define one or more columns as the key and set the timeframe to be 1 DAY. Upsolver will exclude all duplicate events that arrive within the day, ensuring your target only receives unique events.
            Note that if you have multiple jobs writing to a table in your lake, duplicate rows can be generated, even when you include this option."""
        },
        "consumer_properties": {"type": "text", "editable": True, "optional": True,
            "description":"""Additional properties to use when configuring the consumer. This overrides any settings in the Apache Kafka connection."""
        },
        "reader_shards": {"type": "integer", "editable": True, "optional": True,
            "description":"""Determines how many readers are used in parallel to read the stream.
            This number does not need to equal your number of partitions in Apache Kafka.
            A recommended value would be to increase it by 1 for every 70 MB/s sent to your topic.
            Default: 1"""
        },
        "store_raw_data": {"type": "boolean", "editable": False, "optional": True,
            "description":"""When true, an additional copy of the data is stored in its original format.
            Default: false"""
        },
        "start_from": {"type": "value", "editable": False, "optional": True,
            "description":""" Configures the time from which to start ingesting data. Files before the specified time are ignored.
            Default: BEGINNING
            Values: { NOW | BEGINNING }"""
        },
        "end_at": {"type": "value", "editable": True, "optional": True,
            "description":"""Configures the time to stop ingesting data. Files after the specified time are ignored.
            Timestamps should be based on UTC and in the following format: TIMESTAMP 'YYYY-MM-DD HH:MM:SS'
            Values: { NOW | <timestamp> }
            Default: Never"""
        },
        "compute_cluster": {"type": "identifier", "editable": True, "optional": True,
            "description":""" The compute cluster to run this job.
            This option can only be omitted when there is only one cluster in your environment.
            If you have more than one compute cluster, you need to determine which one to use through this option.
            Default: The sole cluster in your environment"""
        },
        "run_parallelism": {"type": "integer", "editable": True, "optional": True,
            "description":"""The number of parser jobs to run in parallel per minute.
            Default: 1"""
        },
        "content_type": {"type": "value", "editable": True, "optional": True,
            "description":""" The file format of the content being read.
            Note that AUTO only works when reading Avro, JSON, or Parquet.
            To configure additional options for particular content types, see Content type options.
            Values: { AUTO | CSV | JSON | PARQUET | TSV | AVRO | AVRO_SCHEMA_REGISTRY | FIXED_WIDTH | REGEX | SPLIT_LINES | ORC | XML }
            Default: AUTO"""
        },
        "compression": {"type": "value", "editable": False, "optional": True,
            "description":"""The compression format of the source.
            Values: { AUTO | GZIP | SNAPPY | LZO | NONE | SNAPPY_UNFRAMED | KCL }
            Default: AUTO"""
        },
        "comment": {"type": "text", "editable": True, "optional": True,
            "description":"""A description or comment regarding this job."""
        }
    }
  },
  "mysql": {
    "source_options": {
        "table_include_list": {"type": "list", "editable": True, "optional": True,
            "description":"""Comma-separated list of regular expressions that match fully-qualified table identifiers of tables whose changes you want to capture. This maps to the Debezium table.include.list property.
            By default, the connector captures changes in every non-system table in all databases. To match the name of a table, SQLake applies the regular expression that you specify as an anchored regular expression. That is, the specified expression is matched against the entire name string of the table.  It does not match substrings that might be present in a table name.
            Default: ''"""
        },
        "column_exclude_list": {"type": "list", "editable": True, "optional": True,
            "description":""" Comma-separated list of regular expressions that match the fully-qualified names of columns to exclude from change event record values. This maps to Debezium column.exclude.list property.
            By default, the connector matches all columns of the tables listed in TABLE_INCLUDE_LIST. To match the name of a column, SQLake applies the regular expression that you specify as an anchored regular expression. That is, the specified expression is matched against the entire name string of the column; it does not match substrings that might be present in a column name.
            Default: ''"""
        }
    },
    "job_options": {
        "exclude_columns": {"type": "list", "editable": False, "optional": True,
            "description":"""The EXCLUDE_COLUMNS option tells Upsolver to ignore data in the columns specified in this list, and the column is not created on the target. To exclude columns, provide a single column or a list of column names, or use a glob pattern.
            When you simply don't need columns, you want to save storage space, or maintain a clean data structure, use EXCLUDE_COLUMNS and the specified columns will be ignored. This option gives you control over the width of the target table by enabling you to manage how many columns are created. If your target system has a limit on the number of columns it supports, continuously adding columns can cause issues.
            Furthermore, columns containing sensitive information can be excluded, ensuring private data is not copied downstream to a staging table in your data lake, or directly into your target."""
        "column_transformations": {"type": "dict", "editable": False, "optional": True,
            "description":""" If transformations must be applied prior to data landing in your target, you can use this option to perform data transformations during ingestion. When ingesting into the data lake, it is recommended that you only apply essential transformations, such as protecting PII, as it is easier to make amendments or corrections at a later date if the data remains in its raw state and instead use a transformation job to apply modifications. Therefore, as a general rule, you should only transform data that must be modified before it reaches the target.
            However, transformations provide the flexibility to shape your data before it lands in the target. You can use all the functions and operators supported by Upsolver to create calculated fields within your ingestion job. New columns can be added to your target, and existing column data can be transformed. You can perform actions such as converting data types, formatting string values, and concatenating columns to create a new column.
            If you need to mask sensitive or personally identifiable information (PII) prior to loading into your staging tables or when performing direct ingestion into your target destination, you can use hashing functions to prevent data from being exposed downstream. Combining hash functions with the EXCLUDE_COLUMNS option enables you to control your data protection."""
        },
        "skip_snapshots": {"type": "boolean", "editable": True, "optional": True},
            "description":""" By default, snapshots are enabled for new tables. This means that SQLake will take a full snapshot of the table(s) and ingest it into the staging table before it continues to listen for change events. When set to True, SQLake will not take an initial snapshot and only process change events starting from the time the ingestion job is created.
            In the majority of cases, when you connect to your source tables, you want to take a full snapshot and ingest it as the baseline of your table. This creates a full copy of the source table in your data lake before you begin to stream the most recent change events. If you skip taking a snapshot, you will not have the historical data in the target table, only the newly added or changed rows.
            Skipping a snapshot is useful in scenarios where your primary database instance crashed or became unreachable, failing over to the secondary. In this case, you will need to re-establish the CDC connection but would not want to take a full snapshot because you already have all of the history in your table. In this case, you would want to restart processing from the moment you left off when the connection to the primary database went down."""
        ,
        "end_at": {"type": "value", "editable": True, "optional": True,
            "description":"""Configures the time to stop ingesting data. Files after the specified time are ignored.
            Timestamps should be based on UTC and in the following format: TIMESTAMP 'YYYY-MM-DD HH:MM:SS'
            Default: Never"""
        },
        "compute_cluster": {"type": "identifier", "editable": True, "optional": True,
            "description":"""The compute cluster to run this job.
            This option can only be omitted when there is only one cluster in your environment.
            If you have more than one compute cluster, you need to determine which one to use through this option.
            Default: The sole cluster in your environment"""
        },
        "comment": {"type": "text", "editable": True, "optional": True,
            "description":"""A description or comment regarding this job."""
        }
    }
  },
  "postgres": {
    "source_options": {
        "table_include_list": {"type": "list", "editable": False, "optional": False,
            "description":""" """
        },
        "column_exclude_list": {"type": "list", "editable": False, "optional": True,
            "description":""" """
        }
    },
    "job_options": {
        "heartbeat_table": {"type": "text", "editable": False, "optional": True,
            "description":""" """
        },
        "skip_snapshots": {"type": "boolean", "editable": False, "optional": True,
            "description":""" """
        },
        "publication_name": {"type": "text", "editable": False, "optional": False,
            "description":""" """
        },
        "end_at": {"type": "value", "editable": True, "optional": True,
            "description":""" """
        },
        "compute_cluster": {"type": "identifier", "editable": True, "optional": True,
            "description":""" """
        },
        "comment": {"type": "text", "editable": True, "optional": True,
            "description":""" """
        },
        "parse_json_columns": {"type": "boolean", "editable": False, "optional": False,
            "description":""" """
        }
    }
  },
  "s3": {
    "source_options": {
        "location": {"type": "text", "editable": False, "optional": False,
            "description":""" """
        }
    },
    "job_options": {
        "file_pattern": {"type": "text", "editable": False, "optional": True,
            "description":""" """
        },
        "delete_files_after_load": {"type": "boolean", "editable": False, "optional": True,
            "description":""" """
        },
        "end_at": {"type": "value", "editable": True, "optional": True,
            "description":""" """
        },
        "compute_cluster": {"type": "identifier", "editable": True, "optional": True,
            "description":""" """
        },
        "run_parallelism": {"type": "integer", "editable": True, "optional": True,
            "description":""" """
        },
        "content_type": {"type": "value", "editable": True, "optional": True,
            "description":""" """
        },
        "compression": {"type": "value", "editable": False, "optional": True,
            "description":""" """
        },
        "comment": {"type": "text", "editable": True, "optional": True,
            "description":""" """
        }
    }
  },
    "kinesis": {
      "source_options": {
          "stream": {"type": "text", "editable": False, "optional": False,
              "description":""" """
          }
      },
      "job_options": {
          "reader_shards": {"type": "integer", "editable": True, "optional": True,
              "description":""" """
          },
          "store_raw_data": {"type": "boolean", "editable": False, "optional": True,
              "description":""" """
          },
          "start_from": {"type": "value", "editable": False, "optional": True,
              "description":""" """
          },
          "end_at": {"type": "value", "editable": False, "optional": True,
              "description":""" """
          },
          "compute_cluster": {"type": "identifier", "editable": True, "optional": True,
              "description":""" """
          },
          "run_parallelism": {"type": "integer", "editable": False, "optional": True,
              "description":""" """
          },
          "content_type": {"type": "value", "editable": True, "optional": True,
              "description":""" """
          },
          "compression": {"type": "value", "editable": False, "optional": True,
              "description":""" """
          },
          "comment": {"type": "text", "editable": True, "optional": True,
              "description":""" """
          }
      }
    }
}
