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

class InlineResponse2003(object):
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
        'asserts': 'list[AssertOverview]',
        'metrics': 'Metrics'
    }

    attribute_map = {
        'asserts': 'asserts',
        'metrics': 'metrics'
    }

    def __init__(self, asserts=None, metrics=None):  # noqa: E501
        """InlineResponse2003 - a model defined in Swagger"""  # noqa: E501
        self._asserts = None
        self._metrics = None
        self.discriminator = None
        if asserts is not None:
            self.asserts = asserts
        if metrics is not None:
            self.metrics = metrics

    @property
    def asserts(self):
        """Gets the asserts of this InlineResponse2003.  # noqa: E501


        :return: The asserts of this InlineResponse2003.  # noqa: E501
        :rtype: list[AssertOverview]
        """
        return self._asserts

    @asserts.setter
    def asserts(self, asserts):
        """Sets the asserts of this InlineResponse2003.


        :param asserts: The asserts of this InlineResponse2003.  # noqa: E501
        :type: list[AssertOverview]
        """

        self._asserts = asserts

    @property
    def metrics(self):
        """Gets the metrics of this InlineResponse2003.  # noqa: E501


        :return: The metrics of this InlineResponse2003.  # noqa: E501
        :rtype: Metrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this InlineResponse2003.


        :param metrics: The metrics of this InlineResponse2003.  # noqa: E501
        :type: Metrics
        """

        self._metrics = metrics

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
        if issubclass(InlineResponse2003, dict):
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
        if not isinstance(other, InlineResponse2003):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
