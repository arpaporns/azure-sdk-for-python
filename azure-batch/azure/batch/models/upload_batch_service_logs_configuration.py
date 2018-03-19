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


class UploadBatchServiceLogsConfiguration(Model):
    """The Azure Batch service log files upload configuration for a compute node.

    All required parameters must be populated in order to send to Azure.

    :param container_url: Required. The URL of the container within Azure Blob
     Storage to which to upload the Batch Service log file(s). The URL must
     include a Shared Access Signature (SAS) granting write permissions to the
     container. The SAS duration must allow enough time for the upload to
     finish. The start time for SAS is optional and recommended to not be
     specified.
    :type container_url: str
    :param start_time: Required. The start of the time range from which to
     upload Batch Service log file(s). Any log file containing a log message in
     the time range will be uploaded. This means that the operation might
     retrieve more logs than have been requested since the entire log file is
     always uploaded, but the operation should not retrieve fewer logs than
     have been requested.
    :type start_time: datetime
    :param end_time: The end of the time range from which to upload Batch
     Service log file(s). Any log file containing a log message in the time
     range will be uploaded. This means that the operation might retrieve more
     logs than have been requested since the entire log file is always
     uploaded, but the operation should not retrieve fewer logs than have been
     requested. If omitted, the default is to upload all logs available after
     the startTime.
    :type end_time: datetime
    """

    _validation = {
        'container_url': {'required': True},
        'start_time': {'required': True},
    }

    _attribute_map = {
        'container_url': {'key': 'containerUrl', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(UploadBatchServiceLogsConfiguration, self).__init__(**kwargs)
        self.container_url = kwargs.get('container_url', None)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
