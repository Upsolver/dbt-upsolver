{{ config(
        	materialized='connection',
        	connection_type='kafka',
          connection_options={
            'hosts': ('host1', 'host2'),
            'consumer_properties': 'consumer_properties_value',
            'version': 'LEGACY',
            'require_static_ip': True,
            'ssl': True,
            'topic_display_filters': ('filter1', 'filter2'),
            'comment': 'comment_value'
          }
    	)
}}
