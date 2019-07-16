from typing import Any, Dict
import logging

logger = logging.getLogger('preauth')
logger.setLevel(logging.INFO)


def preauth_handler(event: Dict[str, Any], context: Dict = None) -> Dict[str, Any]:
    """
    Executed before the user is authenticated

    :param event: Dict - the lambda event
    :param context: Dict - the lambda context
    """

    # TODO: implement
    return event
