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


class GenerateCaptureContextRequest(object):
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
        'client_version': 'str',
        'target_origins': 'list[str]',
        'allowed_card_networks': 'list[str]',
        'checkout_api_initialization': 'Microformv2sessionsCheckoutApiInitialization'
    }

    attribute_map = {
        'client_version': 'clientVersion',
        'target_origins': 'targetOrigins',
        'allowed_card_networks': 'allowedCardNetworks',
        'checkout_api_initialization': 'checkoutApiInitialization'
    }

    def __init__(self, client_version=None, target_origins=None, allowed_card_networks=None, checkout_api_initialization=None):
        """
        GenerateCaptureContextRequest - a model defined in Swagger
        """

        self._client_version = None
        self._target_origins = None
        self._allowed_card_networks = None
        self._checkout_api_initialization = None

        if client_version is not None:
          self.client_version = client_version
        if target_origins is not None:
          self.target_origins = target_origins
        if allowed_card_networks is not None:
          self.allowed_card_networks = allowed_card_networks
        if checkout_api_initialization is not None:
          self.checkout_api_initialization = checkout_api_initialization

    @property
    def client_version(self):
        """
        Gets the client_version of this GenerateCaptureContextRequest.
        Specify the version of Microform that you want to use. 

        :return: The client_version of this GenerateCaptureContextRequest.
        :rtype: str
        """
        return self._client_version

    @client_version.setter
    def client_version(self, client_version):
        """
        Sets the client_version of this GenerateCaptureContextRequest.
        Specify the version of Microform that you want to use. 

        :param client_version: The client_version of this GenerateCaptureContextRequest.
        :type: str
        """

        self._client_version = client_version

    @property
    def target_origins(self):
        """
        Gets the target_origins of this GenerateCaptureContextRequest.
        The [target origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin) of the website on which you will be launching Microform is defined by the scheme (protocol), hostname (domain) and port number (if used).    You must use https://hostname (unless you use http://localhost) Wildcards are NOT supported.  Ensure that subdomains are included. Any valid top-level domain is supported (e.g. .com, .co.uk, .gov.br etc)  Examples:   - https://example.com   - https://subdomain.example.com   - https://example.com:8080<br><br>  If you are embedding within multiple nested iframes you need to specify the origins of all the browser contexts used, for example:    targetOrigins: [     \"https://example.com\",     \"https://basket.example.com\",     \"https://ecom.example.com\"   ] 

        :return: The target_origins of this GenerateCaptureContextRequest.
        :rtype: list[str]
        """
        return self._target_origins

    @target_origins.setter
    def target_origins(self, target_origins):
        """
        Sets the target_origins of this GenerateCaptureContextRequest.
        The [target origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin) of the website on which you will be launching Microform is defined by the scheme (protocol), hostname (domain) and port number (if used).    You must use https://hostname (unless you use http://localhost) Wildcards are NOT supported.  Ensure that subdomains are included. Any valid top-level domain is supported (e.g. .com, .co.uk, .gov.br etc)  Examples:   - https://example.com   - https://subdomain.example.com   - https://example.com:8080<br><br>  If you are embedding within multiple nested iframes you need to specify the origins of all the browser contexts used, for example:    targetOrigins: [     \"https://example.com\",     \"https://basket.example.com\",     \"https://ecom.example.com\"   ] 

        :param target_origins: The target_origins of this GenerateCaptureContextRequest.
        :type: list[str]
        """

        self._target_origins = target_origins

    @property
    def allowed_card_networks(self):
        """
        Gets the allowed_card_networks of this GenerateCaptureContextRequest.
        The list of card networks you want to use for this Microform transaction.  Microform currently supports the following card networks: - VISA - MASTERCARD - AMEX - CARNET - CARTESBANCAIRES - CUP - DINERSCLUB - DISCOVER - EFTPOS - ELO - JCB - JCREW - MADA - MAESTRO - MEEZA 

        :return: The allowed_card_networks of this GenerateCaptureContextRequest.
        :rtype: list[str]
        """
        return self._allowed_card_networks

    @allowed_card_networks.setter
    def allowed_card_networks(self, allowed_card_networks):
        """
        Sets the allowed_card_networks of this GenerateCaptureContextRequest.
        The list of card networks you want to use for this Microform transaction.  Microform currently supports the following card networks: - VISA - MASTERCARD - AMEX - CARNET - CARTESBANCAIRES - CUP - DINERSCLUB - DISCOVER - EFTPOS - ELO - JCB - JCREW - MADA - MAESTRO - MEEZA 

        :param allowed_card_networks: The allowed_card_networks of this GenerateCaptureContextRequest.
        :type: list[str]
        """

        self._allowed_card_networks = allowed_card_networks

    @property
    def checkout_api_initialization(self):
        """
        Gets the checkout_api_initialization of this GenerateCaptureContextRequest.

        :return: The checkout_api_initialization of this GenerateCaptureContextRequest.
        :rtype: Microformv2sessionsCheckoutApiInitialization
        """
        return self._checkout_api_initialization

    @checkout_api_initialization.setter
    def checkout_api_initialization(self, checkout_api_initialization):
        """
        Sets the checkout_api_initialization of this GenerateCaptureContextRequest.

        :param checkout_api_initialization: The checkout_api_initialization of this GenerateCaptureContextRequest.
        :type: Microformv2sessionsCheckoutApiInitialization
        """

        self._checkout_api_initialization = checkout_api_initialization

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
        if not isinstance(other, GenerateCaptureContextRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
