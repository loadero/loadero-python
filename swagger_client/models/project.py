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

class Project(object):
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
        'account_role': 'str',
        'aws_info_id': 'int',
        'created': 'datetime',
        'id': 'int',
        'language': 'str',
        'member_count': 'int',
        'name': 'str',
        'subscription_id': 'int',
        'trial_expired': 'bool',
        'updated': 'datetime'
    }

    attribute_map = {
        'account_role': 'account_role',
        'aws_info_id': 'aws_info_id',
        'created': 'created',
        'id': 'id',
        'language': 'language',
        'member_count': 'member_count',
        'name': 'name',
        'subscription_id': 'subscription_id',
        'trial_expired': 'trial_expired',
        'updated': 'updated'
    }

    def __init__(self, account_role=None, aws_info_id=None, created=None, id=None, language=None, member_count=None, name=None, subscription_id=None, trial_expired=None, updated=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501
        self._account_role = None
        self._aws_info_id = None
        self._created = None
        self._id = None
        self._language = None
        self._member_count = None
        self._name = None
        self._subscription_id = None
        self._trial_expired = None
        self._updated = None
        self.discriminator = None
        if account_role is not None:
            self.account_role = account_role
        if aws_info_id is not None:
            self.aws_info_id = aws_info_id
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        self.language = language
        if member_count is not None:
            self.member_count = member_count
        self.name = name
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if trial_expired is not None:
            self.trial_expired = trial_expired
        if updated is not None:
            self.updated = updated

    @property
    def account_role(self):
        """Gets the account_role of this Project.  # noqa: E501


        :return: The account_role of this Project.  # noqa: E501
        :rtype: str
        """
        return self._account_role

    @account_role.setter
    def account_role(self, account_role):
        """Sets the account_role of this Project.


        :param account_role: The account_role of this Project.  # noqa: E501
        :type: str
        """

        self._account_role = account_role

    @property
    def aws_info_id(self):
        """Gets the aws_info_id of this Project.  # noqa: E501


        :return: The aws_info_id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._aws_info_id

    @aws_info_id.setter
    def aws_info_id(self, aws_info_id):
        """Sets the aws_info_id of this Project.


        :param aws_info_id: The aws_info_id of this Project.  # noqa: E501
        :type: int
        """

        self._aws_info_id = aws_info_id

    @property
    def created(self):
        """Gets the created of this Project.  # noqa: E501


        :return: The created of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Project.


        :param created: The created of this Project.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501


        :return: The id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.


        :param id: The id of this Project.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def language(self):
        """Gets the language of this Project.  # noqa: E501


        :return: The language of this Project.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Project.


        :param language: The language of this Project.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def member_count(self):
        """Gets the member_count of this Project.  # noqa: E501


        :return: The member_count of this Project.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this Project.


        :param member_count: The member_count of this Project.  # noqa: E501
        :type: int
        """

        self._member_count = member_count

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501


        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.


        :param name: The name of this Project.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def subscription_id(self):
        """Gets the subscription_id of this Project.  # noqa: E501


        :return: The subscription_id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this Project.


        :param subscription_id: The subscription_id of this Project.  # noqa: E501
        :type: int
        """

        self._subscription_id = subscription_id

    @property
    def trial_expired(self):
        """Gets the trial_expired of this Project.  # noqa: E501


        :return: The trial_expired of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._trial_expired

    @trial_expired.setter
    def trial_expired(self, trial_expired):
        """Sets the trial_expired of this Project.


        :param trial_expired: The trial_expired of this Project.  # noqa: E501
        :type: bool
        """

        self._trial_expired = trial_expired

    @property
    def updated(self):
        """Gets the updated of this Project.  # noqa: E501


        :return: The updated of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Project.


        :param updated: The updated of this Project.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

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
        if issubclass(Project, dict):
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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
