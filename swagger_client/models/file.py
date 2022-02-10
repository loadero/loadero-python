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

class File(object):
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
        'content': 'str',
        'created': 'datetime',
        'file_type': 'str',
        'id': 'int',
        'project_id': 'int',
        'updated': 'datetime'
    }

    attribute_map = {
        'content': 'content',
        'created': 'created',
        'file_type': 'file_type',
        'id': 'id',
        'project_id': 'project_id',
        'updated': 'updated'
    }

    def __init__(self, content=None, created=None, file_type=None, id=None, project_id=None, updated=None):  # noqa: E501
        """File - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._created = None
        self._file_type = None
        self._id = None
        self._project_id = None
        self._updated = None
        self.discriminator = None
        self.content = content
        if created is not None:
            self.created = created
        self.file_type = file_type
        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if updated is not None:
            self.updated = updated

    @property
    def content(self):
        """Gets the content of this File.  # noqa: E501


        :return: The content of this File.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this File.


        :param content: The content of this File.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def created(self):
        """Gets the created of this File.  # noqa: E501


        :return: The created of this File.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this File.


        :param created: The created of this File.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def file_type(self):
        """Gets the file_type of this File.  # noqa: E501


        :return: The file_type of this File.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this File.


        :param file_type: The file_type of this File.  # noqa: E501
        :type: str
        """
        if file_type is None:
            raise ValueError("Invalid value for `file_type`, must not be `None`")  # noqa: E501

        self._file_type = file_type

    @property
    def id(self):
        """Gets the id of this File.  # noqa: E501


        :return: The id of this File.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this File.


        :param id: The id of this File.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this File.  # noqa: E501


        :return: The project_id of this File.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this File.


        :param project_id: The project_id of this File.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def updated(self):
        """Gets the updated of this File.  # noqa: E501


        :return: The updated of this File.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this File.


        :param updated: The updated of this File.  # noqa: E501
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
        if issubclass(File, dict):
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
        if not isinstance(other, File):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
