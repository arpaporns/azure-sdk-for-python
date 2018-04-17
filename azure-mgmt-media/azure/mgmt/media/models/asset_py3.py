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


class Asset(ProxyResource):
    """An Asset.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar asset_id: The Asset ID.
    :vartype asset_id: str
    :ivar created: The creation date of the Asset.
    :vartype created: datetime
    :ivar last_modified: The last modified date of the Asset.
    :vartype last_modified: datetime
    :param alternate_id: The alternate ID of the Asset.
    :type alternate_id: str
    :param description: The Asset description.
    :type description: str
    :param container: The name of the asset blob container.
    :type container: str
    :param storage_account_id: The ARM resource ID of the Azure Storage
     account containing the Asset.
    :type storage_account_id: str
    :param storage_encryption_format: The Asset encryption format. One of
     None, MediaStorageEncryption, StaticCommonEncryption or
     StaticEnvelopeEncryption. Possible values include: 'None',
     'MediaStorageClientEncryption', 'StaticCommonEncryption',
     'StaticEnvelopeEncryption'
    :type storage_encryption_format: str or
     ~azure.mgmt.media.models.AssetStorageEncryptionFormat
    :param storage_encryption_key: The Base64 encoded key for the Asset
     storage encryption.
    :type storage_encryption_key: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'asset_id': {'readonly': True},
        'created': {'readonly': True},
        'last_modified': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'asset_id': {'key': 'properties.assetId', 'type': 'str'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'last_modified': {'key': 'properties.lastModified', 'type': 'iso-8601'},
        'alternate_id': {'key': 'properties.alternateId', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'container': {'key': 'properties.container', 'type': 'str'},
        'storage_account_id': {'key': 'properties.storageAccountId', 'type': 'str'},
        'storage_encryption_format': {'key': 'properties.storageEncryptionFormat', 'type': 'AssetStorageEncryptionFormat'},
        'storage_encryption_key': {'key': 'properties.storageEncryptionKey', 'type': 'str'},
    }

    def __init__(self, *, alternate_id: str=None, description: str=None, container: str=None, storage_account_id: str=None, storage_encryption_format=None, storage_encryption_key: str=None, **kwargs) -> None:
        super(Asset, self).__init__(, **kwargs)
        self.asset_id = None
        self.created = None
        self.last_modified = None
        self.alternate_id = alternate_id
        self.description = description
        self.container = container
        self.storage_account_id = storage_account_id
        self.storage_encryption_format = storage_encryption_format
        self.storage_encryption_key = storage_encryption_key
