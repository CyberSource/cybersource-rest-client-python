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


class TssV2TransactionsPost201ResponseEmbeddedMerchantInformation(object):
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
        'reseller_id': 'str'
    }

    attribute_map = {
        'reseller_id': 'resellerId'
    }

    def __init__(self, reseller_id=None):
        """
        TssV2TransactionsPost201ResponseEmbeddedMerchantInformation - a model defined in Swagger
        """

        self._reseller_id = None

        if reseller_id is not None:
          self.reseller_id = reseller_id

    @property
    def reseller_id(self):
        """
        Gets the reseller_id of this TssV2TransactionsPost201ResponseEmbeddedMerchantInformation.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :return: The reseller_id of this TssV2TransactionsPost201ResponseEmbeddedMerchantInformation.
        :rtype: str
        """
        return self._reseller_id

    @reseller_id.setter
    def reseller_id(self, reseller_id):
        """
        Sets the reseller_id of this TssV2TransactionsPost201ResponseEmbeddedMerchantInformation.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :param reseller_id: The reseller_id of this TssV2TransactionsPost201ResponseEmbeddedMerchantInformation.
        :type: str
        """

        self._reseller_id = reseller_id

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
        if not isinstance(other, TssV2TransactionsPost201ResponseEmbeddedMerchantInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other