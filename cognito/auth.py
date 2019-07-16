from cognito.handler import postauth_handler, postconfirmation_handler, preauth_handler, presignup_handler

from typing import Any, Dict

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(name)s.%(funcName)s (%(filename)s:%(lineno)d) - %(message)s')

logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

logger = logging.getLogger(__name__)


def handler(event: Dict[str, Any], context: Dict[str, Any]):
    """
    Handles the cognito trigger event

    :param event: Dict - the cognito trigger event
    :param context: Dict - the context
    :return: trigger event response
    """

    # see https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html
    _switcher = {
        'PreAuthentication_Authentication': preauth_handler,
        'PostAuthentication_Authentication': postauth_handler,
        'PostConfirmation_ConfirmSignUp': postconfirmation_handler,
        'PostConfirmation_ConfirmForgotPassword': postconfirmation_handler,
        'PreSignUp_SignUp': presignup_handler,
        'PreSignUp_AdminCreateUser': presignup_handler
    }

    logger.info("Handling event %s", event['triggerSource'])

    func = _switcher.get(event['triggerSource'], None)

    if func is not None:
        return func(event, context)
    else:
        raise Exception('Invalid trigger source ' + event['triggerSource'])
