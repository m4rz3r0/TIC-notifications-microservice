# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NotificationRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: str=None, recipient: str=None, message: str=None):  # noqa: E501
        """NotificationRequest - a model defined in Swagger

        :param type: The type of this NotificationRequest.  # noqa: E501
        :type type: str
        :param recipient: The recipient of this NotificationRequest.  # noqa: E501
        :type recipient: str
        :param message: The message of this NotificationRequest.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'type': str,
            'recipient': str,
            'message': str
        }

        self.attribute_map = {
            'type': 'type',
            'recipient': 'recipient',
            'message': 'message'
        }
        self._type = type
        self._recipient = recipient
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'NotificationRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NotificationRequest of this NotificationRequest.  # noqa: E501
        :rtype: NotificationRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this NotificationRequest.


        :return: The type of this NotificationRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this NotificationRequest.


        :param type: The type of this NotificationRequest.
        :type type: str
        """

        self._type = type

    @property
    def recipient(self) -> str:
        """Gets the recipient of this NotificationRequest.


        :return: The recipient of this NotificationRequest.
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient: str):
        """Sets the recipient of this NotificationRequest.


        :param recipient: The recipient of this NotificationRequest.
        :type recipient: str
        """

        self._recipient = recipient

    @property
    def message(self) -> str:
        """Gets the message of this NotificationRequest.


        :return: The message of this NotificationRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this NotificationRequest.


        :param message: The message of this NotificationRequest.
        :type message: str
        """

        self._message = message
