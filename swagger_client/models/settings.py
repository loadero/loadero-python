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

class Settings(object):
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
        'max_monthly_cu': 'int',
        'max_participant_cu': 'str',
        'max_test_cu': 'int',
        'max_test_duration': 'str',
        'mos_enabled': 'bool'
    }

    attribute_map = {
        'max_monthly_cu': 'max_monthly_cu',
        'max_participant_cu': 'max_participant_cu',
        'max_test_cu': 'max_test_cu',
        'max_test_duration': 'max_test_duration',
        'mos_enabled': 'mos_enabled'
    }

    def __init__(self, max_monthly_cu=None, max_participant_cu=None, max_test_cu=None, max_test_duration=None, mos_enabled=None):  # noqa: E501
        """Settings - a model defined in Swagger"""  # noqa: E501
        self._max_monthly_cu = None
        self._max_participant_cu = None
        self._max_test_cu = None
        self._max_test_duration = None
        self._mos_enabled = None
        self.discriminator = None
        if max_monthly_cu is not None:
            self.max_monthly_cu = max_monthly_cu
        if max_participant_cu is not None:
            self.max_participant_cu = max_participant_cu
        if max_test_cu is not None:
            self.max_test_cu = max_test_cu
        if max_test_duration is not None:
            self.max_test_duration = max_test_duration
        if mos_enabled is not None:
            self.mos_enabled = mos_enabled

    @property
    def max_monthly_cu(self):
        """Gets the max_monthly_cu of this Settings.  # noqa: E501


        :return: The max_monthly_cu of this Settings.  # noqa: E501
        :rtype: int
        """
        return self._max_monthly_cu

    @max_monthly_cu.setter
    def max_monthly_cu(self, max_monthly_cu):
        """Sets the max_monthly_cu of this Settings.


        :param max_monthly_cu: The max_monthly_cu of this Settings.  # noqa: E501
        :type: int
        """

        self._max_monthly_cu = max_monthly_cu

    @property
    def max_participant_cu(self):
        """Gets the max_participant_cu of this Settings.  # noqa: E501


        :return: The max_participant_cu of this Settings.  # noqa: E501
        :rtype: str
        """
        return self._max_participant_cu

    @max_participant_cu.setter
    def max_participant_cu(self, max_participant_cu):
        """Sets the max_participant_cu of this Settings.


        :param max_participant_cu: The max_participant_cu of this Settings.  # noqa: E501
        :type: str
        """

        self._max_participant_cu = max_participant_cu

    @property
    def max_test_cu(self):
        """Gets the max_test_cu of this Settings.  # noqa: E501


        :return: The max_test_cu of this Settings.  # noqa: E501
        :rtype: int
        """
        return self._max_test_cu

    @max_test_cu.setter
    def max_test_cu(self, max_test_cu):
        """Sets the max_test_cu of this Settings.


        :param max_test_cu: The max_test_cu of this Settings.  # noqa: E501
        :type: int
        """

        self._max_test_cu = max_test_cu

    @property
    def max_test_duration(self):
        """Gets the max_test_duration of this Settings.  # noqa: E501


        :return: The max_test_duration of this Settings.  # noqa: E501
        :rtype: str
        """
        return self._max_test_duration

    @max_test_duration.setter
    def max_test_duration(self, max_test_duration):
        """Sets the max_test_duration of this Settings.


        :param max_test_duration: The max_test_duration of this Settings.  # noqa: E501
        :type: str
        """

        self._max_test_duration = max_test_duration

    @property
    def mos_enabled(self):
        """Gets the mos_enabled of this Settings.  # noqa: E501


        :return: The mos_enabled of this Settings.  # noqa: E501
        :rtype: bool
        """
        return self._mos_enabled

    @mos_enabled.setter
    def mos_enabled(self, mos_enabled):
        """Sets the mos_enabled of this Settings.


        :param mos_enabled: The mos_enabled of this Settings.  # noqa: E501
        :type: bool
        """

        self._mos_enabled = mos_enabled

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
        if issubclass(Settings, dict):
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
        if not isinstance(other, Settings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
