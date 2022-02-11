# coding: utf-8

"""
    Loadero Controller

    This application serves main Loadero's endpoints that can be used to manipulate test data and other services  # noqa: E501

    OpenAPI spec version: v0.38.0
    Contact: support@loadero.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RunAssertPrecondition(object):
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
        'expected': 'str',
        'id': 'int',
        'operator': 'str',
        '_property': 'str',
        'run_assert_id': 'int',
        'updated': 'datetime'
    }

    attribute_map = {
        'created': 'created',
        'expected': 'expected',
        'id': 'id',
        'operator': 'operator',
        '_property': 'property',
        'run_assert_id': 'run_assert_id',
        'updated': 'updated'
    }

    def __init__(self, created=None, expected=None, id=None, operator=None, _property=None, run_assert_id=None, updated=None):  # noqa: E501
        """RunAssertPrecondition - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._expected = None
        self._id = None
        self._operator = None
        self.__property = None
        self._run_assert_id = None
        self._updated = None
        self.discriminator = None
        if created is not None:
            self.created = created
        self.expected = expected
        if id is not None:
            self.id = id
        self.operator = operator
        self._property = _property
        if run_assert_id is not None:
            self.run_assert_id = run_assert_id
        if updated is not None:
            self.updated = updated

    @property
    def created(self):
        """Gets the created of this RunAssertPrecondition.  # noqa: E501


        :return: The created of this RunAssertPrecondition.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this RunAssertPrecondition.


        :param created: The created of this RunAssertPrecondition.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def expected(self):
        """Gets the expected of this RunAssertPrecondition.  # noqa: E501


        :return: The expected of this RunAssertPrecondition.  # noqa: E501
        :rtype: str
        """
        return self._expected

    @expected.setter
    def expected(self, expected):
        """Sets the expected of this RunAssertPrecondition.


        :param expected: The expected of this RunAssertPrecondition.  # noqa: E501
        :type: str
        """
        if expected is None:
            raise ValueError("Invalid value for `expected`, must not be `None`")  # noqa: E501

        self._expected = expected

    @property
    def id(self):
        """Gets the id of this RunAssertPrecondition.  # noqa: E501


        :return: The id of this RunAssertPrecondition.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RunAssertPrecondition.


        :param id: The id of this RunAssertPrecondition.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def operator(self):
        """Gets the operator of this RunAssertPrecondition.  # noqa: E501


        :return: The operator of this RunAssertPrecondition.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this RunAssertPrecondition.


        :param operator: The operator of this RunAssertPrecondition.  # noqa: E501
        :type: str
        """
        if operator is None:
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def _property(self):
        """Gets the _property of this RunAssertPrecondition.  # noqa: E501


        :return: The _property of this RunAssertPrecondition.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this RunAssertPrecondition.


        :param _property: The _property of this RunAssertPrecondition.  # noqa: E501
        :type: str
        """
        if _property is None:
            raise ValueError("Invalid value for `_property`, must not be `None`")  # noqa: E501

        self.__property = _property

    @property
    def run_assert_id(self):
        """Gets the run_assert_id of this RunAssertPrecondition.  # noqa: E501


        :return: The run_assert_id of this RunAssertPrecondition.  # noqa: E501
        :rtype: int
        """
        return self._run_assert_id

    @run_assert_id.setter
    def run_assert_id(self, run_assert_id):
        """Sets the run_assert_id of this RunAssertPrecondition.


        :param run_assert_id: The run_assert_id of this RunAssertPrecondition.  # noqa: E501
        :type: int
        """

        self._run_assert_id = run_assert_id

    @property
    def updated(self):
        """Gets the updated of this RunAssertPrecondition.  # noqa: E501


        :return: The updated of this RunAssertPrecondition.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this RunAssertPrecondition.


        :param updated: The updated of this RunAssertPrecondition.  # noqa: E501
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
        if issubclass(RunAssertPrecondition, dict):
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
        if not isinstance(other, RunAssertPrecondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
