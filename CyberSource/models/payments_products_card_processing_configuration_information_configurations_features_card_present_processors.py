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


class PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors(object):
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
        'default_point_of_sale_terminal_id': 'str',
        'point_of_sale_terminal_ids': 'list[str]',
        'disable_point_of_sale_terminal_id_validation': 'bool',
        'pin_debit_network_order': 'str',
        'pin_debit_reimbursement_code': 'str',
        'financial_institution_id': 'str',
        'enable_pin_translation': 'bool'
    }

    attribute_map = {
        'default_point_of_sale_terminal_id': 'defaultPointOfSaleTerminalId',
        'point_of_sale_terminal_ids': 'pointOfSaleTerminalIds',
        'disable_point_of_sale_terminal_id_validation': 'disablePointOfSaleTerminalIdValidation',
        'pin_debit_network_order': 'pinDebitNetworkOrder',
        'pin_debit_reimbursement_code': 'pinDebitReimbursementCode',
        'financial_institution_id': 'financialInstitutionId',
        'enable_pin_translation': 'enablePinTranslation'
    }

    def __init__(self, default_point_of_sale_terminal_id=None, point_of_sale_terminal_ids=None, disable_point_of_sale_terminal_id_validation=None, pin_debit_network_order=None, pin_debit_reimbursement_code=None, financial_institution_id=None, enable_pin_translation=None):
        """
        PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors - a model defined in Swagger
        """

        self._default_point_of_sale_terminal_id = None
        self._point_of_sale_terminal_ids = None
        self._disable_point_of_sale_terminal_id_validation = None
        self._pin_debit_network_order = None
        self._pin_debit_reimbursement_code = None
        self._financial_institution_id = None
        self._enable_pin_translation = None

        if default_point_of_sale_terminal_id is not None:
          self.default_point_of_sale_terminal_id = default_point_of_sale_terminal_id
        if point_of_sale_terminal_ids is not None:
          self.point_of_sale_terminal_ids = point_of_sale_terminal_ids
        if disable_point_of_sale_terminal_id_validation is not None:
          self.disable_point_of_sale_terminal_id_validation = disable_point_of_sale_terminal_id_validation
        if pin_debit_network_order is not None:
          self.pin_debit_network_order = pin_debit_network_order
        if pin_debit_reimbursement_code is not None:
          self.pin_debit_reimbursement_code = pin_debit_reimbursement_code
        if financial_institution_id is not None:
          self.financial_institution_id = financial_institution_id
        if enable_pin_translation is not None:
          self.enable_pin_translation = enable_pin_translation

    @property
    def default_point_of_sale_terminal_id(self):
        """
        Gets the default_point_of_sale_terminal_id of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        Default Terminal ID used for Card Present and Virtual Terminal transactions. Applicable for VPC, GPX (gpx), American Express Direct (amexdirect) and Chase Paymentech Salem (chasepaymentechsalem) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th><th>Default Value</th></tr></thead> <tr><td>American Express Direct</td><td>cp</td><td>Yes</td><td>4</td><td>8</td><td>^[0-9a-zA-Z]+$</td><td>1111</td></tr> </table> 

        :return: The default_point_of_sale_terminal_id of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :rtype: str
        """
        return self._default_point_of_sale_terminal_id

    @default_point_of_sale_terminal_id.setter
    def default_point_of_sale_terminal_id(self, default_point_of_sale_terminal_id):
        """
        Sets the default_point_of_sale_terminal_id of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        Default Terminal ID used for Card Present and Virtual Terminal transactions. Applicable for VPC, GPX (gpx), American Express Direct (amexdirect) and Chase Paymentech Salem (chasepaymentechsalem) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th><th>Default Value</th></tr></thead> <tr><td>American Express Direct</td><td>cp</td><td>Yes</td><td>4</td><td>8</td><td>^[0-9a-zA-Z]+$</td><td>1111</td></tr> </table> 

        :param default_point_of_sale_terminal_id: The default_point_of_sale_terminal_id of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :type: str
        """

        self._default_point_of_sale_terminal_id = default_point_of_sale_terminal_id

    @property
    def point_of_sale_terminal_ids(self):
        """
        Gets the point_of_sale_terminal_ids of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        For retail transactions, if merchant chooses to send the terminal id in the API, then that value has to be validated before being used. Holds a comma separated list of all possible terminal ids that the merchant is likely to send. Applicable for VPC processors.

        :return: The point_of_sale_terminal_ids of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :rtype: list[str]
        """
        return self._point_of_sale_terminal_ids

    @point_of_sale_terminal_ids.setter
    def point_of_sale_terminal_ids(self, point_of_sale_terminal_ids):
        """
        Sets the point_of_sale_terminal_ids of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        For retail transactions, if merchant chooses to send the terminal id in the API, then that value has to be validated before being used. Holds a comma separated list of all possible terminal ids that the merchant is likely to send. Applicable for VPC processors.

        :param point_of_sale_terminal_ids: The point_of_sale_terminal_ids of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :type: list[str]
        """

        self._point_of_sale_terminal_ids = point_of_sale_terminal_ids

    @property
    def disable_point_of_sale_terminal_id_validation(self):
        """
        Gets the disable_point_of_sale_terminal_id_validation of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        Disables terminal ID validation. Applicable for VPC processors.

        :return: The disable_point_of_sale_terminal_id_validation of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :rtype: bool
        """
        return self._disable_point_of_sale_terminal_id_validation

    @disable_point_of_sale_terminal_id_validation.setter
    def disable_point_of_sale_terminal_id_validation(self, disable_point_of_sale_terminal_id_validation):
        """
        Sets the disable_point_of_sale_terminal_id_validation of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        Disables terminal ID validation. Applicable for VPC processors.

        :param disable_point_of_sale_terminal_id_validation: The disable_point_of_sale_terminal_id_validation of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :type: bool
        """

        self._disable_point_of_sale_terminal_id_validation = disable_point_of_sale_terminal_id_validation

    @property
    def pin_debit_network_order(self):
        """
        Gets the pin_debit_network_order of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        Order of the networks in which Visa should make routing decisions. Applicable for GPX (gpx) and VPC processors.

        :return: The pin_debit_network_order of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :rtype: str
        """
        return self._pin_debit_network_order

    @pin_debit_network_order.setter
    def pin_debit_network_order(self, pin_debit_network_order):
        """
        Sets the pin_debit_network_order of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        Order of the networks in which Visa should make routing decisions. Applicable for GPX (gpx) and VPC processors.

        :param pin_debit_network_order: The pin_debit_network_order of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :type: str
        """

        self._pin_debit_network_order = pin_debit_network_order

    @property
    def pin_debit_reimbursement_code(self):
        """
        Gets the pin_debit_reimbursement_code of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        This attribute requests VIP to qualify a given PIN Debit transaction for a certain type of interchange program. Y = SMS supermarket, Z = SMS general merchant. Applicable for GPX (gpx) and VPC processors.

        :return: The pin_debit_reimbursement_code of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :rtype: str
        """
        return self._pin_debit_reimbursement_code

    @pin_debit_reimbursement_code.setter
    def pin_debit_reimbursement_code(self, pin_debit_reimbursement_code):
        """
        Sets the pin_debit_reimbursement_code of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        This attribute requests VIP to qualify a given PIN Debit transaction for a certain type of interchange program. Y = SMS supermarket, Z = SMS general merchant. Applicable for GPX (gpx) and VPC processors.

        :param pin_debit_reimbursement_code: The pin_debit_reimbursement_code of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :type: str
        """

        self._pin_debit_reimbursement_code = pin_debit_reimbursement_code

    @property
    def financial_institution_id(self):
        """
        Gets the financial_institution_id of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        Acquirer Institution ID for the PIN Debit Transactions. Applicable for GPX (gpx) and VPC processors.

        :return: The financial_institution_id of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :rtype: str
        """
        return self._financial_institution_id

    @financial_institution_id.setter
    def financial_institution_id(self, financial_institution_id):
        """
        Sets the financial_institution_id of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        Acquirer Institution ID for the PIN Debit Transactions. Applicable for GPX (gpx) and VPC processors.

        :param financial_institution_id: The financial_institution_id of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :type: str
        """

        self._financial_institution_id = financial_institution_id

    @property
    def enable_pin_translation(self):
        """
        Gets the enable_pin_translation of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        Enables CyberSource PIN Translation for Online PIN Transactions. Please ensure you have exchanged PIN keys with CyberSource to use this feature. Applicable for VPC processors.

        :return: The enable_pin_translation of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :rtype: bool
        """
        return self._enable_pin_translation

    @enable_pin_translation.setter
    def enable_pin_translation(self, enable_pin_translation):
        """
        Sets the enable_pin_translation of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        Enables CyberSource PIN Translation for Online PIN Transactions. Please ensure you have exchanged PIN keys with CyberSource to use this feature. Applicable for VPC processors.

        :param enable_pin_translation: The enable_pin_translation of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors.
        :type: bool
        """

        self._enable_pin_translation = enable_pin_translation

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
        if not isinstance(other, PaymentsProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardPresentProcessors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other