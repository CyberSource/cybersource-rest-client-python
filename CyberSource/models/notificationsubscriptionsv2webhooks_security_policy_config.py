# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class Notificationsubscriptionsv2webhooksSecurityPolicyConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'o_auth_token_expiry': 'str',
        'o_auth_url': 'str',
        'o_auth_token_type': 'str'
    }

    attribute_map = {
        'o_auth_token_expiry': 'oAuthTokenExpiry',
        'o_auth_url': 'oAuthURL',
        'o_auth_token_type': 'oAuthTokenType'
    }

    def __init__(self, o_auth_token_expiry=None, o_auth_url=None, o_auth_token_type=None):
        """
        Notificationsubscriptionsv2webhooksSecurityPolicyConfig - a model defined in Swagger
        """

        self._o_auth_token_expiry = None
        self._o_auth_url = None
        self._o_auth_token_type = None

        if o_auth_token_expiry is not None:
          self.o_auth_token_expiry = o_auth_token_expiry
        if o_auth_url is not None:
          self.o_auth_url = o_auth_url
        if o_auth_token_type is not None:
          self.o_auth_token_type = o_auth_token_type

    @property
    def o_auth_token_expiry(self):
        """
        Gets the o_auth_token_expiry of this Notificationsubscriptionsv2webhooksSecurityPolicyConfig.
        Token expiration for the oAuth server.

        :return: The o_auth_token_expiry of this Notificationsubscriptionsv2webhooksSecurityPolicyConfig.
        :rtype: str
        """
        return self._o_auth_token_expiry

    @o_auth_token_expiry.setter
    def o_auth_token_expiry(self, o_auth_token_expiry):
        """
        Sets the o_auth_token_expiry of this Notificationsubscriptionsv2webhooksSecurityPolicyConfig.
        Token expiration for the oAuth server.

        :param o_auth_token_expiry: The o_auth_token_expiry of this Notificationsubscriptionsv2webhooksSecurityPolicyConfig.
        :type: str
        """

        self._o_auth_token_expiry = o_auth_token_expiry

    @property
    def o_auth_url(self):
        """
        Gets the o_auth_url of this Notificationsubscriptionsv2webhooksSecurityPolicyConfig.
        Client direct endpoint to the oAuth server.

        :return: The o_auth_url of this Notificationsubscriptionsv2webhooksSecurityPolicyConfig.
        :rtype: str
        """
        return self._o_auth_url

    @o_auth_url.setter
    def o_auth_url(self, o_auth_url):
        """
        Sets the o_auth_url of this Notificationsubscriptionsv2webhooksSecurityPolicyConfig.
        Client direct endpoint to the oAuth server.

        :param o_auth_url: The o_auth_url of this Notificationsubscriptionsv2webhooksSecurityPolicyConfig.
        :type: str
        """

        self._o_auth_url = o_auth_url

    @property
    def o_auth_token_type(self):
        """
        Gets the o_auth_token_type of this Notificationsubscriptionsv2webhooksSecurityPolicyConfig.
        Token type for the oAuth config.

        :return: The o_auth_token_type of this Notificationsubscriptionsv2webhooksSecurityPolicyConfig.
        :rtype: str
        """
        return self._o_auth_token_type

    @o_auth_token_type.setter
    def o_auth_token_type(self, o_auth_token_type):
        """
        Sets the o_auth_token_type of this Notificationsubscriptionsv2webhooksSecurityPolicyConfig.
        Token type for the oAuth config.

        :param o_auth_token_type: The o_auth_token_type of this Notificationsubscriptionsv2webhooksSecurityPolicyConfig.
        :type: str
        """

        self._o_auth_token_type = o_auth_token_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Notificationsubscriptionsv2webhooksSecurityPolicyConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
