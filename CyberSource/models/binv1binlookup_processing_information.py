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


class Binv1binlookupProcessingInformation(object):
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
        'bin_source': 'str',
        'payout_options': 'Binv1binlookupProcessingInformationPayoutOptions'
    }

    attribute_map = {
        'bin_source': 'binSource',
        'payout_options': 'payoutOptions'
    }

    def __init__(self, bin_source=None, payout_options=None):
        """
        Binv1binlookupProcessingInformation - a model defined in Swagger
        """

        self._bin_source = None
        self._payout_options = None

        if bin_source is not None:
          self.bin_source = bin_source
        if payout_options is not None:
          self.payout_options = payout_options

    @property
    def bin_source(self):
        """
        Gets the bin_source of this Binv1binlookupProcessingInformation.
        Bin Source File Identifier.  Possible values: - itmx - rupay 

        :return: The bin_source of this Binv1binlookupProcessingInformation.
        :rtype: str
        """
        return self._bin_source

    @bin_source.setter
    def bin_source(self, bin_source):
        """
        Sets the bin_source of this Binv1binlookupProcessingInformation.
        Bin Source File Identifier.  Possible values: - itmx - rupay 

        :param bin_source: The bin_source of this Binv1binlookupProcessingInformation.
        :type: str
        """

        self._bin_source = bin_source

    @property
    def payout_options(self):
        """
        Gets the payout_options of this Binv1binlookupProcessingInformation.

        :return: The payout_options of this Binv1binlookupProcessingInformation.
        :rtype: Binv1binlookupProcessingInformationPayoutOptions
        """
        return self._payout_options

    @payout_options.setter
    def payout_options(self, payout_options):
        """
        Sets the payout_options of this Binv1binlookupProcessingInformation.

        :param payout_options: The payout_options of this Binv1binlookupProcessingInformation.
        :type: Binv1binlookupProcessingInformationPayoutOptions
        """

        self._payout_options = payout_options

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
        if not isinstance(other, Binv1binlookupProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
