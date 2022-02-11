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

class ImageDeleteResponseItem(object):
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
        'deleted': 'str',
        'untagged': 'str'
    }

    attribute_map = {
        'deleted': 'Deleted',
        'untagged': 'Untagged'
    }

    def __init__(self, deleted=None, untagged=None):  # noqa: E501
        """ImageDeleteResponseItem - a model defined in Swagger"""  # noqa: E501
        self._deleted = None
        self._untagged = None
        self.discriminator = None
        if deleted is not None:
            self.deleted = deleted
        if untagged is not None:
            self.untagged = untagged

    @property
    def deleted(self):
        """Gets the deleted of this ImageDeleteResponseItem.  # noqa: E501

        The image ID of an image that was deleted  # noqa: E501

        :return: The deleted of this ImageDeleteResponseItem.  # noqa: E501
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ImageDeleteResponseItem.

        The image ID of an image that was deleted  # noqa: E501

        :param deleted: The deleted of this ImageDeleteResponseItem.  # noqa: E501
        :type: str
        """

        self._deleted = deleted

    @property
    def untagged(self):
        """Gets the untagged of this ImageDeleteResponseItem.  # noqa: E501

        The image ID of an image that was untagged  # noqa: E501

        :return: The untagged of this ImageDeleteResponseItem.  # noqa: E501
        :rtype: str
        """
        return self._untagged

    @untagged.setter
    def untagged(self, untagged):
        """Sets the untagged of this ImageDeleteResponseItem.

        The image ID of an image that was untagged  # noqa: E501

        :param untagged: The untagged of this ImageDeleteResponseItem.  # noqa: E501
        :type: str
        """

        self._untagged = untagged

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
        if issubclass(ImageDeleteResponseItem, dict):
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
        if not isinstance(other, ImageDeleteResponseItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
