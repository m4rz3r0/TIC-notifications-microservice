import connexion
import six

from swagger_server.models.notification_request import NotificationRequest  # noqa: E501
from swagger_server.models.notification_status import NotificationStatus  # noqa: E501
from swagger_server import util


def notifications_id_get(id):  # noqa: E501
    """Consultar el estado de una notificación

    Devuelve el estado de una notificación enviada anteriormente. # noqa: E501

    :param id: ID de la notificación
    :type id: int

    :rtype: NotificationStatus
    """
    return 'do some magic!'


def notifications_post(body):  # noqa: E501
    """Enviar una notificación

    Permite enviar notificaciones relacionadas con respuestas o encuestas. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = NotificationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
