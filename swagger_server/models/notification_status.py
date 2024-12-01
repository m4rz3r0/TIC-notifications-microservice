# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NotificationStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, status: str=None):  # noqa: E501
        """NotificationStatus - a model defined in Swagger

        :param id: The id of this NotificationStatus.  # noqa: E501
        :type id: int
        :param status: The status of this NotificationStatus.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'id': int,
            'status': str
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status'
        }
        self._id = id
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'NotificationStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NotificationStatus of this NotificationStatus.  # noqa: E501
        :rtype: NotificationStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this NotificationStatus.


        :return: The id of this NotificationStatus.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this NotificationStatus.


        :param id: The id of this NotificationStatus.
        :type id: int
        """

        self._id = id

    @property
    def status(self) -> str:
        """Gets the status of this NotificationStatus.


        :return: The status of this NotificationStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this NotificationStatus.


        :param status: The status of this NotificationStatus.
        :type status: str
        """

        self._status = status
