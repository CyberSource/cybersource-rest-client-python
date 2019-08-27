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


class CreateInstrumentIdentifierRequest(object):
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
        'type': 'str',
        'card': 'Tmsv1instrumentidentifiersCard',
        'bank_account': 'Tmsv1instrumentidentifiersBankAccount',
        'bill_to': 'Tmsv1instrumentidentifiersBillTo'
    }

    attribute_map = {
        'type': 'type',
        'card': 'card',
        'bank_account': 'BankAccount',
        'bill_to': 'billTo'
    }

    def __init__(self, type=None, card=None, bank_account=None, bill_to=None):
        """
        CreateInstrumentIdentifierRequest - a model defined in Swagger
        """

        self._type = None
        self._card = None
        self._bank_account = None
        self._bill_to = None

        if type is not None:
          self.type = type
        if card is not None:
          self.card = card
        if bank_account is not None:
          self.bank_account = bank_account
        if bill_to is not None:
          self.bill_to = bill_to

    @property
    def type(self):
        """
        Gets the type of this CreateInstrumentIdentifierRequest.
        Type of Card

        :return: The type of this CreateInstrumentIdentifierRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateInstrumentIdentifierRequest.
        Type of Card

        :param type: The type of this CreateInstrumentIdentifierRequest.
        :type: str
        """

        self._type = type

    @property
    def card(self):
        """
        Gets the card of this CreateInstrumentIdentifierRequest.

        :return: The card of this CreateInstrumentIdentifierRequest.
        :rtype: Tmsv1instrumentidentifiersCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this CreateInstrumentIdentifierRequest.

        :param card: The card of this CreateInstrumentIdentifierRequest.
        :type: Tmsv1instrumentidentifiersCard
        """

        self._card = card

    @property
    def bank_account(self):
        """
        Gets the bank_account of this CreateInstrumentIdentifierRequest.

        :return: The bank_account of this CreateInstrumentIdentifierRequest.
        :rtype: Tmsv1instrumentidentifiersBankAccount
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """
        Sets the bank_account of this CreateInstrumentIdentifierRequest.

        :param bank_account: The bank_account of this CreateInstrumentIdentifierRequest.
        :type: Tmsv1instrumentidentifiersBankAccount
        """

        self._bank_account = bank_account

    @property
    def bill_to(self):
        """
        Gets the bill_to of this CreateInstrumentIdentifierRequest.

        :return: The bill_to of this CreateInstrumentIdentifierRequest.
        :rtype: Tmsv1instrumentidentifiersBillTo
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """
        Sets the bill_to of this CreateInstrumentIdentifierRequest.

        :param bill_to: The bill_to of this CreateInstrumentIdentifierRequest.
        :type: Tmsv1instrumentidentifiersBillTo
        """

        self._bill_to = bill_to

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
        if not isinstance(other, CreateInstrumentIdentifierRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other