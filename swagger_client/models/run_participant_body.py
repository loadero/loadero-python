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

class RunParticipantBody(object):
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
        'created': 'datetime',
        'group_name': 'str',
        'group_num': 'int',
        'id': 'int',
        'location': 'str',
        'media_type': 'str',
        'network': 'str',
        'participant_name': 'str',
        'participant_num': 'int',
        'profile_id': 'int',
        'record_audio': 'bool',
        'run_id': 'int',
        'updated': 'datetime',
        'video_feed': 'str'
    }

    attribute_map = {
        'audio_feed': 'audio_feed',
        'browser': 'browser',
        'compute_unit': 'compute_unit',
        'created': 'created',
        'group_name': 'group_name',
        'group_num': 'group_num',
        'id': 'id',
        'location': 'location',
        'media_type': 'media_type',
        'network': 'network',
        'participant_name': 'participant_name',
        'participant_num': 'participant_num',
        'profile_id': 'profile_id',
        'record_audio': 'record_audio',
        'run_id': 'run_id',
        'updated': 'updated',
        'video_feed': 'video_feed'
    }

    def __init__(self, audio_feed=None, browser=None, compute_unit=None, created=None, group_name=None, group_num=None, id=None, location=None, media_type=None, network=None, participant_name=None, participant_num=None, profile_id=None, record_audio=None, run_id=None, updated=None, video_feed=None):  # noqa: E501
        """RunParticipantBody - a model defined in Swagger"""  # noqa: E501
        self._audio_feed = None
        self._browser = None
        self._compute_unit = None
        self._created = None
        self._group_name = None
        self._group_num = None
        self._id = None
        self._location = None
        self._media_type = None
        self._network = None
        self._participant_name = None
        self._participant_num = None
        self._profile_id = None
        self._record_audio = None
        self._run_id = None
        self._updated = None
        self._video_feed = None
        self.discriminator = None
        if audio_feed is not None:
            self.audio_feed = audio_feed
        self.browser = browser
        if compute_unit is not None:
            self.compute_unit = compute_unit
        if created is not None:
            self.created = created
        if group_name is not None:
            self.group_name = group_name
        if group_num is not None:
            self.group_num = group_num
        if id is not None:
            self.id = id
        if location is not None:
            self.location = location
        if media_type is not None:
            self.media_type = media_type
        if network is not None:
            self.network = network
        if participant_name is not None:
            self.participant_name = participant_name
        if participant_num is not None:
            self.participant_num = participant_num
        if profile_id is not None:
            self.profile_id = profile_id
        if record_audio is not None:
            self.record_audio = record_audio
        if run_id is not None:
            self.run_id = run_id
        if updated is not None:
            self.updated = updated
        if video_feed is not None:
            self.video_feed = video_feed

    @property
    def audio_feed(self):
        """Gets the audio_feed of this RunParticipantBody.  # noqa: E501


        :return: The audio_feed of this RunParticipantBody.  # noqa: E501
        :rtype: str
        """
        return self._audio_feed

    @audio_feed.setter
    def audio_feed(self, audio_feed):
        """Sets the audio_feed of this RunParticipantBody.


        :param audio_feed: The audio_feed of this RunParticipantBody.  # noqa: E501
        :type: str
        """

        self._audio_feed = audio_feed

    @property
    def browser(self):
        """Gets the browser of this RunParticipantBody.  # noqa: E501


        :return: The browser of this RunParticipantBody.  # noqa: E501
        :rtype: str
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        """Sets the browser of this RunParticipantBody.


        :param browser: The browser of this RunParticipantBody.  # noqa: E501
        :type: str
        """
        if browser is None:
            raise ValueError("Invalid value for `browser`, must not be `None`")  # noqa: E501

        self._browser = browser

    @property
    def compute_unit(self):
        """Gets the compute_unit of this RunParticipantBody.  # noqa: E501


        :return: The compute_unit of this RunParticipantBody.  # noqa: E501
        :rtype: str
        """
        return self._compute_unit

    @compute_unit.setter
    def compute_unit(self, compute_unit):
        """Sets the compute_unit of this RunParticipantBody.


        :param compute_unit: The compute_unit of this RunParticipantBody.  # noqa: E501
        :type: str
        """

        self._compute_unit = compute_unit

    @property
    def created(self):
        """Gets the created of this RunParticipantBody.  # noqa: E501


        :return: The created of this RunParticipantBody.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this RunParticipantBody.


        :param created: The created of this RunParticipantBody.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def group_name(self):
        """Gets the group_name of this RunParticipantBody.  # noqa: E501


        :return: The group_name of this RunParticipantBody.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this RunParticipantBody.


        :param group_name: The group_name of this RunParticipantBody.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def group_num(self):
        """Gets the group_num of this RunParticipantBody.  # noqa: E501


        :return: The group_num of this RunParticipantBody.  # noqa: E501
        :rtype: int
        """
        return self._group_num

    @group_num.setter
    def group_num(self, group_num):
        """Sets the group_num of this RunParticipantBody.


        :param group_num: The group_num of this RunParticipantBody.  # noqa: E501
        :type: int
        """

        self._group_num = group_num

    @property
    def id(self):
        """Gets the id of this RunParticipantBody.  # noqa: E501


        :return: The id of this RunParticipantBody.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RunParticipantBody.


        :param id: The id of this RunParticipantBody.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this RunParticipantBody.  # noqa: E501


        :return: The location of this RunParticipantBody.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this RunParticipantBody.


        :param location: The location of this RunParticipantBody.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def media_type(self):
        """Gets the media_type of this RunParticipantBody.  # noqa: E501


        :return: The media_type of this RunParticipantBody.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this RunParticipantBody.


        :param media_type: The media_type of this RunParticipantBody.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    @property
    def network(self):
        """Gets the network of this RunParticipantBody.  # noqa: E501


        :return: The network of this RunParticipantBody.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this RunParticipantBody.


        :param network: The network of this RunParticipantBody.  # noqa: E501
        :type: str
        """

        self._network = network

    @property
    def participant_name(self):
        """Gets the participant_name of this RunParticipantBody.  # noqa: E501


        :return: The participant_name of this RunParticipantBody.  # noqa: E501
        :rtype: str
        """
        return self._participant_name

    @participant_name.setter
    def participant_name(self, participant_name):
        """Sets the participant_name of this RunParticipantBody.


        :param participant_name: The participant_name of this RunParticipantBody.  # noqa: E501
        :type: str
        """

        self._participant_name = participant_name

    @property
    def participant_num(self):
        """Gets the participant_num of this RunParticipantBody.  # noqa: E501


        :return: The participant_num of this RunParticipantBody.  # noqa: E501
        :rtype: int
        """
        return self._participant_num

    @participant_num.setter
    def participant_num(self, participant_num):
        """Sets the participant_num of this RunParticipantBody.


        :param participant_num: The participant_num of this RunParticipantBody.  # noqa: E501
        :type: int
        """

        self._participant_num = participant_num

    @property
    def profile_id(self):
        """Gets the profile_id of this RunParticipantBody.  # noqa: E501


        :return: The profile_id of this RunParticipantBody.  # noqa: E501
        :rtype: int
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this RunParticipantBody.


        :param profile_id: The profile_id of this RunParticipantBody.  # noqa: E501
        :type: int
        """

        self._profile_id = profile_id

    @property
    def record_audio(self):
        """Gets the record_audio of this RunParticipantBody.  # noqa: E501


        :return: The record_audio of this RunParticipantBody.  # noqa: E501
        :rtype: bool
        """
        return self._record_audio

    @record_audio.setter
    def record_audio(self, record_audio):
        """Sets the record_audio of this RunParticipantBody.


        :param record_audio: The record_audio of this RunParticipantBody.  # noqa: E501
        :type: bool
        """

        self._record_audio = record_audio

    @property
    def run_id(self):
        """Gets the run_id of this RunParticipantBody.  # noqa: E501


        :return: The run_id of this RunParticipantBody.  # noqa: E501
        :rtype: int
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this RunParticipantBody.


        :param run_id: The run_id of this RunParticipantBody.  # noqa: E501
        :type: int
        """

        self._run_id = run_id

    @property
    def updated(self):
        """Gets the updated of this RunParticipantBody.  # noqa: E501


        :return: The updated of this RunParticipantBody.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this RunParticipantBody.


        :param updated: The updated of this RunParticipantBody.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def video_feed(self):
        """Gets the video_feed of this RunParticipantBody.  # noqa: E501


        :return: The video_feed of this RunParticipantBody.  # noqa: E501
        :rtype: str
        """
        return self._video_feed

    @video_feed.setter
    def video_feed(self, video_feed):
        """Sets the video_feed of this RunParticipantBody.


        :param video_feed: The video_feed of this RunParticipantBody.  # noqa: E501
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
        if issubclass(RunParticipantBody, dict):
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
        if not isinstance(other, RunParticipantBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
