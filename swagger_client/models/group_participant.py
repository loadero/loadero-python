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

class GroupParticipant(object):
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
        'audio_feed': 'str',
        'browser': 'str',
        'compute_unit': 'str',
        'count': 'int',
        'created': 'datetime',
        'group_id': 'int',
        'id': 'int',
        'location': 'str',
        'media_type': 'str',
        'name': 'str',
        'network': 'str',
        'profile_id': 'int',
        'record_audio': 'bool',
        'test_id': 'int',
        'updated': 'datetime',
        'video_feed': 'str'
    }

    attribute_map = {
        'audio_feed': 'audio_feed',
        'browser': 'browser',
        'compute_unit': 'compute_unit',
        'count': 'count',
        'created': 'created',
        'group_id': 'group_id',
        'id': 'id',
        'location': 'location',
        'media_type': 'media_type',
        'name': 'name',
        'network': 'network',
        'profile_id': 'profile_id',
        'record_audio': 'record_audio',
        'test_id': 'test_id',
        'updated': 'updated',
        'video_feed': 'video_feed'
    }

    def __init__(self, audio_feed=None, browser=None, compute_unit=None, count=None, created=None, group_id=None, id=None, location=None, media_type=None, name=None, network=None, profile_id=None, record_audio=None, test_id=None, updated=None, video_feed=None):  # noqa: E501
        """GroupParticipant - a model defined in Swagger"""  # noqa: E501
        self._audio_feed = None
        self._browser = None
        self._compute_unit = None
        self._count = None
        self._created = None
        self._group_id = None
        self._id = None
        self._location = None
        self._media_type = None
        self._name = None
        self._network = None
        self._profile_id = None
        self._record_audio = None
        self._test_id = None
        self._updated = None
        self._video_feed = None
        self.discriminator = None
        if audio_feed is not None:
            self.audio_feed = audio_feed
        self.browser = browser
        if compute_unit is not None:
            self.compute_unit = compute_unit
        self.count = count
        if created is not None:
            self.created = created
        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if location is not None:
            self.location = location
        if media_type is not None:
            self.media_type = media_type
        self.name = name
        if network is not None:
            self.network = network
        if profile_id is not None:
            self.profile_id = profile_id
        if record_audio is not None:
            self.record_audio = record_audio
        if test_id is not None:
            self.test_id = test_id
        if updated is not None:
            self.updated = updated
        if video_feed is not None:
            self.video_feed = video_feed

    @property
    def audio_feed(self):
        """Gets the audio_feed of this GroupParticipant.  # noqa: E501


        :return: The audio_feed of this GroupParticipant.  # noqa: E501
        :rtype: str
        """
        return self._audio_feed

    @audio_feed.setter
    def audio_feed(self, audio_feed):
        """Sets the audio_feed of this GroupParticipant.


        :param audio_feed: The audio_feed of this GroupParticipant.  # noqa: E501
        :type: str
        """

        self._audio_feed = audio_feed

    @property
    def browser(self):
        """Gets the browser of this GroupParticipant.  # noqa: E501


        :return: The browser of this GroupParticipant.  # noqa: E501
        :rtype: str
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        """Sets the browser of this GroupParticipant.


        :param browser: The browser of this GroupParticipant.  # noqa: E501
        :type: str
        """
        if browser is None:
            raise ValueError("Invalid value for `browser`, must not be `None`")  # noqa: E501

        self._browser = browser

    @property
    def compute_unit(self):
        """Gets the compute_unit of this GroupParticipant.  # noqa: E501

        normalize indentaion  # noqa: E501

        :return: The compute_unit of this GroupParticipant.  # noqa: E501
        :rtype: str
        """
        return self._compute_unit

    @compute_unit.setter
    def compute_unit(self, compute_unit):
        """Sets the compute_unit of this GroupParticipant.

        normalize indentaion  # noqa: E501

        :param compute_unit: The compute_unit of this GroupParticipant.  # noqa: E501
        :type: str
        """

        self._compute_unit = compute_unit

    @property
    def count(self):
        """Gets the count of this GroupParticipant.  # noqa: E501


        :return: The count of this GroupParticipant.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this GroupParticipant.


        :param count: The count of this GroupParticipant.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def created(self):
        """Gets the created of this GroupParticipant.  # noqa: E501


        :return: The created of this GroupParticipant.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GroupParticipant.


        :param created: The created of this GroupParticipant.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def group_id(self):
        """Gets the group_id of this GroupParticipant.  # noqa: E501


        :return: The group_id of this GroupParticipant.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupParticipant.


        :param group_id: The group_id of this GroupParticipant.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def id(self):
        """Gets the id of this GroupParticipant.  # noqa: E501


        :return: The id of this GroupParticipant.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupParticipant.


        :param id: The id of this GroupParticipant.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this GroupParticipant.  # noqa: E501


        :return: The location of this GroupParticipant.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this GroupParticipant.


        :param location: The location of this GroupParticipant.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def media_type(self):
        """Gets the media_type of this GroupParticipant.  # noqa: E501


        :return: The media_type of this GroupParticipant.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this GroupParticipant.


        :param media_type: The media_type of this GroupParticipant.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    @property
    def name(self):
        """Gets the name of this GroupParticipant.  # noqa: E501


        :return: The name of this GroupParticipant.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupParticipant.


        :param name: The name of this GroupParticipant.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def network(self):
        """Gets the network of this GroupParticipant.  # noqa: E501


        :return: The network of this GroupParticipant.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this GroupParticipant.


        :param network: The network of this GroupParticipant.  # noqa: E501
        :type: str
        """

        self._network = network

    @property
    def profile_id(self):
        """Gets the profile_id of this GroupParticipant.  # noqa: E501


        :return: The profile_id of this GroupParticipant.  # noqa: E501
        :rtype: int
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this GroupParticipant.


        :param profile_id: The profile_id of this GroupParticipant.  # noqa: E501
        :type: int
        """

        self._profile_id = profile_id

    @property
    def record_audio(self):
        """Gets the record_audio of this GroupParticipant.  # noqa: E501


        :return: The record_audio of this GroupParticipant.  # noqa: E501
        :rtype: bool
        """
        return self._record_audio

    @record_audio.setter
    def record_audio(self, record_audio):
        """Sets the record_audio of this GroupParticipant.


        :param record_audio: The record_audio of this GroupParticipant.  # noqa: E501
        :type: bool
        """

        self._record_audio = record_audio

    @property
    def test_id(self):
        """Gets the test_id of this GroupParticipant.  # noqa: E501


        :return: The test_id of this GroupParticipant.  # noqa: E501
        :rtype: int
        """
        return self._test_id

    @test_id.setter
    def test_id(self, test_id):
        """Sets the test_id of this GroupParticipant.


        :param test_id: The test_id of this GroupParticipant.  # noqa: E501
        :type: int
        """

        self._test_id = test_id

    @property
    def updated(self):
        """Gets the updated of this GroupParticipant.  # noqa: E501


        :return: The updated of this GroupParticipant.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this GroupParticipant.


        :param updated: The updated of this GroupParticipant.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def video_feed(self):
        """Gets the video_feed of this GroupParticipant.  # noqa: E501


        :return: The video_feed of this GroupParticipant.  # noqa: E501
        :rtype: str
        """
        return self._video_feed

    @video_feed.setter
    def video_feed(self, video_feed):
        """Sets the video_feed of this GroupParticipant.


        :param video_feed: The video_feed of this GroupParticipant.  # noqa: E501
        :type: str
        """

        self._video_feed = video_feed

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
        if issubclass(GroupParticipant, dict):
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
        if not isinstance(other, GroupParticipant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
