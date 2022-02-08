# coding: utf-8

"""
    Loadero Controller

    This application serves main Loadero's endpoints that can be used to manipulate test data and other services  # noqa: E501

    OpenAPI spec version: {{ .Version }}
    Contact: support@loadero.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RunBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created': 'datetime',
        'execution_finished': 'datetime',
        'execution_started': 'datetime',
        'group_count': 'int',
        'id': 'int',
        'increment_strategy': 'str',
        'launching_account_id': 'int',
        'metric_status': 'str',
        'mos_test': 'bool',
        'participant_count': 'int',
        'participant_timeout': 'int',
        'processing_finished': 'datetime',
        'processing_started': 'datetime',
        'script_file_id': 'int',
        'start_interval': 'int',
        'status': 'str',
        'success_rate': 'float',
        'test_id': 'int',
        'test_mode': 'str',
        'test_name': 'str',
        'total_cu_count': 'float',
        'updated': 'datetime'
    }

    attribute_map = {
        'created': 'created',
        'execution_finished': 'execution_finished',
        'execution_started': 'execution_started',
        'group_count': 'group_count',
        'id': 'id',
        'increment_strategy': 'increment_strategy',
        'launching_account_id': 'launching_account_id',
        'metric_status': 'metric_status',
        'mos_test': 'mos_test',
        'participant_count': 'participant_count',
        'participant_timeout': 'participant_timeout',
        'processing_finished': 'processing_finished',
        'processing_started': 'processing_started',
        'script_file_id': 'script_file_id',
        'start_interval': 'start_interval',
        'status': 'status',
        'success_rate': 'success_rate',
        'test_id': 'test_id',
        'test_mode': 'test_mode',
        'test_name': 'test_name',
        'total_cu_count': 'total_cu_count',
        'updated': 'updated'
    }

    def __init__(self, created=None, execution_finished=None, execution_started=None, group_count=None, id=None, increment_strategy=None, launching_account_id=None, metric_status=None, mos_test=None, participant_count=None, participant_timeout=None, processing_finished=None, processing_started=None, script_file_id=None, start_interval=None, status=None, success_rate=None, test_id=None, test_mode=None, test_name=None, total_cu_count=None, updated=None):  # noqa: E501
        """RunBody - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._execution_finished = None
        self._execution_started = None
        self._group_count = None
        self._id = None
        self._increment_strategy = None
        self._launching_account_id = None
        self._metric_status = None
        self._mos_test = None
        self._participant_count = None
        self._participant_timeout = None
        self._processing_finished = None
        self._processing_started = None
        self._script_file_id = None
        self._start_interval = None
        self._status = None
        self._success_rate = None
        self._test_id = None
        self._test_mode = None
        self._test_name = None
        self._total_cu_count = None
        self._updated = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if execution_finished is not None:
            self.execution_finished = execution_finished
        if execution_started is not None:
            self.execution_started = execution_started
        if group_count is not None:
            self.group_count = group_count
        if id is not None:
            self.id = id
        if increment_strategy is not None:
            self.increment_strategy = increment_strategy
        if launching_account_id is not None:
            self.launching_account_id = launching_account_id
        if metric_status is not None:
            self.metric_status = metric_status
        if mos_test is not None:
            self.mos_test = mos_test
        if participant_count is not None:
            self.participant_count = participant_count
        if participant_timeout is not None:
            self.participant_timeout = participant_timeout
        if processing_finished is not None:
            self.processing_finished = processing_finished
        if processing_started is not None:
            self.processing_started = processing_started
        if script_file_id is not None:
            self.script_file_id = script_file_id
        if start_interval is not None:
            self.start_interval = start_interval
        if status is not None:
            self.status = status
        if success_rate is not None:
            self.success_rate = success_rate
        if test_id is not None:
            self.test_id = test_id
        if test_mode is not None:
            self.test_mode = test_mode
        if test_name is not None:
            self.test_name = test_name
        if total_cu_count is not None:
            self.total_cu_count = total_cu_count
        if updated is not None:
            self.updated = updated

    @property
    def created(self):
        """Gets the created of this RunBody.  # noqa: E501


        :return: The created of this RunBody.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this RunBody.


        :param created: The created of this RunBody.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def execution_finished(self):
        """Gets the execution_finished of this RunBody.  # noqa: E501


        :return: The execution_finished of this RunBody.  # noqa: E501
        :rtype: datetime
        """
        return self._execution_finished

    @execution_finished.setter
    def execution_finished(self, execution_finished):
        """Sets the execution_finished of this RunBody.


        :param execution_finished: The execution_finished of this RunBody.  # noqa: E501
        :type: datetime
        """

        self._execution_finished = execution_finished

    @property
    def execution_started(self):
        """Gets the execution_started of this RunBody.  # noqa: E501


        :return: The execution_started of this RunBody.  # noqa: E501
        :rtype: datetime
        """
        return self._execution_started

    @execution_started.setter
    def execution_started(self, execution_started):
        """Sets the execution_started of this RunBody.


        :param execution_started: The execution_started of this RunBody.  # noqa: E501
        :type: datetime
        """

        self._execution_started = execution_started

    @property
    def group_count(self):
        """Gets the group_count of this RunBody.  # noqa: E501


        :return: The group_count of this RunBody.  # noqa: E501
        :rtype: int
        """
        return self._group_count

    @group_count.setter
    def group_count(self, group_count):
        """Sets the group_count of this RunBody.


        :param group_count: The group_count of this RunBody.  # noqa: E501
        :type: int
        """

        self._group_count = group_count

    @property
    def id(self):
        """Gets the id of this RunBody.  # noqa: E501


        :return: The id of this RunBody.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RunBody.


        :param id: The id of this RunBody.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def increment_strategy(self):
        """Gets the increment_strategy of this RunBody.  # noqa: E501


        :return: The increment_strategy of this RunBody.  # noqa: E501
        :rtype: str
        """
        return self._increment_strategy

    @increment_strategy.setter
    def increment_strategy(self, increment_strategy):
        """Sets the increment_strategy of this RunBody.


        :param increment_strategy: The increment_strategy of this RunBody.  # noqa: E501
        :type: str
        """

        self._increment_strategy = increment_strategy

    @property
    def launching_account_id(self):
        """Gets the launching_account_id of this RunBody.  # noqa: E501


        :return: The launching_account_id of this RunBody.  # noqa: E501
        :rtype: int
        """
        return self._launching_account_id

    @launching_account_id.setter
    def launching_account_id(self, launching_account_id):
        """Sets the launching_account_id of this RunBody.


        :param launching_account_id: The launching_account_id of this RunBody.  # noqa: E501
        :type: int
        """

        self._launching_account_id = launching_account_id

    @property
    def metric_status(self):
        """Gets the metric_status of this RunBody.  # noqa: E501


        :return: The metric_status of this RunBody.  # noqa: E501
        :rtype: str
        """
        return self._metric_status

    @metric_status.setter
    def metric_status(self, metric_status):
        """Sets the metric_status of this RunBody.


        :param metric_status: The metric_status of this RunBody.  # noqa: E501
        :type: str
        """

        self._metric_status = metric_status

    @property
    def mos_test(self):
        """Gets the mos_test of this RunBody.  # noqa: E501


        :return: The mos_test of this RunBody.  # noqa: E501
        :rtype: bool
        """
        return self._mos_test

    @mos_test.setter
    def mos_test(self, mos_test):
        """Sets the mos_test of this RunBody.


        :param mos_test: The mos_test of this RunBody.  # noqa: E501
        :type: bool
        """

        self._mos_test = mos_test

    @property
    def participant_count(self):
        """Gets the participant_count of this RunBody.  # noqa: E501


        :return: The participant_count of this RunBody.  # noqa: E501
        :rtype: int
        """
        return self._participant_count

    @participant_count.setter
    def participant_count(self, participant_count):
        """Sets the participant_count of this RunBody.


        :param participant_count: The participant_count of this RunBody.  # noqa: E501
        :type: int
        """

        self._participant_count = participant_count

    @property
    def participant_timeout(self):
        """Gets the participant_timeout of this RunBody.  # noqa: E501


        :return: The participant_timeout of this RunBody.  # noqa: E501
        :rtype: int
        """
        return self._participant_timeout

    @participant_timeout.setter
    def participant_timeout(self, participant_timeout):
        """Sets the participant_timeout of this RunBody.


        :param participant_timeout: The participant_timeout of this RunBody.  # noqa: E501
        :type: int
        """

        self._participant_timeout = participant_timeout

    @property
    def processing_finished(self):
        """Gets the processing_finished of this RunBody.  # noqa: E501


        :return: The processing_finished of this RunBody.  # noqa: E501
        :rtype: datetime
        """
        return self._processing_finished

    @processing_finished.setter
    def processing_finished(self, processing_finished):
        """Sets the processing_finished of this RunBody.


        :param processing_finished: The processing_finished of this RunBody.  # noqa: E501
        :type: datetime
        """

        self._processing_finished = processing_finished

    @property
    def processing_started(self):
        """Gets the processing_started of this RunBody.  # noqa: E501


        :return: The processing_started of this RunBody.  # noqa: E501
        :rtype: datetime
        """
        return self._processing_started

    @processing_started.setter
    def processing_started(self, processing_started):
        """Sets the processing_started of this RunBody.


        :param processing_started: The processing_started of this RunBody.  # noqa: E501
        :type: datetime
        """

        self._processing_started = processing_started

    @property
    def script_file_id(self):
        """Gets the script_file_id of this RunBody.  # noqa: E501


        :return: The script_file_id of this RunBody.  # noqa: E501
        :rtype: int
        """
        return self._script_file_id

    @script_file_id.setter
    def script_file_id(self, script_file_id):
        """Sets the script_file_id of this RunBody.


        :param script_file_id: The script_file_id of this RunBody.  # noqa: E501
        :type: int
        """

        self._script_file_id = script_file_id

    @property
    def start_interval(self):
        """Gets the start_interval of this RunBody.  # noqa: E501


        :return: The start_interval of this RunBody.  # noqa: E501
        :rtype: int
        """
        return self._start_interval

    @start_interval.setter
    def start_interval(self, start_interval):
        """Sets the start_interval of this RunBody.


        :param start_interval: The start_interval of this RunBody.  # noqa: E501
        :type: int
        """

        self._start_interval = start_interval

    @property
    def status(self):
        """Gets the status of this RunBody.  # noqa: E501


        :return: The status of this RunBody.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RunBody.


        :param status: The status of this RunBody.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def success_rate(self):
        """Gets the success_rate of this RunBody.  # noqa: E501


        :return: The success_rate of this RunBody.  # noqa: E501
        :rtype: float
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this RunBody.


        :param success_rate: The success_rate of this RunBody.  # noqa: E501
        :type: float
        """

        self._success_rate = success_rate

    @property
    def test_id(self):
        """Gets the test_id of this RunBody.  # noqa: E501


        :return: The test_id of this RunBody.  # noqa: E501
        :rtype: int
        """
        return self._test_id

    @test_id.setter
    def test_id(self, test_id):
        """Sets the test_id of this RunBody.


        :param test_id: The test_id of this RunBody.  # noqa: E501
        :type: int
        """

        self._test_id = test_id

    @property
    def test_mode(self):
        """Gets the test_mode of this RunBody.  # noqa: E501


        :return: The test_mode of this RunBody.  # noqa: E501
        :rtype: str
        """
        return self._test_mode

    @test_mode.setter
    def test_mode(self, test_mode):
        """Sets the test_mode of this RunBody.


        :param test_mode: The test_mode of this RunBody.  # noqa: E501
        :type: str
        """

        self._test_mode = test_mode

    @property
    def test_name(self):
        """Gets the test_name of this RunBody.  # noqa: E501


        :return: The test_name of this RunBody.  # noqa: E501
        :rtype: str
        """
        return self._test_name

    @test_name.setter
    def test_name(self, test_name):
        """Sets the test_name of this RunBody.


        :param test_name: The test_name of this RunBody.  # noqa: E501
        :type: str
        """

        self._test_name = test_name

    @property
    def total_cu_count(self):
        """Gets the total_cu_count of this RunBody.  # noqa: E501


        :return: The total_cu_count of this RunBody.  # noqa: E501
        :rtype: float
        """
        return self._total_cu_count

    @total_cu_count.setter
    def total_cu_count(self, total_cu_count):
        """Sets the total_cu_count of this RunBody.


        :param total_cu_count: The total_cu_count of this RunBody.  # noqa: E501
        :type: float
        """

        self._total_cu_count = total_cu_count

    @property
    def updated(self):
        """Gets the updated of this RunBody.  # noqa: E501


        :return: The updated of this RunBody.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this RunBody.


        :param updated: The updated of this RunBody.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RunBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RunBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
