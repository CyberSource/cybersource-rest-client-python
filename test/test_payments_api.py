# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import os
import sys
import unittest

import CyberSource
from CyberSource.rest import ApiException
from CyberSource.apis.payments_api import PaymentsApi


class TestPaymentsApi(unittest.TestCase):
    """ PaymentsApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.payments_api.PaymentsApi()

    def tearDown(self):
        pass

    def test_create_order_request(self):
        """
        Test case for create_order_request

        Create a Payment Order Request
        """
        pass

    def test_create_payment(self):
        """
        Test case for create_payment

        Process a Payment
        """
        pass

    def test_create_session_request(self):
        """
        Test case for create_session_request

        Create Alternative Payments Sessions Request
        """
        pass

    def test_increment_auth(self):
        """
        Test case for increment_auth

        Increment an Authorization
        """
        pass

    def test_refresh_payment_status(self):
        """
        Test case for refresh_payment_status

        Check a Payment Status
        """
        pass

    def test_update_session_req(self):
        """
        Test case for update_session_req

        Update Alternative Payments Sessions Request
        """
        pass


if __name__ == '__main__':
    unittest.main()
