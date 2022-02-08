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

class MOSGroup(object):
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
        'count': 'int',
        'created': 'datetime',
        'id': 'int',
        'name': 'str',
        'participant_count': 'int',
        'test_id': 'int',
        'updated': 'datetime'
    }

    attribute_map = {
        'count': 'count',
        'created': 'created',
        'id': 'id',
        'name': 'name',
        'participant_count': 'participant_count',
        'test_id': 'test_id',
        'updated': 'updated'
    }

    def __init__(self, count=None, created=None, id=None, name=None, participant_count=None, test_id=None, updated=None):  # noqa: E501
        """MOSGroup - a model defined in Swagger"""  # noqa: E501
        self._count = None
        self._created = None
        self._id = None
        self._name = None
        self._participant_count = None
        self._test_id = None
        self._updated = None
        self.discriminator = None
        self.count = count
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        self.name = name
        if participant_count is not None:
            self.participant_count = participant_count
        if test_id is not None:
            self.test_id = test_id
        if updated is not None:
            self.updated = updated

    @property
    def count(self):
        """Gets the count of this MOSGroup.  # noqa: E501


        :return: The count of this MOSGroup.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MOSGroup.


        :param count: The count of this MOSGroup.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def created(self):
        """Gets the created of this MOSGroup.  # noqa: E501


        :return: The created of this MOSGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this MOSGroup.


        :param created: The created of this MOSGroup.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this MOSGroup.  # noqa: E501


        :return: The id of this MOSGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MOSGroup.


        :param id: The id of this MOSGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MOSGroup.  # noqa: E501


        :return: The name of this MOSGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MOSGroup.


        :param name: The name of this MOSGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def participant_count(self):
        """Gets the participant_count of this MOSGroup.  # noqa: E501


        :return: The participant_count of this MOSGroup.  # noqa: E501
        :rtype: int
        """
        return self._participant_count

    @participant_count.setter
    def participant_count(self, participant_count):
        """Sets the participant_count of this MOSGroup.


        :param participant_count: The participant_count of this MOSGroup.  # noqa: E501
        :type: int
        """

        self._participant_count = participant_count

    @property
    def test_id(self):
        """Gets the test_id of this MOSGroup.  # noqa: E501


        :return: The test_id of this MOSGroup.  # noqa: E501
        :rtype: int
        """
        return self._test_id

    @test_id.setter
    def test_id(self, test_id):
        """Sets the test_id of this MOSGroup.


        :param test_id: The test_id of this MOSGroup.  # noqa: E501
        :type: int
        """

        self._test_id = test_id

    @property
    def updated(self):
        """Gets the updated of this MOSGroup.  # noqa: E501


        :return: The updated of this MOSGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this MOSGroup.


        :param updated: The updated of this MOSGroup.  # noqa: E501
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
        if issubclass(MOSGroup, dict):
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
        if not isinstance(other, MOSGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
