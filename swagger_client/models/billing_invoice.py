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

class BillingInvoice(object):
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
        'amount': 'float',
        'compute_units': 'float',
        'currency': 'str',
        'description': 'str',
        'hosted_invoice_url': 'str',
        'paid_at': 'int',
        'pdf': 'str',
        'period_end': 'int',
        'period_start': 'int',
        'status': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'compute_units': 'compute_units',
        'currency': 'currency',
        'description': 'description',
        'hosted_invoice_url': 'hosted_invoice_url',
        'paid_at': 'paid_at',
        'pdf': 'pdf',
        'period_end': 'period_end',
        'period_start': 'period_start',
        'status': 'status'
    }

    def __init__(self, amount=None, compute_units=None, currency=None, description=None, hosted_invoice_url=None, paid_at=None, pdf=None, period_end=None, period_start=None, status=None):  # noqa: E501
        """BillingInvoice - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._compute_units = None
        self._currency = None
        self._description = None
        self._hosted_invoice_url = None
        self._paid_at = None
        self._pdf = None
        self._period_end = None
        self._period_start = None
        self._status = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if compute_units is not None:
            self.compute_units = compute_units
        if currency is not None:
            self.currency = currency
        if description is not None:
            self.description = description
        if hosted_invoice_url is not None:
            self.hosted_invoice_url = hosted_invoice_url
        if paid_at is not None:
            self.paid_at = paid_at
        if pdf is not None:
            self.pdf = pdf
        if period_end is not None:
            self.period_end = period_end
        if period_start is not None:
            self.period_start = period_start
        if status is not None:
            self.status = status

    @property
    def amount(self):
        """Gets the amount of this BillingInvoice.  # noqa: E501


        :return: The amount of this BillingInvoice.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BillingInvoice.


        :param amount: The amount of this BillingInvoice.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def compute_units(self):
        """Gets the compute_units of this BillingInvoice.  # noqa: E501


        :return: The compute_units of this BillingInvoice.  # noqa: E501
        :rtype: float
        """
        return self._compute_units

    @compute_units.setter
    def compute_units(self, compute_units):
        """Sets the compute_units of this BillingInvoice.


        :param compute_units: The compute_units of this BillingInvoice.  # noqa: E501
        :type: float
        """

        self._compute_units = compute_units

    @property
    def currency(self):
        """Gets the currency of this BillingInvoice.  # noqa: E501


        :return: The currency of this BillingInvoice.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this BillingInvoice.


        :param currency: The currency of this BillingInvoice.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def description(self):
        """Gets the description of this BillingInvoice.  # noqa: E501


        :return: The description of this BillingInvoice.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BillingInvoice.


        :param description: The description of this BillingInvoice.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hosted_invoice_url(self):
        """Gets the hosted_invoice_url of this BillingInvoice.  # noqa: E501


        :return: The hosted_invoice_url of this BillingInvoice.  # noqa: E501
        :rtype: str
        """
        return self._hosted_invoice_url

    @hosted_invoice_url.setter
    def hosted_invoice_url(self, hosted_invoice_url):
        """Sets the hosted_invoice_url of this BillingInvoice.


        :param hosted_invoice_url: The hosted_invoice_url of this BillingInvoice.  # noqa: E501
        :type: str
        """

        self._hosted_invoice_url = hosted_invoice_url

    @property
    def paid_at(self):
        """Gets the paid_at of this BillingInvoice.  # noqa: E501


        :return: The paid_at of this BillingInvoice.  # noqa: E501
        :rtype: int
        """
        return self._paid_at

    @paid_at.setter
    def paid_at(self, paid_at):
        """Sets the paid_at of this BillingInvoice.


        :param paid_at: The paid_at of this BillingInvoice.  # noqa: E501
        :type: int
        """

        self._paid_at = paid_at

    @property
    def pdf(self):
        """Gets the pdf of this BillingInvoice.  # noqa: E501


        :return: The pdf of this BillingInvoice.  # noqa: E501
        :rtype: str
        """
        return self._pdf

    @pdf.setter
    def pdf(self, pdf):
        """Sets the pdf of this BillingInvoice.


        :param pdf: The pdf of this BillingInvoice.  # noqa: E501
        :type: str
        """

        self._pdf = pdf

    @property
    def period_end(self):
        """Gets the period_end of this BillingInvoice.  # noqa: E501


        :return: The period_end of this BillingInvoice.  # noqa: E501
        :rtype: int
        """
        return self._period_end

    @period_end.setter
    def period_end(self, period_end):
        """Sets the period_end of this BillingInvoice.


        :param period_end: The period_end of this BillingInvoice.  # noqa: E501
        :type: int
        """

        self._period_end = period_end

    @property
    def period_start(self):
        """Gets the period_start of this BillingInvoice.  # noqa: E501


        :return: The period_start of this BillingInvoice.  # noqa: E501
        :rtype: int
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start):
        """Sets the period_start of this BillingInvoice.


        :param period_start: The period_start of this BillingInvoice.  # noqa: E501
        :type: int
        """

        self._period_start = period_start

    @property
    def status(self):
        """Gets the status of this BillingInvoice.  # noqa: E501


        :return: The status of this BillingInvoice.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BillingInvoice.


        :param status: The status of this BillingInvoice.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(BillingInvoice, dict):
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
        if not isinstance(other, BillingInvoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
