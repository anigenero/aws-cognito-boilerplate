from typing import Any, Dict
import logging

logger = logging.getLogger('postconfirmation')
logger.setLevel(logging.INFO)


def postconfirmation_handler(event: Dict[str, Any], context: Dict = None) -> Dict[str, Any]:
    """
    Executed after the user has successfully completed the confirmation process

    :param event: Dict - the lambda event
    :param context: Dict - the lambda context
    """

    # TODO: implement
    return event
