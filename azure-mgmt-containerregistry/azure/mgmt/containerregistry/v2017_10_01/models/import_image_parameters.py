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


class ImportImageParameters(Model):
    """ImportImageParameters.

    All required parameters must be populated in order to send to Azure.

    :param source_repository: Required. Repository name of the source image.
    :type source_repository: str
    :param source_tag: The tag name of the source image.  When both source tag
     and source manifest are omitted the 'latest' tag will be used.
     Exclusive with SourceManifestDigest.
    :type source_tag: str
    :param source_manifest_digest: The manifest sha of the source image.
     Exclusive with SourceTag.
    :type source_manifest_digest: str
    :param source: Required. The source of the image.
    :type source:
     ~azure.mgmt.containerregistry.v2017_10_01.models.ImportSource
    :param target_tags: List of strings of the form repo[:tag].  When tag is
     omitted the source will be used (or 'latest' if source tag is also
     omitted.)
    :type target_tags: list[str]
    :param untagged_target_repositories: List of strings of repository names
     to do a manifest only copy.  No tag will be created.
    :type untagged_target_repositories: list[str]
    :param mode: When Force, any existing target tags will be overwritten.
     When NoForce, any existing target tags will fail the operation before any
     copying begins.
     NoForce is the default. Possible values include: 'NoForce', 'Force'
    :type mode: str or
     ~azure.mgmt.containerregistry.v2017_10_01.models.ImportMode
    """

    _validation = {
        'source_repository': {'required': True},
        'source': {'required': True},
    }

    _attribute_map = {
        'source_repository': {'key': 'sourceRepository', 'type': 'str'},
        'source_tag': {'key': 'sourceTag', 'type': 'str'},
        'source_manifest_digest': {'key': 'sourceManifestDigest', 'type': 'str'},
        'source': {'key': 'source', 'type': 'ImportSource'},
        'target_tags': {'key': 'targetTags', 'type': '[str]'},
        'untagged_target_repositories': {'key': 'untaggedTargetRepositories', 'type': '[str]'},
        'mode': {'key': 'mode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImportImageParameters, self).__init__(**kwargs)
        self.source_repository = kwargs.get('source_repository', None)
        self.source_tag = kwargs.get('source_tag', None)
        self.source_manifest_digest = kwargs.get('source_manifest_digest', None)
        self.source = kwargs.get('source', None)
        self.target_tags = kwargs.get('target_tags', None)
        self.untagged_target_repositories = kwargs.get('untagged_target_repositories', None)
        self.mode = kwargs.get('mode', None)
