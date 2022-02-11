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

class UpdateUserBody(object):
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
        'confirm_new_password': 'str',
        'new_password': 'str',
        'password': 'str',
        'reset_password_token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'confirm_new_password': 'confirm_new_password',
        'new_password': 'new_password',
        'password': 'password',
        'reset_password_token': 'reset_password_token',
        'username': 'username'
    }

    def __init__(self, confirm_new_password=None, new_password=None, password=None, reset_password_token=None, username=None):  # noqa: E501
        """UpdateUserBody - a model defined in Swagger"""  # noqa: E501
        self._confirm_new_password = None
        self._new_password = None
        self._password = None
        self._reset_password_token = None
        self._username = None
        self.discriminator = None
        if confirm_new_password is not None:
            self.confirm_new_password = confirm_new_password
        if new_password is not None:
            self.new_password = new_password
        if password is not None:
            self.password = password
        if reset_password_token is not None:
            self.reset_password_token = reset_password_token
        if username is not None:
            self.username = username

    @property
    def confirm_new_password(self):
        """Gets the confirm_new_password of this UpdateUserBody.  # noqa: E501


        :return: The confirm_new_password of this UpdateUserBody.  # noqa: E501
        :rtype: str
        """
        return self._confirm_new_password

    @confirm_new_password.setter
    def confirm_new_password(self, confirm_new_password):
        """Sets the confirm_new_password of this UpdateUserBody.


        :param confirm_new_password: The confirm_new_password of this UpdateUserBody.  # noqa: E501
        :type: str
        """

        self._confirm_new_password = confirm_new_password

    @property
    def new_password(self):
        """Gets the new_password of this UpdateUserBody.  # noqa: E501


        :return: The new_password of this UpdateUserBody.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this UpdateUserBody.


        :param new_password: The new_password of this UpdateUserBody.  # noqa: E501
        :type: str
        """

        self._new_password = new_password

    @property
    def password(self):
        """Gets the password of this UpdateUserBody.  # noqa: E501


        :return: The password of this UpdateUserBody.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateUserBody.


        :param password: The password of this UpdateUserBody.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def reset_password_token(self):
        """Gets the reset_password_token of this UpdateUserBody.  # noqa: E501


        :return: The reset_password_token of this UpdateUserBody.  # noqa: E501
        :rtype: str
        """
        return self._reset_password_token

    @reset_password_token.setter
    def reset_password_token(self, reset_password_token):
        """Sets the reset_password_token of this UpdateUserBody.


        :param reset_password_token: The reset_password_token of this UpdateUserBody.  # noqa: E501
        :type: str
        """

        self._reset_password_token = reset_password_token

    @property
    def username(self):
        """Gets the username of this UpdateUserBody.  # noqa: E501


        :return: The username of this UpdateUserBody.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UpdateUserBody.


        :param username: The username of this UpdateUserBody.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(UpdateUserBody, dict):
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
        if not isinstance(other, UpdateUserBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
