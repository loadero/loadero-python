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

class Test(object):
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
        'deleted': 'bool',
        'group_count': 'int',
        'id': 'int',
        'increment_strategy': 'str',
        'mode': 'str',
        'name': 'str',
        'participant_count': 'int',
        'participant_timeout': 'int',
        'project_id': 'int',
        'script_file_id': 'int',
        'start_interval': 'int',
        'updated': 'datetime'
    }

    attribute_map = {
        'created': 'created',
        'deleted': 'deleted',
        'group_count': 'group_count',
        'id': 'id',
        'increment_strategy': 'increment_strategy',
        'mode': 'mode',
        'name': 'name',
        'participant_count': 'participant_count',
        'participant_timeout': 'participant_timeout',
        'project_id': 'project_id',
        'script_file_id': 'script_file_id',
        'start_interval': 'start_interval',
        'updated': 'updated'
    }

    def __init__(self, created=None, deleted=None, group_count=None, id=None, increment_strategy=None, mode=None, name=None, participant_count=None, participant_timeout=None, project_id=None, script_file_id=None, start_interval=None, updated=None):  # noqa: E501
        """Test - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._deleted = None
        self._group_count = None
        self._id = None
        self._increment_strategy = None
        self._mode = None
        self._name = None
        self._participant_count = None
        self._participant_timeout = None
        self._project_id = None
        self._script_file_id = None
        self._start_interval = None
        self._updated = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if deleted is not None:
            self.deleted = deleted
        if group_count is not None:
            self.group_count = group_count
        if id is not None:
            self.id = id
        self.increment_strategy = increment_strategy
        self.mode = mode
        self.name = name
        if participant_count is not None:
            self.participant_count = participant_count
        self.participant_timeout = participant_timeout
        if project_id is not None:
            self.project_id = project_id
        if script_file_id is not None:
            self.script_file_id = script_file_id
        self.start_interval = start_interval
        if updated is not None:
            self.updated = updated

    @property
    def created(self):
        """Gets the created of this Test.  # noqa: E501


        :return: The created of this Test.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Test.


        :param created: The created of this Test.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def deleted(self):
        """Gets the deleted of this Test.  # noqa: E501


        :return: The deleted of this Test.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Test.


        :param deleted: The deleted of this Test.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def group_count(self):
        """Gets the group_count of this Test.  # noqa: E501


        :return: The group_count of this Test.  # noqa: E501
        :rtype: int
        """
        return self._group_count

    @group_count.setter
    def group_count(self, group_count):
        """Sets the group_count of this Test.


        :param group_count: The group_count of this Test.  # noqa: E501
        :type: int
        """

        self._group_count = group_count

    @property
    def id(self):
        """Gets the id of this Test.  # noqa: E501


        :return: The id of this Test.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Test.


        :param id: The id of this Test.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def increment_strategy(self):
        """Gets the increment_strategy of this Test.  # noqa: E501


        :return: The increment_strategy of this Test.  # noqa: E501
        :rtype: str
        """
        return self._increment_strategy

    @increment_strategy.setter
    def increment_strategy(self, increment_strategy):
        """Sets the increment_strategy of this Test.


        :param increment_strategy: The increment_strategy of this Test.  # noqa: E501
        :type: str
        """
        if increment_strategy is None:
            raise ValueError("Invalid value for `increment_strategy`, must not be `None`")  # noqa: E501

        self._increment_strategy = increment_strategy

    @property
    def mode(self):
        """Gets the mode of this Test.  # noqa: E501


        :return: The mode of this Test.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Test.


        :param mode: The mode of this Test.  # noqa: E501
        :type: str
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501

        self._mode = mode

    @property
    def name(self):
        """Gets the name of this Test.  # noqa: E501


        :return: The name of this Test.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Test.


        :param name: The name of this Test.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def participant_count(self):
        """Gets the participant_count of this Test.  # noqa: E501


        :return: The participant_count of this Test.  # noqa: E501
        :rtype: int
        """
        return self._participant_count

    @participant_count.setter
    def participant_count(self, participant_count):
        """Sets the participant_count of this Test.


        :param participant_count: The participant_count of this Test.  # noqa: E501
        :type: int
        """

        self._participant_count = participant_count

    @property
    def participant_timeout(self):
        """Gets the participant_timeout of this Test.  # noqa: E501


        :return: The participant_timeout of this Test.  # noqa: E501
        :rtype: int
        """
        return self._participant_timeout

    @participant_timeout.setter
    def participant_timeout(self, participant_timeout):
        """Sets the participant_timeout of this Test.


        :param participant_timeout: The participant_timeout of this Test.  # noqa: E501
        :type: int
        """
        if participant_timeout is None:
            raise ValueError("Invalid value for `participant_timeout`, must not be `None`")  # noqa: E501

        self._participant_timeout = participant_timeout

    @property
    def project_id(self):
        """Gets the project_id of this Test.  # noqa: E501


        :return: The project_id of this Test.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Test.


        :param project_id: The project_id of this Test.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def script_file_id(self):
        """Gets the script_file_id of this Test.  # noqa: E501


        :return: The script_file_id of this Test.  # noqa: E501
        :rtype: int
        """
        return self._script_file_id

    @script_file_id.setter
    def script_file_id(self, script_file_id):
        """Sets the script_file_id of this Test.


        :param script_file_id: The script_file_id of this Test.  # noqa: E501
        :type: int
        """

        self._script_file_id = script_file_id

    @property
    def start_interval(self):
        """Gets the start_interval of this Test.  # noqa: E501


        :return: The start_interval of this Test.  # noqa: E501
        :rtype: int
        """
        return self._start_interval

    @start_interval.setter
    def start_interval(self, start_interval):
        """Sets the start_interval of this Test.


        :param start_interval: The start_interval of this Test.  # noqa: E501
        :type: int
        """
        if start_interval is None:
            raise ValueError("Invalid value for `start_interval`, must not be `None`")  # noqa: E501

        self._start_interval = start_interval

    @property
    def updated(self):
        """Gets the updated of this Test.  # noqa: E501


        :return: The updated of this Test.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Test.


        :param updated: The updated of this Test.  # noqa: E501
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
        if issubclass(Test, dict):
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
        if not isinstance(other, Test):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
