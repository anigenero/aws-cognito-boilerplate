from unittest.mock import patch
from auth.auth import handler
import unittest


class TestAuth(unittest.TestCase):

    def test_bad_trigger_source(self):
        # test error is thrown on bad trigger
        event = {
            "triggerSource": "foobar"
        }

        with self.assertRaises(Exception):
            handler(event, None)

    def test_pre_auth_authentication_call(self):
        # should call post auth handler on auth

        event = {
            "userName": "nick.fury@shield.gov",
            "triggerSource": "PreAuthentication_Authentication"
        }

        handler(event, None)

    def test_post_auth_authentication_call(self):
        # should call post auth handler on auth

        event = {
            "userName": "nick.fury@shield.gov",
            "triggerSource": "PostAuthentication_Authentication"
        }

        handler(event, None)

    def test_post_confirmation_confirm_signup_call(self):
        # should call post confirmation on confirm signup

        event = {
            "userName": "nick.fury@shield.gov",
            "triggerSource": "PostConfirmation_ConfirmSignUp"
        }

        handler(event, None)

    def test_post_confirmation_confirm_forgot_password_call(self):
        # should call post confirmation on confirm forgot password

        event = {
            "userName": "nick.fury@shield.gov",
            "triggerSource": "PostConfirmation_ConfirmForgotPassword"
        }

        handler(event, None)

    def test_presignup_call(self):
        # should call presignup on presignup

        event = {
            "userName": "nick.fury@shield.gov",
            "triggerSource": "PreSignUp_SignUp"
        }

        handler(event, None)

    def test_presignup_admin_call(self):
        # should call presignup on admin create user

        event = {
            "userName": "nick.fury@shield.gov",
            "triggerSource": "PreSignUp_AdminCreateUser"
        }

        handler(event, None)
