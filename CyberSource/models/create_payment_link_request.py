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


class CreatePaymentLinkRequest(object):
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
        'client_reference_information': 'Invoicingv2invoicesClientReferenceInformation',
        'processing_information': 'Iplv2paymentlinksProcessingInformation',
        'purchase_information': 'Iplv2paymentlinksPurchaseInformation',
        'order_information': 'Iplv2paymentlinksOrderInformation'
    }

    attribute_map = {
        'client_reference_information': 'clientReferenceInformation',
        'processing_information': 'processingInformation',
        'purchase_information': 'purchaseInformation',
        'order_information': 'orderInformation'
    }

    def __init__(self, client_reference_information=None, processing_information=None, purchase_information=None, order_information=None):
        """
        CreatePaymentLinkRequest - a model defined in Swagger
        """

        self._client_reference_information = None
        self._processing_information = None
        self._purchase_information = None
        self._order_information = None

        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        self.processing_information = processing_information
        self.purchase_information = purchase_information
        self.order_information = order_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this CreatePaymentLinkRequest.

        :return: The client_reference_information of this CreatePaymentLinkRequest.
        :rtype: Invoicingv2invoicesClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this CreatePaymentLinkRequest.

        :param client_reference_information: The client_reference_information of this CreatePaymentLinkRequest.
        :type: Invoicingv2invoicesClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this CreatePaymentLinkRequest.

        :return: The processing_information of this CreatePaymentLinkRequest.
        :rtype: Iplv2paymentlinksProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this CreatePaymentLinkRequest.

        :param processing_information: The processing_information of this CreatePaymentLinkRequest.
        :type: Iplv2paymentlinksProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def purchase_information(self):
        """
        Gets the purchase_information of this CreatePaymentLinkRequest.

        :return: The purchase_information of this CreatePaymentLinkRequest.
        :rtype: Iplv2paymentlinksPurchaseInformation
        """
        return self._purchase_information

    @purchase_information.setter
    def purchase_information(self, purchase_information):
        """
        Sets the purchase_information of this CreatePaymentLinkRequest.

        :param purchase_information: The purchase_information of this CreatePaymentLinkRequest.
        :type: Iplv2paymentlinksPurchaseInformation
        """

        self._purchase_information = purchase_information

    @property
    def order_information(self):
        """
        Gets the order_information of this CreatePaymentLinkRequest.

        :return: The order_information of this CreatePaymentLinkRequest.
        :rtype: Iplv2paymentlinksOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this CreatePaymentLinkRequest.

        :param order_information: The order_information of this CreatePaymentLinkRequest.
        :type: Iplv2paymentlinksOrderInformation
        """

        self._order_information = order_information

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
        if not isinstance(other, CreatePaymentLinkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
