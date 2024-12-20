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
from CyberSource.apis.invoice_settings_api import InvoiceSettingsApi


class TestInvoiceSettingsApi(unittest.TestCase):
    """ InvoiceSettingsApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.invoice_settings_api.InvoiceSettingsApi()

    def tearDown(self):
        pass

    def test_get_invoice_settings(self):
        """
        Test case for get_invoice_settings

        Get Invoice Settings
        """
        pass

    def test_update_invoice_settings(self):
        """
        Test case for update_invoice_settings

        Update Invoice Settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
