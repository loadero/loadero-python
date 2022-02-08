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

class PluginConfigRootfs(object):
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
        'diff_ids': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'diff_ids': 'diff_ids',
        'type': 'type'
    }

    def __init__(self, diff_ids=None, type=None):  # noqa: E501
        """PluginConfigRootfs - a model defined in Swagger"""  # noqa: E501
        self._diff_ids = None
        self._type = None
        self.discriminator = None
        if diff_ids is not None:
            self.diff_ids = diff_ids
        if type is not None:
            self.type = type

    @property
    def diff_ids(self):
        """Gets the diff_ids of this PluginConfigRootfs.  # noqa: E501

        diff ids  # noqa: E501

        :return: The diff_ids of this PluginConfigRootfs.  # noqa: E501
        :rtype: list[str]
        """
        return self._diff_ids

    @diff_ids.setter
    def diff_ids(self, diff_ids):
        """Sets the diff_ids of this PluginConfigRootfs.

        diff ids  # noqa: E501

        :param diff_ids: The diff_ids of this PluginConfigRootfs.  # noqa: E501
        :type: list[str]
        """

        self._diff_ids = diff_ids

    @property
    def type(self):
        """Gets the type of this PluginConfigRootfs.  # noqa: E501

        type  # noqa: E501

        :return: The type of this PluginConfigRootfs.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PluginConfigRootfs.

        type  # noqa: E501

        :param type: The type of this PluginConfigRootfs.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(PluginConfigRootfs, dict):
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
        if not isinstance(other, PluginConfigRootfs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
