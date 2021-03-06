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


class ClusterConfiguration(Model):
    """Information about the standalone cluster configuration.

    :param cluster_configuration: The contents of the cluster configuration
     file.
    :type cluster_configuration: str
    """

    _attribute_map = {
        'cluster_configuration': {'key': 'ClusterConfiguration', 'type': 'str'},
    }

    def __init__(self, cluster_configuration=None):
        super(ClusterConfiguration, self).__init__()
        self.cluster_configuration = cluster_configuration
