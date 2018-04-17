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

from .proxy_resource import ProxyResource


class StreamingPolicy(ProxyResource):
    """A Streaming Policy resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar created: Creation time of Streaming Policy
    :vartype created: datetime
    :param default_content_key_policy_name: Default ContentKey used by current
     Streaming Policy
    :type default_content_key_policy_name: str
    :param envelope_encryption: Configuration of EnvelopeEncryption
    :type envelope_encryption: ~azure.mgmt.media.models.EnvelopeEncryption
    :param common_encryption_cenc: Configuration of CommonEncryptionCenc
    :type common_encryption_cenc:
     ~azure.mgmt.media.models.CommonEncryptionCenc
    :param common_encryption_cbcs: Configuration of CommonEncryptionCbcs
    :type common_encryption_cbcs:
     ~azure.mgmt.media.models.CommonEncryptionCbcs
    :param no_encryption: Configuations of NoEncryption
    :type no_encryption: ~azure.mgmt.media.models.NoEncryption
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'created': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'default_content_key_policy_name': {'key': 'properties.defaultContentKeyPolicyName', 'type': 'str'},
        'envelope_encryption': {'key': 'properties.envelopeEncryption', 'type': 'EnvelopeEncryption'},
        'common_encryption_cenc': {'key': 'properties.commonEncryptionCenc', 'type': 'CommonEncryptionCenc'},
        'common_encryption_cbcs': {'key': 'properties.commonEncryptionCbcs', 'type': 'CommonEncryptionCbcs'},
        'no_encryption': {'key': 'properties.noEncryption', 'type': 'NoEncryption'},
    }

    def __init__(self, *, default_content_key_policy_name: str=None, envelope_encryption=None, common_encryption_cenc=None, common_encryption_cbcs=None, no_encryption=None, **kwargs) -> None:
        super(StreamingPolicy, self).__init__(, **kwargs)
        self.created = None
        self.default_content_key_policy_name = default_content_key_policy_name
        self.envelope_encryption = envelope_encryption
        self.common_encryption_cenc = common_encryption_cenc
        self.common_encryption_cbcs = common_encryption_cbcs
        self.no_encryption = no_encryption
