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

class AWSStatus(object):
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
        'classificator': 'ClassificatorType',
        'description': 'str',
        'disabled': 'bool',
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'classificator': 'classificator',
        'description': 'description',
        'disabled': 'disabled',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, classificator=None, description=None, disabled=None, name=None, value=None):  # noqa: E501
        """AWSStatus - a model defined in Swagger"""  # noqa: E501
        self._classificator = None
        self._description = None
        self._disabled = None
        self._name = None
        self._value = None
        self.discriminator = None
        if classificator is not None:
            self.classificator = classificator
        if description is not None:
            self.description = description
        if disabled is not None:
            self.disabled = disabled
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def classificator(self):
        """Gets the classificator of this AWSStatus.  # noqa: E501


        :return: The classificator of this AWSStatus.  # noqa: E501
        :rtype: ClassificatorType
        """
        return self._classificator

    @classificator.setter
    def classificator(self, classificator):
        """Sets the classificator of this AWSStatus.


        :param classificator: The classificator of this AWSStatus.  # noqa: E501
        :type: ClassificatorType
        """

        self._classificator = classificator

    @property
    def description(self):
        """Gets the description of this AWSStatus.  # noqa: E501


        :return: The description of this AWSStatus.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AWSStatus.


        :param description: The description of this AWSStatus.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disabled(self):
        """Gets the disabled of this AWSStatus.  # noqa: E501


        :return: The disabled of this AWSStatus.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this AWSStatus.


        :param disabled: The disabled of this AWSStatus.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def name(self):
        """Gets the name of this AWSStatus.  # noqa: E501


        :return: The name of this AWSStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AWSStatus.


        :param name: The name of this AWSStatus.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this AWSStatus.  # noqa: E501


        :return: The value of this AWSStatus.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AWSStatus.


        :param value: The value of this AWSStatus.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(AWSStatus, dict):
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
        if not isinstance(other, AWSStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
