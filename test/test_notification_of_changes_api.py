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
from CyberSource.apis.notification_of_changes_api import NotificationOfChangesApi


class TestNotificationOfChangesApi(unittest.TestCase):
    """ NotificationOfChangesApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.notification_of_changes_api.NotificationOfChangesApi()

    def tearDown(self):
        pass

    def test_get_notification_of_change_report(self):
        """
        Test case for get_notification_of_change_report

        Get Notification of Changes
        """
        pass


if __name__ == '__main__':
    unittest.main()
