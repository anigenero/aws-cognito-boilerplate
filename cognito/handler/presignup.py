from typing import Any, Dict
import logging

logger = logging.getLogger('presignup')


def presignup_handler(event: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executed after the user submits the signup payload

    :param event:
    :param context:
    :return:
    """

    # TODO: handle pre-signup

    return event
