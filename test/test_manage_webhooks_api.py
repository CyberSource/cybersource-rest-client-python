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
from CyberSource.apis.manage_webhooks_api import ManageWebhooksApi


class TestManageWebhooksApi(unittest.TestCase):
    """ ManageWebhooksApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.manage_webhooks_api.ManageWebhooksApi()

    def tearDown(self):
        pass

    def test_delete_webhook_subscription(self):
        """
        Test case for delete_webhook_subscription

        Delete a Webhook Subscription
        """
        pass

    def test_get_all_webhooks(self):
        """
        Test case for get_all_webhooks

        Get Details On All Created Webhooks
        """
        pass

    def test_get_webhook_details(self):
        """
        Test case for get_webhook_details

        Get Details On a Single Webhook
        """
        pass

    def test_replay_previous_webhook(self):
        """
        Test case for replay_previous_webhook

        Replay Previous Webhooks
        """
        pass

    def test_save_asym_egress_key(self):
        """
        Test case for save_asym_egress_key

        Message Level Encryption
        """
        pass

    def test_update_webhook_subscription(self):
        """
        Test case for update_webhook_subscription

        Update a Webhook Subscription
        """
        pass


if __name__ == '__main__':
    unittest.main()