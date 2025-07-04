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


class InlineResponse2012SetupsPayments(object):
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
        'card_processing': 'InlineResponse2012SetupsPaymentsCardProcessing',
        'alternative_payment_methods': 'InlineResponse2012SetupsPaymentsAlternativePaymentMethods',
        'card_present_connect': 'InlineResponse2012SetupsPaymentsCardProcessing',
        'e_check': 'InlineResponse2012SetupsPaymentsCardProcessing',
        'payer_authentication': 'InlineResponse2012SetupsPaymentsCardProcessing',
        'digital_payments': 'InlineResponse2012SetupsPaymentsDigitalPayments',
        'secure_acceptance': 'InlineResponse2012SetupsPaymentsCardProcessing',
        'virtual_terminal': 'InlineResponse2012SetupsPaymentsCardProcessing',
        'currency_conversion': 'InlineResponse2012SetupsPaymentsCardProcessing',
        'tax': 'InlineResponse2012SetupsPaymentsDigitalPayments',
        'customer_invoicing': 'InlineResponse2012SetupsPaymentsDigitalPayments',
        'recurring_billing': 'InlineResponse2012SetupsPaymentsCardProcessing',
        'cybs_ready_terminal': 'InlineResponse2012SetupsPaymentsCardProcessing',
        'payment_orchestration': 'InlineResponse2012SetupsPaymentsDigitalPayments',
        'payouts': 'InlineResponse2012SetupsPaymentsCardProcessing',
        'pay_by_link': 'InlineResponse2012SetupsPaymentsDigitalPayments',
        'unified_checkout': 'InlineResponse2012SetupsPaymentsDigitalPayments',
        'receivables_manager': 'InlineResponse2012SetupsPaymentsDigitalPayments',
        'service_fee': 'InlineResponse2012SetupsPaymentsCardProcessing'
    }

    attribute_map = {
        'card_processing': 'cardProcessing',
        'alternative_payment_methods': 'alternativePaymentMethods',
        'card_present_connect': 'cardPresentConnect',
        'e_check': 'eCheck',
        'payer_authentication': 'payerAuthentication',
        'digital_payments': 'digitalPayments',
        'secure_acceptance': 'secureAcceptance',
        'virtual_terminal': 'virtualTerminal',
        'currency_conversion': 'currencyConversion',
        'tax': 'tax',
        'customer_invoicing': 'customerInvoicing',
        'recurring_billing': 'recurringBilling',
        'cybs_ready_terminal': 'cybsReadyTerminal',
        'payment_orchestration': 'paymentOrchestration',
        'payouts': 'payouts',
        'pay_by_link': 'payByLink',
        'unified_checkout': 'unifiedCheckout',
        'receivables_manager': 'receivablesManager',
        'service_fee': 'serviceFee'
    }

    def __init__(self, card_processing=None, alternative_payment_methods=None, card_present_connect=None, e_check=None, payer_authentication=None, digital_payments=None, secure_acceptance=None, virtual_terminal=None, currency_conversion=None, tax=None, customer_invoicing=None, recurring_billing=None, cybs_ready_terminal=None, payment_orchestration=None, payouts=None, pay_by_link=None, unified_checkout=None, receivables_manager=None, service_fee=None):
        """
        InlineResponse2012SetupsPayments - a model defined in Swagger
        """

        self._card_processing = None
        self._alternative_payment_methods = None
        self._card_present_connect = None
        self._e_check = None
        self._payer_authentication = None
        self._digital_payments = None
        self._secure_acceptance = None
        self._virtual_terminal = None
        self._currency_conversion = None
        self._tax = None
        self._customer_invoicing = None
        self._recurring_billing = None
        self._cybs_ready_terminal = None
        self._payment_orchestration = None
        self._payouts = None
        self._pay_by_link = None
        self._unified_checkout = None
        self._receivables_manager = None
        self._service_fee = None

        if card_processing is not None:
          self.card_processing = card_processing
        if alternative_payment_methods is not None:
          self.alternative_payment_methods = alternative_payment_methods
        if card_present_connect is not None:
          self.card_present_connect = card_present_connect
        if e_check is not None:
          self.e_check = e_check
        if payer_authentication is not None:
          self.payer_authentication = payer_authentication
        if digital_payments is not None:
          self.digital_payments = digital_payments
        if secure_acceptance is not None:
          self.secure_acceptance = secure_acceptance
        if virtual_terminal is not None:
          self.virtual_terminal = virtual_terminal
        if currency_conversion is not None:
          self.currency_conversion = currency_conversion
        if tax is not None:
          self.tax = tax
        if customer_invoicing is not None:
          self.customer_invoicing = customer_invoicing
        if recurring_billing is not None:
          self.recurring_billing = recurring_billing
        if cybs_ready_terminal is not None:
          self.cybs_ready_terminal = cybs_ready_terminal
        if payment_orchestration is not None:
          self.payment_orchestration = payment_orchestration
        if payouts is not None:
          self.payouts = payouts
        if pay_by_link is not None:
          self.pay_by_link = pay_by_link
        if unified_checkout is not None:
          self.unified_checkout = unified_checkout
        if receivables_manager is not None:
          self.receivables_manager = receivables_manager
        if service_fee is not None:
          self.service_fee = service_fee

    @property
    def card_processing(self):
        """
        Gets the card_processing of this InlineResponse2012SetupsPayments.

        :return: The card_processing of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsCardProcessing
        """
        return self._card_processing

    @card_processing.setter
    def card_processing(self, card_processing):
        """
        Sets the card_processing of this InlineResponse2012SetupsPayments.

        :param card_processing: The card_processing of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsCardProcessing
        """

        self._card_processing = card_processing

    @property
    def alternative_payment_methods(self):
        """
        Gets the alternative_payment_methods of this InlineResponse2012SetupsPayments.

        :return: The alternative_payment_methods of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsAlternativePaymentMethods
        """
        return self._alternative_payment_methods

    @alternative_payment_methods.setter
    def alternative_payment_methods(self, alternative_payment_methods):
        """
        Sets the alternative_payment_methods of this InlineResponse2012SetupsPayments.

        :param alternative_payment_methods: The alternative_payment_methods of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsAlternativePaymentMethods
        """

        self._alternative_payment_methods = alternative_payment_methods

    @property
    def card_present_connect(self):
        """
        Gets the card_present_connect of this InlineResponse2012SetupsPayments.

        :return: The card_present_connect of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsCardProcessing
        """
        return self._card_present_connect

    @card_present_connect.setter
    def card_present_connect(self, card_present_connect):
        """
        Sets the card_present_connect of this InlineResponse2012SetupsPayments.

        :param card_present_connect: The card_present_connect of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsCardProcessing
        """

        self._card_present_connect = card_present_connect

    @property
    def e_check(self):
        """
        Gets the e_check of this InlineResponse2012SetupsPayments.

        :return: The e_check of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsCardProcessing
        """
        return self._e_check

    @e_check.setter
    def e_check(self, e_check):
        """
        Sets the e_check of this InlineResponse2012SetupsPayments.

        :param e_check: The e_check of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsCardProcessing
        """

        self._e_check = e_check

    @property
    def payer_authentication(self):
        """
        Gets the payer_authentication of this InlineResponse2012SetupsPayments.

        :return: The payer_authentication of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsCardProcessing
        """
        return self._payer_authentication

    @payer_authentication.setter
    def payer_authentication(self, payer_authentication):
        """
        Sets the payer_authentication of this InlineResponse2012SetupsPayments.

        :param payer_authentication: The payer_authentication of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsCardProcessing
        """

        self._payer_authentication = payer_authentication

    @property
    def digital_payments(self):
        """
        Gets the digital_payments of this InlineResponse2012SetupsPayments.

        :return: The digital_payments of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsDigitalPayments
        """
        return self._digital_payments

    @digital_payments.setter
    def digital_payments(self, digital_payments):
        """
        Sets the digital_payments of this InlineResponse2012SetupsPayments.

        :param digital_payments: The digital_payments of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsDigitalPayments
        """

        self._digital_payments = digital_payments

    @property
    def secure_acceptance(self):
        """
        Gets the secure_acceptance of this InlineResponse2012SetupsPayments.

        :return: The secure_acceptance of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsCardProcessing
        """
        return self._secure_acceptance

    @secure_acceptance.setter
    def secure_acceptance(self, secure_acceptance):
        """
        Sets the secure_acceptance of this InlineResponse2012SetupsPayments.

        :param secure_acceptance: The secure_acceptance of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsCardProcessing
        """

        self._secure_acceptance = secure_acceptance

    @property
    def virtual_terminal(self):
        """
        Gets the virtual_terminal of this InlineResponse2012SetupsPayments.

        :return: The virtual_terminal of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsCardProcessing
        """
        return self._virtual_terminal

    @virtual_terminal.setter
    def virtual_terminal(self, virtual_terminal):
        """
        Sets the virtual_terminal of this InlineResponse2012SetupsPayments.

        :param virtual_terminal: The virtual_terminal of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsCardProcessing
        """

        self._virtual_terminal = virtual_terminal

    @property
    def currency_conversion(self):
        """
        Gets the currency_conversion of this InlineResponse2012SetupsPayments.

        :return: The currency_conversion of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsCardProcessing
        """
        return self._currency_conversion

    @currency_conversion.setter
    def currency_conversion(self, currency_conversion):
        """
        Sets the currency_conversion of this InlineResponse2012SetupsPayments.

        :param currency_conversion: The currency_conversion of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsCardProcessing
        """

        self._currency_conversion = currency_conversion

    @property
    def tax(self):
        """
        Gets the tax of this InlineResponse2012SetupsPayments.

        :return: The tax of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsDigitalPayments
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """
        Sets the tax of this InlineResponse2012SetupsPayments.

        :param tax: The tax of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsDigitalPayments
        """

        self._tax = tax

    @property
    def customer_invoicing(self):
        """
        Gets the customer_invoicing of this InlineResponse2012SetupsPayments.

        :return: The customer_invoicing of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsDigitalPayments
        """
        return self._customer_invoicing

    @customer_invoicing.setter
    def customer_invoicing(self, customer_invoicing):
        """
        Sets the customer_invoicing of this InlineResponse2012SetupsPayments.

        :param customer_invoicing: The customer_invoicing of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsDigitalPayments
        """

        self._customer_invoicing = customer_invoicing

    @property
    def recurring_billing(self):
        """
        Gets the recurring_billing of this InlineResponse2012SetupsPayments.

        :return: The recurring_billing of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsCardProcessing
        """
        return self._recurring_billing

    @recurring_billing.setter
    def recurring_billing(self, recurring_billing):
        """
        Sets the recurring_billing of this InlineResponse2012SetupsPayments.

        :param recurring_billing: The recurring_billing of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsCardProcessing
        """

        self._recurring_billing = recurring_billing

    @property
    def cybs_ready_terminal(self):
        """
        Gets the cybs_ready_terminal of this InlineResponse2012SetupsPayments.

        :return: The cybs_ready_terminal of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsCardProcessing
        """
        return self._cybs_ready_terminal

    @cybs_ready_terminal.setter
    def cybs_ready_terminal(self, cybs_ready_terminal):
        """
        Sets the cybs_ready_terminal of this InlineResponse2012SetupsPayments.

        :param cybs_ready_terminal: The cybs_ready_terminal of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsCardProcessing
        """

        self._cybs_ready_terminal = cybs_ready_terminal

    @property
    def payment_orchestration(self):
        """
        Gets the payment_orchestration of this InlineResponse2012SetupsPayments.

        :return: The payment_orchestration of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsDigitalPayments
        """
        return self._payment_orchestration

    @payment_orchestration.setter
    def payment_orchestration(self, payment_orchestration):
        """
        Sets the payment_orchestration of this InlineResponse2012SetupsPayments.

        :param payment_orchestration: The payment_orchestration of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsDigitalPayments
        """

        self._payment_orchestration = payment_orchestration

    @property
    def payouts(self):
        """
        Gets the payouts of this InlineResponse2012SetupsPayments.

        :return: The payouts of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsCardProcessing
        """
        return self._payouts

    @payouts.setter
    def payouts(self, payouts):
        """
        Sets the payouts of this InlineResponse2012SetupsPayments.

        :param payouts: The payouts of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsCardProcessing
        """

        self._payouts = payouts

    @property
    def pay_by_link(self):
        """
        Gets the pay_by_link of this InlineResponse2012SetupsPayments.

        :return: The pay_by_link of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsDigitalPayments
        """
        return self._pay_by_link

    @pay_by_link.setter
    def pay_by_link(self, pay_by_link):
        """
        Sets the pay_by_link of this InlineResponse2012SetupsPayments.

        :param pay_by_link: The pay_by_link of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsDigitalPayments
        """

        self._pay_by_link = pay_by_link

    @property
    def unified_checkout(self):
        """
        Gets the unified_checkout of this InlineResponse2012SetupsPayments.

        :return: The unified_checkout of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsDigitalPayments
        """
        return self._unified_checkout

    @unified_checkout.setter
    def unified_checkout(self, unified_checkout):
        """
        Sets the unified_checkout of this InlineResponse2012SetupsPayments.

        :param unified_checkout: The unified_checkout of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsDigitalPayments
        """

        self._unified_checkout = unified_checkout

    @property
    def receivables_manager(self):
        """
        Gets the receivables_manager of this InlineResponse2012SetupsPayments.

        :return: The receivables_manager of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsDigitalPayments
        """
        return self._receivables_manager

    @receivables_manager.setter
    def receivables_manager(self, receivables_manager):
        """
        Sets the receivables_manager of this InlineResponse2012SetupsPayments.

        :param receivables_manager: The receivables_manager of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsDigitalPayments
        """

        self._receivables_manager = receivables_manager

    @property
    def service_fee(self):
        """
        Gets the service_fee of this InlineResponse2012SetupsPayments.

        :return: The service_fee of this InlineResponse2012SetupsPayments.
        :rtype: InlineResponse2012SetupsPaymentsCardProcessing
        """
        return self._service_fee

    @service_fee.setter
    def service_fee(self, service_fee):
        """
        Sets the service_fee of this InlineResponse2012SetupsPayments.

        :param service_fee: The service_fee of this InlineResponse2012SetupsPayments.
        :type: InlineResponse2012SetupsPaymentsCardProcessing
        """

        self._service_fee = service_fee

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
        if not isinstance(other, InlineResponse2012SetupsPayments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
