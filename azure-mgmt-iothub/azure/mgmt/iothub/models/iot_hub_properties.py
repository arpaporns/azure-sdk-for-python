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

from msrest.serialization import Model


class IotHubProperties(Model):
    """The properties of an IoT hub.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param authorization_policies: The shared access policies you can use to
     secure a connection to the IoT hub.
    :type authorization_policies:
     list[~azure.mgmt.iothub.models.SharedAccessSignatureAuthorizationRule]
    :param ip_filter_rules: The IP filter rules.
    :type ip_filter_rules: list[~azure.mgmt.iothub.models.IpFilterRule]
    :ivar provisioning_state: The provisioning state.
    :vartype provisioning_state: str
    :ivar state: Thehub state state.
    :vartype state: str
    :ivar host_name: The name of the host.
    :vartype host_name: str
    :param event_hub_endpoints: The Event Hub-compatible endpoint properties.
     The possible keys to this dictionary are events and
     operationsMonitoringEvents. Both of these keys have to be present in the
     dictionary while making create or update calls for the IoT hub.
    :type event_hub_endpoints: dict[str,
     ~azure.mgmt.iothub.models.EventHubProperties]
    :param routing:
    :type routing: ~azure.mgmt.iothub.models.RoutingProperties
    :param storage_endpoints: The list of Azure Storage endpoints where you
     can upload files. Currently you can configure only one Azure Storage
     account and that MUST have its key as $default. Specifying more than one
     storage account causes an error to be thrown. Not specifying a value for
     this property when the enableFileUploadNotifications property is set to
     True, causes an error to be thrown.
    :type storage_endpoints: dict[str,
     ~azure.mgmt.iothub.models.StorageEndpointProperties]
    :param messaging_endpoints: The messaging endpoint properties for the file
     upload notification queue.
    :type messaging_endpoints: dict[str,
     ~azure.mgmt.iothub.models.MessagingEndpointProperties]
    :param enable_file_upload_notifications: If True, file upload
     notifications are enabled.
    :type enable_file_upload_notifications: bool
    :param cloud_to_device:
    :type cloud_to_device: ~azure.mgmt.iothub.models.CloudToDeviceProperties
    :param comments: IoT hub comments.
    :type comments: str
    :param operations_monitoring_properties:
    :type operations_monitoring_properties:
     ~azure.mgmt.iothub.models.OperationsMonitoringProperties
    :param features: The capabilities and features enabled for the IoT hub.
     Possible values include: 'None', 'DeviceManagement'
    :type features: str or ~azure.mgmt.iothub.models.Capabilities
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'state': {'readonly': True},
        'host_name': {'readonly': True},
    }

    _attribute_map = {
        'authorization_policies': {'key': 'authorizationPolicies', 'type': '[SharedAccessSignatureAuthorizationRule]'},
        'ip_filter_rules': {'key': 'ipFilterRules', 'type': '[IpFilterRule]'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'host_name': {'key': 'hostName', 'type': 'str'},
        'event_hub_endpoints': {'key': 'eventHubEndpoints', 'type': '{EventHubProperties}'},
        'routing': {'key': 'routing', 'type': 'RoutingProperties'},
        'storage_endpoints': {'key': 'storageEndpoints', 'type': '{StorageEndpointProperties}'},
        'messaging_endpoints': {'key': 'messagingEndpoints', 'type': '{MessagingEndpointProperties}'},
        'enable_file_upload_notifications': {'key': 'enableFileUploadNotifications', 'type': 'bool'},
        'cloud_to_device': {'key': 'cloudToDevice', 'type': 'CloudToDeviceProperties'},
        'comments': {'key': 'comments', 'type': 'str'},
        'operations_monitoring_properties': {'key': 'operationsMonitoringProperties', 'type': 'OperationsMonitoringProperties'},
        'features': {'key': 'features', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(IotHubProperties, self).__init__(**kwargs)
        self.authorization_policies = kwargs.get('authorization_policies', None)
        self.ip_filter_rules = kwargs.get('ip_filter_rules', None)
        self.provisioning_state = None
        self.state = None
        self.host_name = None
        self.event_hub_endpoints = kwargs.get('event_hub_endpoints', None)
        self.routing = kwargs.get('routing', None)
        self.storage_endpoints = kwargs.get('storage_endpoints', None)
        self.messaging_endpoints = kwargs.get('messaging_endpoints', None)
        self.enable_file_upload_notifications = kwargs.get('enable_file_upload_notifications', None)
        self.cloud_to_device = kwargs.get('cloud_to_device', None)
        self.comments = kwargs.get('comments', None)
        self.operations_monitoring_properties = kwargs.get('operations_monitoring_properties', None)
        self.features = kwargs.get('features', None)
