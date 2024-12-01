# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.notification_request import NotificationRequest  # noqa: E501
from swagger_server.models.notification_status import NotificationStatus  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNotificationsController(BaseTestCase):
    """NotificationsController integration test stubs"""

    def test_notifications_id_get(self):
        """Test case for notifications_id_get

        Consultar el estado de una notificación
        """
        response = self.client.open(
            '/notifications/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notifications_post(self):
        """Test case for notifications_post

        Enviar una notificación
        """
        body = NotificationRequest()
        response = self.client.open(
            '/notifications',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
