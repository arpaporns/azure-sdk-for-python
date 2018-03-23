# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class SBQueue(Resource):
    """Description of queue Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :ivar count_details: Message Count Details.
    :vartype count_details: ~azure.mgmt.servicebus.models.MessageCountDetails
    :ivar created_at: The exact time the message was created.
    :vartype created_at: datetime
    :ivar updated_at: The exact time the message was updated.
    :vartype updated_at: datetime
    :ivar accessed_at: Last time a message was sent, or the last time there
     was a receive request to this queue.
    :vartype accessed_at: datetime
    :ivar size_in_bytes: The size of the queue, in bytes.
    :vartype size_in_bytes: long
    :ivar message_count: The number of messages in the queue.
    :vartype message_count: long
    :param lock_duration: ISO 8601 timespan duration of a peek-lock; that is,
     the amount of time that the message is locked for other receivers. The
     maximum value for LockDuration is 5 minutes; the default value is 1
     minute.
    :type lock_duration: timedelta
    :param max_size_in_megabytes: The maximum size of the queue in megabytes,
     which is the size of memory allocated for the queue. Default is 1024.
    :type max_size_in_megabytes: int
    :param requires_duplicate_detection: A value indicating if this queue
     requires duplicate detection.
    :type requires_duplicate_detection: bool
    :param requires_session: A value that indicates whether the queue supports
     the concept of sessions.
    :type requires_session: bool
    :param default_message_time_to_live: ISO 8601 default message timespan to
     live value. This is the duration after which the message expires, starting
     from when the message is sent to Service Bus. This is the default value
     used when TimeToLive is not set on a message itself.
    :type default_message_time_to_live: timedelta
    :param dead_lettering_on_message_expiration: A value that indicates
     whether this queue has dead letter support when a message expires.
    :type dead_lettering_on_message_expiration: bool
    :param duplicate_detection_history_time_window: ISO 8601 timeSpan
     structure that defines the duration of the duplicate detection history.
     The default value is 10 minutes.
    :type duplicate_detection_history_time_window: timedelta
    :param max_delivery_count: The maximum delivery count. A message is
     automatically deadlettered after this number of deliveries. default value
     is 10.
    :type max_delivery_count: int
    :param status: Enumerates the possible values for the status of a
     messaging entity. Possible values include: 'Active', 'Disabled',
     'Restoring', 'SendDisabled', 'ReceiveDisabled', 'Creating', 'Deleting',
     'Renaming', 'Unknown'
    :type status: str or ~azure.mgmt.servicebus.models.EntityStatus
    :param enable_batched_operations: Value that indicates whether server-side
     batched operations are enabled.
    :type enable_batched_operations: bool
    :param auto_delete_on_idle: ISO 8061 timeSpan idle interval after which
     the queue is automatically deleted. The minimum duration is 5 minutes.
    :type auto_delete_on_idle: timedelta
    :param enable_partitioning: A value that indicates whether the queue is to
     be partitioned across multiple message brokers.
    :type enable_partitioning: bool
    :param enable_express: A value that indicates whether Express Entities are
     enabled. An express queue holds a message in memory temporarily before
     writing it to persistent storage.
    :type enable_express: bool
    :param forward_to: Queue/Topic name to forward the messages
    :type forward_to: str
    :param forward_dead_lettered_messages_to: Queue/Topic name to forward the
     Dead Letter message
    :type forward_dead_lettered_messages_to: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'count_details': {'readonly': True},
        'created_at': {'readonly': True},
        'updated_at': {'readonly': True},
        'accessed_at': {'readonly': True},
        'size_in_bytes': {'readonly': True},
        'message_count': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'count_details': {'key': 'properties.countDetails', 'type': 'MessageCountDetails'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
        'accessed_at': {'key': 'properties.accessedAt', 'type': 'iso-8601'},
        'size_in_bytes': {'key': 'properties.sizeInBytes', 'type': 'long'},
        'message_count': {'key': 'properties.messageCount', 'type': 'long'},
        'lock_duration': {'key': 'properties.lockDuration', 'type': 'duration'},
        'max_size_in_megabytes': {'key': 'properties.maxSizeInMegabytes', 'type': 'int'},
        'requires_duplicate_detection': {'key': 'properties.requiresDuplicateDetection', 'type': 'bool'},
        'requires_session': {'key': 'properties.requiresSession', 'type': 'bool'},
        'default_message_time_to_live': {'key': 'properties.defaultMessageTimeToLive', 'type': 'duration'},
        'dead_lettering_on_message_expiration': {'key': 'properties.deadLetteringOnMessageExpiration', 'type': 'bool'},
        'duplicate_detection_history_time_window': {'key': 'properties.duplicateDetectionHistoryTimeWindow', 'type': 'duration'},
        'max_delivery_count': {'key': 'properties.maxDeliveryCount', 'type': 'int'},
        'status': {'key': 'properties.status', 'type': 'EntityStatus'},
        'enable_batched_operations': {'key': 'properties.enableBatchedOperations', 'type': 'bool'},
        'auto_delete_on_idle': {'key': 'properties.autoDeleteOnIdle', 'type': 'duration'},
        'enable_partitioning': {'key': 'properties.enablePartitioning', 'type': 'bool'},
        'enable_express': {'key': 'properties.enableExpress', 'type': 'bool'},
        'forward_to': {'key': 'properties.forwardTo', 'type': 'str'},
        'forward_dead_lettered_messages_to': {'key': 'properties.forwardDeadLetteredMessagesTo', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SBQueue, self).__init__(**kwargs)
        self.count_details = None
        self.created_at = None
        self.updated_at = None
        self.accessed_at = None
        self.size_in_bytes = None
        self.message_count = None
        self.lock_duration = kwargs.get('lock_duration', None)
        self.max_size_in_megabytes = kwargs.get('max_size_in_megabytes', None)
        self.requires_duplicate_detection = kwargs.get('requires_duplicate_detection', None)
        self.requires_session = kwargs.get('requires_session', None)
        self.default_message_time_to_live = kwargs.get('default_message_time_to_live', None)
        self.dead_lettering_on_message_expiration = kwargs.get('dead_lettering_on_message_expiration', None)
        self.duplicate_detection_history_time_window = kwargs.get('duplicate_detection_history_time_window', None)
        self.max_delivery_count = kwargs.get('max_delivery_count', None)
        self.status = kwargs.get('status', None)
        self.enable_batched_operations = kwargs.get('enable_batched_operations', None)
        self.auto_delete_on_idle = kwargs.get('auto_delete_on_idle', None)
        self.enable_partitioning = kwargs.get('enable_partitioning', None)
        self.enable_express = kwargs.get('enable_express', None)
        self.forward_to = kwargs.get('forward_to', None)
        self.forward_dead_lettered_messages_to = kwargs.get('forward_dead_lettered_messages_to', None)
