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

from .job_properties import JobProperties


class ScopeJobProperties(JobProperties):
    """Scope job properties used when submitting and retrieving Scope jobs. (Only
    for use internally with Scope job type.).

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param runtime_version: The runtime version of the Data Lake Analytics
     engine to use for the specific type of job being run.
    :type runtime_version: str
    :param script: Required. The script to run. Please note that the maximum
     script size is 3 MB.
    :type script: str
    :param type: Required. Constant filled by server.
    :type type: str
    :ivar resources: The list of resources that are required by the job.
    :vartype resources:
     list[~azure.mgmt.datalake.analytics.job.models.ScopeJobResource]
    :ivar user_algebra_path: The algebra file path after the job has
     completed.
    :vartype user_algebra_path: str
    :param notifier: The list of email addresses, separated by semi-colons, to
     notify when the job reaches a terminal state.
    :type notifier: str
    :ivar total_compilation_time: The total time this job spent compiling.
     This value should not be set by the user and will be ignored if it is.
    :vartype total_compilation_time: timedelta
    :ivar total_queued_time: The total time this job spent queued. This value
     should not be set by the user and will be ignored if it is.
    :vartype total_queued_time: timedelta
    :ivar total_running_time: The total time this job spent executing. This
     value should not be set by the user and will be ignored if it is.
    :vartype total_running_time: timedelta
    :ivar total_paused_time: The total time this job spent paused. This value
     should not be set by the user and will be ignored if it is.
    :vartype total_paused_time: timedelta
    :ivar root_process_node_id: The ID used to identify the job manager
     coordinating job execution. This value should not be set by the user and
     will be ignored if it is.
    :vartype root_process_node_id: str
    :ivar yarn_application_id: The ID used to identify the yarn application
     executing the job. This value should not be set by the user and will be
     ignored if it is.
    :vartype yarn_application_id: str
    """

    _validation = {
        'script': {'required': True},
        'type': {'required': True},
        'resources': {'readonly': True},
        'user_algebra_path': {'readonly': True},
        'total_compilation_time': {'readonly': True},
        'total_queued_time': {'readonly': True},
        'total_running_time': {'readonly': True},
        'total_paused_time': {'readonly': True},
        'root_process_node_id': {'readonly': True},
        'yarn_application_id': {'readonly': True},
    }

    _attribute_map = {
        'runtime_version': {'key': 'runtimeVersion', 'type': 'str'},
        'script': {'key': 'script', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[ScopeJobResource]'},
        'user_algebra_path': {'key': 'userAlgebraPath', 'type': 'str'},
        'notifier': {'key': 'notifier', 'type': 'str'},
        'total_compilation_time': {'key': 'totalCompilationTime', 'type': 'duration'},
        'total_queued_time': {'key': 'totalQueuedTime', 'type': 'duration'},
        'total_running_time': {'key': 'totalRunningTime', 'type': 'duration'},
        'total_paused_time': {'key': 'totalPausedTime', 'type': 'duration'},
        'root_process_node_id': {'key': 'rootProcessNodeId', 'type': 'str'},
        'yarn_application_id': {'key': 'yarnApplicationId', 'type': 'str'},
    }

    def __init__(self, *, script: str, runtime_version: str=None, notifier: str=None, **kwargs) -> None:
        super(ScopeJobProperties, self).__init__(runtime_version=runtime_version, script=script, **kwargs)
        self.resources = None
        self.user_algebra_path = None
        self.notifier = notifier
        self.total_compilation_time = None
        self.total_queued_time = None
        self.total_running_time = None
        self.total_paused_time = None
        self.root_process_node_id = None
        self.yarn_application_id = None
        self.type = 'Scope'
