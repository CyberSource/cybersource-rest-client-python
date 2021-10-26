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
from CyberSource.apis.chargeback_summaries_api import ChargebackSummariesApi


class TestChargebackSummariesApi(unittest.TestCase):
    """ ChargebackSummariesApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.chargeback_summaries_api.ChargebackSummariesApi()

    def tearDown(self):
        pass

    def test_get_chargeback_summaries(self):
        """
        Test case for get_chargeback_summaries

        Get Chargeback Summaries
        """
        pass


if __name__ == '__main__':
    unittest.main()