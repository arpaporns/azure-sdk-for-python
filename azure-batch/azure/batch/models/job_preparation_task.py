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


class JobPreparationTask(Model):
    """A Job Preparation task to run before any tasks of the job on any given
    compute node.

    You can use Job Preparation to prepare a compute node to run tasks for the
    job. Activities commonly performed in Job Preparation include: Downloading
    common resource files used by all the tasks in the job. The Job Preparation
    task can download these common resource files to the shared location on the
    compute node. (AZ_BATCH_NODE_ROOT_DIR\shared), or starting a local service
    on the compute node so that all tasks of that job can communicate with it.
    If the Job Preparation task fails (that is, exhausts its retry count before
    exiting with exit code 0), Batch will not run tasks of this job on the
    compute node. The node remains ineligible to run tasks of this job until it
    is reimaged. The node remains active and can be used for other jobs. The
    Job Preparation task can run multiple times on the same compute node.
    Therefore, you should write the Job Preparation task to handle
    re-execution. If the compute node is rebooted, the Job Preparation task is
    run again on the node before scheduling any other task of the job, if
    rerunOnNodeRebootAfterSuccess is true or if the Job Preparation task did
    not previously complete. If the compute node is reimaged, the Job
    Preparation task is run again before scheduling any task of the job.

    All required parameters must be populated in order to send to Azure.

    :param id: A string that uniquely identifies the Job Preparation task
     within the job. The ID can contain any combination of alphanumeric
     characters including hyphens and underscores and cannot contain more than
     64 characters. If you do not specify this property, the Batch service
     assigns a default value of 'jobpreparation'. No other task in the job can
     have the same ID as the Job Preparation task. If you try to submit a task
     with the same id, the Batch service rejects the request with error code
     TaskIdSameAsJobPreparationTask; if you are calling the REST API directly,
     the HTTP status code is 409 (Conflict).
    :type id: str
    :param command_line: Required. The command line of the Job Preparation
     task. The command line does not run under a shell, and therefore cannot
     take advantage of shell features such as environment variable expansion.
     If you want to take advantage of such features, you should invoke the
     shell in the command line, for example using "cmd /c MyCommand" in Windows
     or "/bin/sh -c MyCommand" in Linux.
    :type command_line: str
    :param container_settings: The settings for the container under which the
     Job Preparation task runs. When this is specified, all directories
     recursively below the AZ_BATCH_NODE_ROOT_DIR (the root of Azure Batch
     directories on the node) are mapped into the container, all task
     environment variables are mapped into the container, and the task command
     line is executed in the container.
    :type container_settings: ~azure.batch.models.TaskContainerSettings
    :param resource_files: A list of files that the Batch service will
     download to the compute node before running the command line. Files listed
     under this element are located in the task's working directory.
    :type resource_files: list[~azure.batch.models.ResourceFile]
    :param environment_settings: A list of environment variable settings for
     the Job Preparation task.
    :type environment_settings: list[~azure.batch.models.EnvironmentSetting]
    :param constraints: Constraints that apply to the Job Preparation task.
    :type constraints: ~azure.batch.models.TaskConstraints
    :param wait_for_success: Whether the Batch service should wait for the Job
     Preparation task to complete successfully before scheduling any other
     tasks of the job on the compute node. A Job Preparation task has completed
     successfully if it exits with exit code 0. If true and the Job Preparation
     task fails on a compute node, the Batch service retries the Job
     Preparation task up to its maximum retry count (as specified in the
     constraints element). If the task has still not completed successfully
     after all retries, then the Batch service will not schedule tasks of the
     job to the compute node. The compute node remains active and eligible to
     run tasks of other jobs. If false, the Batch service will not wait for the
     Job Preparation task to complete. In this case, other tasks of the job can
     start executing on the compute node while the Job Preparation task is
     still running; and even if the Job Preparation task fails, new tasks will
     continue to be scheduled on the node. The default value is true.
    :type wait_for_success: bool
    :param user_identity: The user identity under which the Job Preparation
     task runs. If omitted, the task runs as a non-administrative user unique
     to the task on Windows nodes, or a a non-administrative user unique to the
     pool on Linux nodes.
    :type user_identity: ~azure.batch.models.UserIdentity
    :param rerun_on_node_reboot_after_success: Whether the Batch service
     should rerun the Job Preparation task after a compute node reboots. The
     Job Preparation task is always rerun if a compute node is reimaged, or if
     the Job Preparation task did not complete (e.g. because the reboot
     occurred while the task was running). Therefore, you should always write a
     Job Preparation task to be idempotent and to behave correctly if run
     multiple times. The default value is true.
    :type rerun_on_node_reboot_after_success: bool
    """

    _validation = {
        'command_line': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'container_settings': {'key': 'containerSettings', 'type': 'TaskContainerSettings'},
        'resource_files': {'key': 'resourceFiles', 'type': '[ResourceFile]'},
        'environment_settings': {'key': 'environmentSettings', 'type': '[EnvironmentSetting]'},
        'constraints': {'key': 'constraints', 'type': 'TaskConstraints'},
        'wait_for_success': {'key': 'waitForSuccess', 'type': 'bool'},
        'user_identity': {'key': 'userIdentity', 'type': 'UserIdentity'},
        'rerun_on_node_reboot_after_success': {'key': 'rerunOnNodeRebootAfterSuccess', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(JobPreparationTask, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.command_line = kwargs.get('command_line', None)
        self.container_settings = kwargs.get('container_settings', None)
        self.resource_files = kwargs.get('resource_files', None)
        self.environment_settings = kwargs.get('environment_settings', None)
        self.constraints = kwargs.get('constraints', None)
        self.wait_for_success = kwargs.get('wait_for_success', None)
        self.user_identity = kwargs.get('user_identity', None)
        self.rerun_on_node_reboot_after_success = kwargs.get('rerun_on_node_reboot_after_success', None)
