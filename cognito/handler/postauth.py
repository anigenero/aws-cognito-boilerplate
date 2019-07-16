from typing import Any, Dict
import logging

logger = logging.getLogger('postauth')


def postauth_handler(event: Dict[str, Any], context: Dict):
    """
    Executed after the user has successfully logged in

    :param event: Dict - the lambda event
    :param context: Dict - the lambda context
    """

    # TODO: implement

    return event
