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


class TaskAddParameter(Model):
    """An Azure Batch task to add.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. A string that uniquely identifies the task within the
     job. The ID can contain any combination of alphanumeric characters
     including hyphens and underscores, and cannot contain more than 64
     characters. The ID is case-preserving and case-insensitive (that is, you
     may not have two IDs within a job that differ only by case).
    :type id: str
    :param display_name: A display name for the task. The display name need
     not be unique and can contain any Unicode characters up to a maximum
     length of 1024.
    :type display_name: str
    :param command_line: Required. The command line of the task. For
     multi-instance tasks, the command line is executed as the primary task,
     after the primary task and all subtasks have finished executing the
     coordination command line. The command line does not run under a shell,
     and therefore cannot take advantage of shell features such as environment
     variable expansion. If you want to take advantage of such features, you
     should invoke the shell in the command line, for example using "cmd /c
     MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux.
    :type command_line: str
    :param container_settings: The settings for the container under which the
     task runs. If the pool that will run this task has containerConfiguration
     set, this must be set as well. If the pool that will run this task doesn't
     have containerConfiguration set, this must not be set. When this is
     specified, all directories recursively below the AZ_BATCH_NODE_ROOT_DIR
     (the root of Azure Batch directories on the node) are mapped into the
     container, all task environment variables are mapped into the container,
     and the task command line is executed in the container.
    :type container_settings: ~azure.batch.models.TaskContainerSettings
    :param exit_conditions: How the Batch service should respond when the task
     completes.
    :type exit_conditions: ~azure.batch.models.ExitConditions
    :param resource_files: A list of files that the Batch service will
     download to the compute node before running the command line. For
     multi-instance tasks, the resource files will only be downloaded to the
     compute node on which the primary task is executed.
    :type resource_files: list[~azure.batch.models.ResourceFile]
    :param output_files: A list of files that the Batch service will upload
     from the compute node after running the command line. For multi-instance
     tasks, the files will only be uploaded from the compute node on which the
     primary task is executed.
    :type output_files: list[~azure.batch.models.OutputFile]
    :param environment_settings: A list of environment variable settings for
     the task.
    :type environment_settings: list[~azure.batch.models.EnvironmentSetting]
    :param affinity_info: A locality hint that can be used by the Batch
     service to select a compute node on which to start the new task.
    :type affinity_info: ~azure.batch.models.AffinityInformation
    :param constraints: The execution constraints that apply to this task. If
     you do not specify constraints, the maxTaskRetryCount is the
     maxTaskRetryCount specified for the job, and the maxWallClockTime and
     retentionTime are infinite.
    :type constraints: ~azure.batch.models.TaskConstraints
    :param user_identity: The user identity under which the task runs. If
     omitted, the task runs as a non-administrative user unique to the task.
    :type user_identity: ~azure.batch.models.UserIdentity
    :param multi_instance_settings: An object that indicates that the task is
     a multi-instance task, and contains information about how to run the
     multi-instance task.
    :type multi_instance_settings: ~azure.batch.models.MultiInstanceSettings
    :param depends_on: The tasks that this task depends on. This task will not
     be scheduled until all tasks that it depends on have completed
     successfully. If any of those tasks fail and exhaust their retry counts,
     this task will never be scheduled. If the job does not have
     usesTaskDependencies set to true, and this element is present, the request
     fails with error code TaskDependenciesNotSpecifiedOnJob.
    :type depends_on: ~azure.batch.models.TaskDependencies
    :param application_package_references: A list of application packages that
     the Batch service will deploy to the compute node before running the
     command line. Application packages are downloaded and deployed to a shared
     directory, not the task working directory. Therefore, if a referenced
     package is already on the compute node, and is up to date, then it is not
     re-downloaded; the existing copy on the compute node is used. If a
     referenced application package cannot be installed, for example because
     the package has been deleted or because download failed, the task fails.
    :type application_package_references:
     list[~azure.batch.models.ApplicationPackageReference]
    :param authentication_token_settings: The settings for an authentication
     token that the task can use to perform Batch service operations. If this
     property is set, the Batch service provides the task with an
     authentication token which can be used to authenticate Batch service
     operations without requiring an account access key. The token is provided
     via the AZ_BATCH_AUTHENTICATION_TOKEN environment variable. The operations
     that the task can carry out using the token depend on the settings. For
     example, a task can request job permissions in order to add other tasks to
     the job, or check the status of the job or of other tasks under the job.
    :type authentication_token_settings:
     ~azure.batch.models.AuthenticationTokenSettings
    """

    _validation = {
        'id': {'required': True},
        'command_line': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'container_settings': {'key': 'containerSettings', 'type': 'TaskContainerSettings'},
        'exit_conditions': {'key': 'exitConditions', 'type': 'ExitConditions'},
        'resource_files': {'key': 'resourceFiles', 'type': '[ResourceFile]'},
        'output_files': {'key': 'outputFiles', 'type': '[OutputFile]'},
        'environment_settings': {'key': 'environmentSettings', 'type': '[EnvironmentSetting]'},
        'affinity_info': {'key': 'affinityInfo', 'type': 'AffinityInformation'},
        'constraints': {'key': 'constraints', 'type': 'TaskConstraints'},
        'user_identity': {'key': 'userIdentity', 'type': 'UserIdentity'},
        'multi_instance_settings': {'key': 'multiInstanceSettings', 'type': 'MultiInstanceSettings'},
        'depends_on': {'key': 'dependsOn', 'type': 'TaskDependencies'},
        'application_package_references': {'key': 'applicationPackageReferences', 'type': '[ApplicationPackageReference]'},
        'authentication_token_settings': {'key': 'authenticationTokenSettings', 'type': 'AuthenticationTokenSettings'},
    }

    def __init__(self, *, id: str, command_line: str, display_name: str=None, container_settings=None, exit_conditions=None, resource_files=None, output_files=None, environment_settings=None, affinity_info=None, constraints=None, user_identity=None, multi_instance_settings=None, depends_on=None, application_package_references=None, authentication_token_settings=None, **kwargs) -> None:
        super(TaskAddParameter, self).__init__(**kwargs)
        self.id = id
        self.display_name = display_name
        self.command_line = command_line
        self.container_settings = container_settings
        self.exit_conditions = exit_conditions
        self.resource_files = resource_files
        self.output_files = output_files
        self.environment_settings = environment_settings
        self.affinity_info = affinity_info
        self.constraints = constraints
        self.user_identity = user_identity
        self.multi_instance_settings = multi_instance_settings
        self.depends_on = depends_on
        self.application_package_references = application_package_references
        self.authentication_token_settings = authentication_token_settings
