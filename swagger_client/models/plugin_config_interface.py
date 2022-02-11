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

class PluginConfigInterface(object):
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
        'protocol_scheme': 'str',
        'socket': 'str',
        'types': 'list[PluginInterfaceType]'
    }

    attribute_map = {
        'protocol_scheme': 'ProtocolScheme',
        'socket': 'Socket',
        'types': 'Types'
    }

    def __init__(self, protocol_scheme=None, socket=None, types=None):  # noqa: E501
        """PluginConfigInterface - a model defined in Swagger"""  # noqa: E501
        self._protocol_scheme = None
        self._socket = None
        self._types = None
        self.discriminator = None
        if protocol_scheme is not None:
            self.protocol_scheme = protocol_scheme
        self.socket = socket
        self.types = types

    @property
    def protocol_scheme(self):
        """Gets the protocol_scheme of this PluginConfigInterface.  # noqa: E501

        Protocol to use for clients connecting to the plugin.  # noqa: E501

        :return: The protocol_scheme of this PluginConfigInterface.  # noqa: E501
        :rtype: str
        """
        return self._protocol_scheme

    @protocol_scheme.setter
    def protocol_scheme(self, protocol_scheme):
        """Sets the protocol_scheme of this PluginConfigInterface.

        Protocol to use for clients connecting to the plugin.  # noqa: E501

        :param protocol_scheme: The protocol_scheme of this PluginConfigInterface.  # noqa: E501
        :type: str
        """

        self._protocol_scheme = protocol_scheme

    @property
    def socket(self):
        """Gets the socket of this PluginConfigInterface.  # noqa: E501

        socket  # noqa: E501

        :return: The socket of this PluginConfigInterface.  # noqa: E501
        :rtype: str
        """
        return self._socket

    @socket.setter
    def socket(self, socket):
        """Sets the socket of this PluginConfigInterface.

        socket  # noqa: E501

        :param socket: The socket of this PluginConfigInterface.  # noqa: E501
        :type: str
        """
        if socket is None:
            raise ValueError("Invalid value for `socket`, must not be `None`")  # noqa: E501

        self._socket = socket

    @property
    def types(self):
        """Gets the types of this PluginConfigInterface.  # noqa: E501

        types  # noqa: E501

        :return: The types of this PluginConfigInterface.  # noqa: E501
        :rtype: list[PluginInterfaceType]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this PluginConfigInterface.

        types  # noqa: E501

        :param types: The types of this PluginConfigInterface.  # noqa: E501
        :type: list[PluginInterfaceType]
        """
        if types is None:
            raise ValueError("Invalid value for `types`, must not be `None`")  # noqa: E501

        self._types = types

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
        if issubclass(PluginConfigInterface, dict):
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
        if not isinstance(other, PluginConfigInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other