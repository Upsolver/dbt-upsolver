Copy_options = {
  "kafka": {
    "source_options": {
        "topic_name": {"type": "text", "editable": False, "optional": False,
            "description":"""The topic name to read from."""
        },
        "topic": {"type": "text", "editable": False, "optional": False,
            "description":"""The topic to read from."""
        }
    },
    "job_options": {
        "consumer_properties": {"type": "text", "editable": True, "optional": True,
            "description":"""Additional properties to use when configuring the consumer. This overrides any settings in the Apache Kafka connection."""
        },
        "reader_shards": {"type": "integer", "editable": True, "optional": True,
            "description":""" """
        },
        "store_raw_data": {"type": "value", "editable": False, "optional": True,
            "description":""" """
        },
        "start_from": {"type": "value", "editable": False, "optional": True,
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
            "description":""" The file format of the content being read.
            Note that AUTO only works when reading Avro, JSON, or Parquet.
            To configure additional options for particular content types, see Content type options.
            Values: { AUTO | CSV | JSON | PARQUET | TSV | AVRO | AVRO_SCHEMA_REGISTRY | FIXED_WIDTH | REGEX | SPLIT_LINES | ORC | XML }
            Default: AUTO"""
        },
        "compression": {"type": "value", "editable": False, "optional": True,
            "description":""" """
        },
        "comment": {"type": "text", "editable": True, "optional": True,
            "description":""" """
        }
    }
  },
  "mysql": {
    "source_options": {
        "table_include_list": {"type": "list", "editable": True, "optional": True,
            "description":""" """
        },
        "column_exclude_list": {"type": "list", "editable": True, "optional": True,
            "description":""" """
        }
    },
    "job_options": {
        "skip_snapshots": {"type": "boolean", "editable": True, "optional": True},
            "description":""" """
        ,
        "end_at": {"type": "value", "editable": True, "optional": True,
            "description":""" """
        },
        "compute_cluster": {"type": "identifier", "editable": True, "optional": True,
            "description":""" """
        },
        "comment": {"type": "text", "editable": True, "optional": True,
            "description":""" """
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
