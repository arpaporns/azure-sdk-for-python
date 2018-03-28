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


class VirtualMachineExtensionsListResult(Model):
    """The List Extension operation response.

    :param value: The list of extensions
    :type value:
     list[~azure.mgmt.compute.v2017_03_30.models.VirtualMachineExtension]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[VirtualMachineExtension]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(VirtualMachineExtensionsListResult, self).__init__(**kwargs)
        self.value = value
