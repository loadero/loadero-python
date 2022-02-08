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

class NewPassword(object):
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
        'confirm_password': 'str',
        'password': 'str'
    }

    attribute_map = {
        'confirm_password': 'confirm_password',
        'password': 'password'
    }

    def __init__(self, confirm_password=None, password=None):  # noqa: E501
        """NewPassword - a model defined in Swagger"""  # noqa: E501
        self._confirm_password = None
        self._password = None
        self.discriminator = None
        self.confirm_password = confirm_password
        self.password = password

    @property
    def confirm_password(self):
        """Gets the confirm_password of this NewPassword.  # noqa: E501


        :return: The confirm_password of this NewPassword.  # noqa: E501
        :rtype: str
        """
        return self._confirm_password

    @confirm_password.setter
    def confirm_password(self, confirm_password):
        """Sets the confirm_password of this NewPassword.


        :param confirm_password: The confirm_password of this NewPassword.  # noqa: E501
        :type: str
        """
        if confirm_password is None:
            raise ValueError("Invalid value for `confirm_password`, must not be `None`")  # noqa: E501

        self._confirm_password = confirm_password

    @property
    def password(self):
        """Gets the password of this NewPassword.  # noqa: E501


        :return: The password of this NewPassword.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this NewPassword.


        :param password: The password of this NewPassword.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

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
        if issubclass(NewPassword, dict):
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
        if not isinstance(other, NewPassword):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
