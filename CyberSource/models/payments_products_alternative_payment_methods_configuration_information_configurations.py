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


class PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurations(object):
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
        'merchant_category_code': 'str',
        'processors': 'dict(str, PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurationsProcessors)'
    }

    attribute_map = {
        'merchant_category_code': 'merchantCategoryCode',
        'processors': 'processors'
    }

    def __init__(self, merchant_category_code=None, processors=None):
        """
        PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurations - a model defined in Swagger
        """

        self._merchant_category_code = None
        self._processors = None

        if merchant_category_code is not None:
          self.merchant_category_code = merchant_category_code
        if processors is not None:
          self.processors = processors

    @property
    def merchant_category_code(self):
        """
        Gets the merchant_category_code of this PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurations.
        Merchant Category Code (MCC) is a four-digit number assigned to a business by credit card companies when the business first starts accepting credit cards as a form of payment. The MCC is used to classify the business by the type of goods or services it provides. 

        :return: The merchant_category_code of this PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurations.
        :rtype: str
        """
        return self._merchant_category_code

    @merchant_category_code.setter
    def merchant_category_code(self, merchant_category_code):
        """
        Sets the merchant_category_code of this PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurations.
        Merchant Category Code (MCC) is a four-digit number assigned to a business by credit card companies when the business first starts accepting credit cards as a form of payment. The MCC is used to classify the business by the type of goods or services it provides. 

        :param merchant_category_code: The merchant_category_code of this PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurations.
        :type: str
        """

        self._merchant_category_code = merchant_category_code

    @property
    def processors(self):
        """
        Gets the processors of this PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurations.
        This is a map. The allowed keys are below. Value should be an object containing a sole boolean property - enabled. <table>   <tr>     <td>klarna</td>   </tr>   <tr>     <td>payPal</td>   </tr>   <tr>     <td>alipay</td>   </tr>   <tr>     <td>bancontact</td>   </tr>   <tr>     <td>giropay</td>   </tr>   <tr>     <td>ideal</td>   </tr> </table> 

        :return: The processors of this PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurations.
        :rtype: dict(str, PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurationsProcessors)
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        """
        Sets the processors of this PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurations.
        This is a map. The allowed keys are below. Value should be an object containing a sole boolean property - enabled. <table>   <tr>     <td>klarna</td>   </tr>   <tr>     <td>payPal</td>   </tr>   <tr>     <td>alipay</td>   </tr>   <tr>     <td>bancontact</td>   </tr>   <tr>     <td>giropay</td>   </tr>   <tr>     <td>ideal</td>   </tr> </table> 

        :param processors: The processors of this PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurations.
        :type: dict(str, PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurationsProcessors)
        """

        self._processors = processors

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
        if not isinstance(other, PaymentsProductsAlternativePaymentMethodsConfigurationInformationConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
