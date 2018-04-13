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

from .create_job_properties import CreateJobProperties


class CreateScopeJobProperties(CreateJobProperties):
    """Scope job properties used when submitting Scope jobs. (Only for use
    internally with Scope job type.).

    All required parameters must be populated in order to send to Azure.

    :param runtime_version: The runtime version of the Data Lake Analytics
     engine to use for the specific type of job being run.
    :type runtime_version: str
    :param script: Required. The script to run. Please note that the maximum
     script size is 3 MB.
    :type script: str
    :param type: Required. Constant filled by server.
    :type type: str
    :param resources: The list of resources that are required by the job.
    :type resources:
     list[~azure.mgmt.datalake.analytics.job.models.ScopeJobResource]
    :param notifier: The list of email addresses, separated by semi-colons, to
     notify when the job reaches a terminal state.
    :type notifier: str
    """

    _validation = {
        'script': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'runtime_version': {'key': 'runtimeVersion', 'type': 'str'},
        'script': {'key': 'script', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[ScopeJobResource]'},
        'notifier': {'key': 'notifier', 'type': 'str'},
    }

    def __init__(self, *, script: str, runtime_version: str=None, resources=None, notifier: str=None, **kwargs) -> None:
        super(CreateScopeJobProperties, self).__init__(runtime_version=runtime_version, script=script, **kwargs)
        self.resources = resources
        self.notifier = notifier
        self.type = 'Scope'
