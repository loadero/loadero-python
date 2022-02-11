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

class AwsInfoReponse(object):
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
        'account_id': 'str',
        'artifact_bucket': 'str',
        'client_id': 'str',
        'created': 'datetime',
        'id': 'int',
        'linked_projects': 'list[SimpleProject]',
        'log_bucket': 'str',
        'status': 'str',
        'updated': 'datetime'
    }

    attribute_map = {
        'account_id': 'account_id',
        'artifact_bucket': 'artifact_bucket',
        'client_id': 'client_id',
        'created': 'created',
        'id': 'id',
        'linked_projects': 'linked_projects',
        'log_bucket': 'log_bucket',
        'status': 'status',
        'updated': 'updated'
    }

    def __init__(self, account_id=None, artifact_bucket=None, client_id=None, created=None, id=None, linked_projects=None, log_bucket=None, status=None, updated=None):  # noqa: E501
        """AwsInfoReponse - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._artifact_bucket = None
        self._client_id = None
        self._created = None
        self._id = None
        self._linked_projects = None
        self._log_bucket = None
        self._status = None
        self._updated = None
        self.discriminator = None
        self.account_id = account_id
        if artifact_bucket is not None:
            self.artifact_bucket = artifact_bucket
        self.client_id = client_id
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if linked_projects is not None:
            self.linked_projects = linked_projects
        if log_bucket is not None:
            self.log_bucket = log_bucket
        if status is not None:
            self.status = status
        if updated is not None:
            self.updated = updated

    @property
    def account_id(self):
        """Gets the account_id of this AwsInfoReponse.  # noqa: E501


        :return: The account_id of this AwsInfoReponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AwsInfoReponse.


        :param account_id: The account_id of this AwsInfoReponse.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def artifact_bucket(self):
        """Gets the artifact_bucket of this AwsInfoReponse.  # noqa: E501


        :return: The artifact_bucket of this AwsInfoReponse.  # noqa: E501
        :rtype: str
        """
        return self._artifact_bucket

    @artifact_bucket.setter
    def artifact_bucket(self, artifact_bucket):
        """Sets the artifact_bucket of this AwsInfoReponse.


        :param artifact_bucket: The artifact_bucket of this AwsInfoReponse.  # noqa: E501
        :type: str
        """

        self._artifact_bucket = artifact_bucket

    @property
    def client_id(self):
        """Gets the client_id of this AwsInfoReponse.  # noqa: E501


        :return: The client_id of this AwsInfoReponse.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AwsInfoReponse.


        :param client_id: The client_id of this AwsInfoReponse.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def created(self):
        """Gets the created of this AwsInfoReponse.  # noqa: E501


        :return: The created of this AwsInfoReponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AwsInfoReponse.


        :param created: The created of this AwsInfoReponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this AwsInfoReponse.  # noqa: E501


        :return: The id of this AwsInfoReponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AwsInfoReponse.


        :param id: The id of this AwsInfoReponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def linked_projects(self):
        """Gets the linked_projects of this AwsInfoReponse.  # noqa: E501


        :return: The linked_projects of this AwsInfoReponse.  # noqa: E501
        :rtype: list[SimpleProject]
        """
        return self._linked_projects

    @linked_projects.setter
    def linked_projects(self, linked_projects):
        """Sets the linked_projects of this AwsInfoReponse.


        :param linked_projects: The linked_projects of this AwsInfoReponse.  # noqa: E501
        :type: list[SimpleProject]
        """

        self._linked_projects = linked_projects

    @property
    def log_bucket(self):
        """Gets the log_bucket of this AwsInfoReponse.  # noqa: E501


        :return: The log_bucket of this AwsInfoReponse.  # noqa: E501
        :rtype: str
        """
        return self._log_bucket

    @log_bucket.setter
    def log_bucket(self, log_bucket):
        """Sets the log_bucket of this AwsInfoReponse.


        :param log_bucket: The log_bucket of this AwsInfoReponse.  # noqa: E501
        :type: str
        """

        self._log_bucket = log_bucket

    @property
    def status(self):
        """Gets the status of this AwsInfoReponse.  # noqa: E501


        :return: The status of this AwsInfoReponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AwsInfoReponse.


        :param status: The status of this AwsInfoReponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def updated(self):
        """Gets the updated of this AwsInfoReponse.  # noqa: E501


        :return: The updated of this AwsInfoReponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this AwsInfoReponse.


        :param updated: The updated of this AwsInfoReponse.  # noqa: E501
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
        if issubclass(AwsInfoReponse, dict):
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
        if not isinstance(other, AwsInfoReponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other