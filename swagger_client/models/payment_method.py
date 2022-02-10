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

class PaymentMethod(object):
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
        'brand': 'str',
        'cardholder_name': 'str',
        'exp_month': 'int',
        'exp_year': 'int',
        'id': 'str',
        'is_default': 'bool',
        'last_4': 'str'
    }

    attribute_map = {
        'brand': 'brand',
        'cardholder_name': 'cardholder_name',
        'exp_month': 'exp_month',
        'exp_year': 'exp_year',
        'id': 'id',
        'is_default': 'is_default',
        'last_4': 'last_4'
    }

    def __init__(self, brand=None, cardholder_name=None, exp_month=None, exp_year=None, id=None, is_default=None, last_4=None):  # noqa: E501
        """PaymentMethod - a model defined in Swagger"""  # noqa: E501
        self._brand = None
        self._cardholder_name = None
        self._exp_month = None
        self._exp_year = None
        self._id = None
        self._is_default = None
        self._last_4 = None
        self.discriminator = None
        if brand is not None:
            self.brand = brand
        if cardholder_name is not None:
            self.cardholder_name = cardholder_name
        if exp_month is not None:
            self.exp_month = exp_month
        if exp_year is not None:
            self.exp_year = exp_year
        if id is not None:
            self.id = id
        if is_default is not None:
            self.is_default = is_default
        if last_4 is not None:
            self.last_4 = last_4

    @property
    def brand(self):
        """Gets the brand of this PaymentMethod.  # noqa: E501


        :return: The brand of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PaymentMethod.


        :param brand: The brand of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def cardholder_name(self):
        """Gets the cardholder_name of this PaymentMethod.  # noqa: E501


        :return: The cardholder_name of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        """Sets the cardholder_name of this PaymentMethod.


        :param cardholder_name: The cardholder_name of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._cardholder_name = cardholder_name

    @property
    def exp_month(self):
        """Gets the exp_month of this PaymentMethod.  # noqa: E501


        :return: The exp_month of this PaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._exp_month

    @exp_month.setter
    def exp_month(self, exp_month):
        """Sets the exp_month of this PaymentMethod.


        :param exp_month: The exp_month of this PaymentMethod.  # noqa: E501
        :type: int
        """

        self._exp_month = exp_month

    @property
    def exp_year(self):
        """Gets the exp_year of this PaymentMethod.  # noqa: E501


        :return: The exp_year of this PaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._exp_year

    @exp_year.setter
    def exp_year(self, exp_year):
        """Sets the exp_year of this PaymentMethod.


        :param exp_year: The exp_year of this PaymentMethod.  # noqa: E501
        :type: int
        """

        self._exp_year = exp_year

    @property
    def id(self):
        """Gets the id of this PaymentMethod.  # noqa: E501


        :return: The id of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentMethod.


        :param id: The id of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_default(self):
        """Gets the is_default of this PaymentMethod.  # noqa: E501


        :return: The is_default of this PaymentMethod.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this PaymentMethod.


        :param is_default: The is_default of this PaymentMethod.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def last_4(self):
        """Gets the last_4 of this PaymentMethod.  # noqa: E501


        :return: The last_4 of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._last_4

    @last_4.setter
    def last_4(self, last_4):
        """Sets the last_4 of this PaymentMethod.


        :param last_4: The last_4 of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._last_4 = last_4

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
        if issubclass(PaymentMethod, dict):
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
        if not isinstance(other, PaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
