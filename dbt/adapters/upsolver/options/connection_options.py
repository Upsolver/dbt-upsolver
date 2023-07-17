Connection_options = {
  "s3": {
        "aws_role": {"type": "text", "editable": True, "optional": True,
            "description":"""The AWS IAM role ARN. Used in conjunction with EXTERNAL_ID.
            If omitted, the role created when integrating Upsolver with the AWS account is used.
            To learn how to provide a role with the proper credentials, see: Configure access to S3"""
        },
        "external_id": {"type": "text", "editable": True, "optional": True,
                    "description":"""The external ID of the role to assume. Used in conjunction with AWS_ROLE.
                    If omitted, the role created when integrating Upsolver with the AWS account is used"""
        },
        "aws_access_key_id": {"type": "text", "editable": True, "optional": True,
                    "description":"""The AWS access key ID. Used in conjunction with AWS_SECRET_ACCESS_KEY.
                    If omitted, the role created when integrating Upsolver with the AWS account is used"""
        },
        "aws_secret_access_key_id": {"type": "text", "editable": True, "optional": True,
                    "description":"""The AWS secret key corresponding to the provided AWS_ACCESS_KEY_ID.
                    If omitted, the role created when integrating Upsolver with the AWS account is used"""
        },
        "path_display_filter": {"type": "text", "editable": True, "optional": True,
                    "description":"""A single path to show. If not provided, all buckets are shown.
                    Paths should be provided in the following format: s3://bucket/prefix. This shows anything beginning with the given prefix.
                    To filter by a specific folder, use the following format: s3://bucket/folder-path/"""
        },
        "path_display_filters": {"type": "list", "editable": True, "optional": True,
                    "description":"""The list of paths to show. If not provided, all buckets are shown.
                    Paths should be provided in the following format: s3://bucket/prefix. This shows anything beginning with the given prefix.
                    To filter by a specific folder, use the following format: s3://bucket/folder-path/"""
        },
        "read_only": {"type": "boolean", "editable": True, "optional": True,
                    "description":"""Whether or not the connection is read-only.
                    When true, Upsolver is not able to write data to or delete data from, the bucket"""
        },
        "encryption_kms_key": {"type": "text", "editable": True, "optional": True,
                    "description":"""The ARN of the KMS key to use.
                    If omitted, uses the default encryption defined on the bucket in AWS"""
        },
        "encryption_customer_kms_key": {"type": "text", "editable": True, "optional": True,
                    "description":"""The Base64 text representation of the encryption key to use.
                    If omitted, uses the default encryption defined on the bucket in AWS"""
        },
        "comment": {"type": "text", "editable": True, "optional": True,
                    "description":"""A description or comment regarding this connection"""
        }
  },
    "kafka": {
        "host": {"type": "text", "editable": False, "optional": False,
                    "description":"""A single host in the format of hostname:port"""
        },
        "hosts": {"type": "list", "editable": False, "optional": False,
                    "description":"""The list of Kafka hosts in the format of hostname:port"""
        },
        "consumer_properties": {"type": "text", "editable": True, "optional": True,
                    "description":"""Extra properties to configure for the consumer"""
        },
        "version": {"type": "value", "editable": False, "optional": True,
                    "description":"""Legacy is for anything before 0.10. Default: CURRENT"""
        },
        "require_static_ip": {"type": "boolean", "editable": True, "optional": True,
                    "description":"""With Upsolver clusters, you can configure how many elastic IPs
                    it should allocate and use within that cluster.
                    If the cluster running the job has at least one elastic IP set and REQUIRE_STATIC_IP
                    is enabled, then the job runs on a server that has an elastic IP associated with it.
                    Default: true"""
        },
        "ssl": {"type": "boolean", "editable": True, "optional": True,
                    "description":"""If enabled, SSL is used to connect.
                    Please contact Upsolver to ensure your CA certificate is supported. Default: false"""
        },
        "topic_display_filter": {"type": "text", "editable": True, "optional": True,
                    "description":"""A single topic to show. If left empty, all topics are visible"""
        },
        "topic_display_filters": {"type": "list", "editable": True, "optional": True,
                    "description":"""The list of topics to show. If left empty, all topics are visible"""
        },
        "comment": {"type": "text", "editable": True, "optional": True,
                    "description":"""A description or comment regarding this connection"""
        }
    },
    "glue_catalog": {
        "aws_role": {"type": "text", "editable": True, "optional": True,
                    "description":"""The AWS IAM role ARN. Used in conjunction with EXTERNAL_ID.
                    If omitted, the role created when integrating Upsolver with the AWS account is used"""
        },
        "external_id": {"type": "text", "editable": True, "optional": True,
                    "description":"""The external ID of the role to assume. Used in conjunction with AWS_ROLE.
                    If omitted, the role created when integrating Upsolver with the AWS account is used"""
        },
        "aws_access_key_id": {"type": "text", "editable": True, "optional": True,
                    "description":"""The AWS access key ID. Used in conjunction with AWS_SECRET_ACCESS_KEY.
                    If omitted, the role created when integrating Upsolver with the AWS account is used"""
        },
        "aws_secret_access_key": {"type": "text", "editable": True, "optional": True,
                    "description":"""The AWS secret key corresponding to the provided AWS_ACCESS_KEY_ID.
                    If omitted, the role created when integrating Upsolver with the AWS account is used"""
        },
        "default_storage_connection": {"type": "identifier", "editable": False, "optional": False,
                    "description":"""An Amazon S3 connection with the appropriate credentials to write to the
                    DEFAULT_STORAGE_LOCATION provided"""
        },
        "default_storage_location": {"type": "text", "editable": False, "optional": False,
                    "description":"""The Amazon S3 path that serves as the default storage location for the
                    underlying files associated with tables created under this metastore connection"""
        },
        "region": {"type": "text", "editable": False, "optional": True,
                    "description":"""The region your Glue Catalog is in.
                    Default: Region in which Upsolver is deployed within your AWS account"""
        },
        "database_display_filter": {"type": "text", "editable": True, "optional": True,
                    "description":"""A single database to show.
                    If left empty, all databases are visible"""
        },
        "database_display_filters": {"type": "list", "editable": True, "optional": True,
                    "description":"""The list of databases to show.
                    If left empty, all databases are visible"""
        },
        "comment": {"type": "text", "editable": True, "optional": True,
                    "description":"""A description or comment regarding this connection"""
        }
    },
    "kinesis": {
        "aws_role": {"type": "text", "editable": True, "optional": True,
                    "description":"""The AWS IAM role ARN. Used in conjunction with EXTERNAL_ID.
                    If omitted, the role created when integrating Upsolver with the AWS account is used"""
        },
        "external_id": {"type": "text", "editable": True, "optional": True,
                    "description":"""The external ID of the role to assume. Used in conjunction with AWS_ROLE.
                    If omitted, the role created when integrating Upsolver with the AWS account is used"""
        },
        "aws_access_key_id": {"type": "text", "editable": True, "optional": True,
                    "description":"""The AWS access key ID. Used in conjunction with AWS_SECRET_ACCESS_KEY.
                    If omitted, the role created when integrating Upsolver with the AWS account is used"""
        },
        "aws_secret_access_key": {"type": "text", "editable": True, "optional": True,
                    "description":"""The AWS secret key corresponding to the provided AWS_ACCESS_KEY_ID.
                    If omitted, the role created when integrating Upsolver with the AWS account is used"""
        },
        "region": {"type": "text", "editable": False, "optional": False,
                    "description":"""The AWS region to use"""
        },
        "read_only": {"type": "boolean", "editable": False, "optional": True,
                    "description":"""When true, the connection can only be used to read data from Kinesis
                    and not for writing data to Kinesis. Default: false"""
        },
        "max_writers": {"type": "integer", "editable": True, "optional": True,
                    "description":"""The number of maximum parallel writers to Kinesis. Default: 20"""
        },
        "stream_display_filter": {"type": "text", "editable": True, "optional": True,
                    "description":"""A single stream to show. If left empty, all streams are visible"""
        },
        "stream_display_filters": {"type": "list", "editable": True, "optional": True,
                    "description":"""The list of streams to show. If left empty, all streams are visible"""
        },
        "comment": {"type": "text", "editable": True, "optional": True,
                    "description":"""A description or comment regarding this connection"""
        }
    },
    "snowflake": {
        "connection_string": {"type": "text", "editable": True, "optional": False,
                    "description":"""The connection string to use when connecting to the database.
                    Format: jdbc:snowflake://<ACCOUNT_WITH_REGION>.snowflakecomputing.com?db=<DB_NAME>&warehouse=<WAREHOUSE_NAME>&role=<ROLE_NAME >
                    Where: ACCOUNT_WITH_REGION.snowflakecomputing.com
                    The connection URL in Snowflake.
                    Example: snowflakedemo.us-east-2.aws.snowflakecomputing.com
                    DB_NAME The name of the database to connect to.
                    WAREHOUSE_NAME (Optional) The warehouse name. If not provided, the default warehouse is used. If no default warehouse exists, the CREATE CONNECTION command fails.
                    ROLE_NAME (Optional) The name of the role to use when connecting. If not provided, the default role is used. If no default role exists, the CREATE CONNECTION command fails.
                    Read more about connection string arguments in Snowflake"""
        },
        "user_name": {"type": "text", "editable": True, "optional": False,
                    "description":"""The user to authenticate to the database with"""
        },
        "password": {"type": "text", "editable": True, "optional": False,
                    "description":"""The password for the user"""
        },
        "max_concurrent_connections": {"type": "integer", "editable": True, "optional": True,
                    "description":"""The maximum number of concurrent connections to the database.
                    Limiting this may reduce the load on the database but could result in longer data latency"""
        },
        "comment": {"type": "text", "editable": True, "optional": True,
                    "description":"""A description or comment regarding this connection"""
        }
    },
    "redshift": {
        "connection_string": {"type": "text", "editable": True, "optional": False,
                    "description":"""The connection string to use when connecting to the database.
                    Format:
                    jdbc:snowflake://<ACCOUNT_WITH_REGION>.snowflakecomputing.com?db=<DB_NAME>&warehouse=<WAREHOUSE_NAME>&role=<ROLE_NAME >
                    Where:
                    ACCOUNT_WITH_REGION.snowflakecomputing.com
                    The connection URL in Snowflake.
                    Example: snowflakedemo.us-east-2.aws.snowflakecomputing.com
                    DB_NAME
                    The name of the database to connect to.
                    WAREHOUSE_NAME
                    (Optional) The warehouse name. If not provided, the default warehouse is used. If no default warehouse exists, the CREATE CONNECTION command fails.
                    ROLE_NAME
                    (Optional) The name of the role to use when connecting. If not provided, the default role is used. If no default role exists, the CREATE CONNECTION command fails.
                    Read more about connection string arguments in Snowflake"""
        },
        "user_name": {"type": "text", "editable": True, "optional": False,
                    "description":"""The user to authenticate to the database with"""
        },
        "password": {"type": "text", "editable": True, "optional": False,
                    "description":"""The password for the user"""
        },
        "max_concurrent_connections": {"type": "integer", "editable": True, "optional": True,
                    "description":"""The maximum number of concurrent connections to the database.
                    Limiting this may reduce the load on the database but could result in longer data latency"""
        },
        "comment": {"type": "text", "editable": True, "optional": True,
                    "description":"""A description or comment regarding this connection"""
        }
    },
    "mysql": {
        "connection_string": {"type": "text", "editable": True, "optional": False,
                    "description":"""The connection string to use when connecting to the database.
                    This string can be copied directly from MySQL.
                    The connection string should include the database name at the end of the string"""
        },
        "user_name": {"type": "text", "editable": True, "optional": False,
                    "description":"""The user to authenticate to the database with"""
        },
        "password": {"type": "text", "editable": True, "optional": False,
                    "description":"""The password for the user"""
        },
        "comment": {"type": "text", "editable": True, "optional": True,
                    "description":"""A description or comment regarding this connection"""
        }
    },
    "postgres": {
        "connection_string": {"type": "text", "editable": True, "optional": False,
                    "description":"""The connection string to use when connecting to the database.
                    This string can be copied directly from PostgreSQL """
        },
        "user_name": {"type": "text", "editable": True, "optional": False,
                    "description":"""The user to authenticate to the database with"""
        },
        "password": {"type": "text", "editable": True, "optional": False,
                    "description":"""The password for the user"""
        },
        "comment": {"type": "text", "editable": True, "optional": True,
                    "description":"""A description or comment regarding this connection"""
        }
    },
    "elasticsearch": {
        "connection_string": {"type": "text", "editable": True, "optional": False,
                    "description":"""The connection string to use when connecting to the cluster.
                    Format: 'elasticsearch://host:port?cluster.name=your_cluster_name'"""
        },
        "user_name": {"type": "text", "editable": True, "optional": False,
                    "description":"""The user to authenticate to the cluster"""
        },
        "password": {"type": "text", "editable": True, "optional": False,
                    "description":"""The password for the user"""
        },
        "comment": {"type": "text", "editable": True, "optional": True,
                    "description":"""A description or comment regarding this connection"""
        }
    }
}
