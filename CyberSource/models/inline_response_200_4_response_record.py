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


class InlineResponse2004ResponseRecord(object):
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
        'response': 'str',
        'reason': 'str',
        'token': 'str',
        'instrument_identifier_id': 'str',
        'instrument_identifier_created': 'str',
        'card_number': 'str',
        'card_expiry_month': 'str',
        'card_expiry_year': 'str',
        'card_type': 'str',
        'additional_updates': 'list[InlineResponse2004ResponseRecordAdditionalUpdates]'
    }

    attribute_map = {
        'response': 'response',
        'reason': 'reason',
        'token': 'token',
        'instrument_identifier_id': 'instrumentIdentifierId',
        'instrument_identifier_created': 'instrumentIdentifierCreated',
        'card_number': 'cardNumber',
        'card_expiry_month': 'cardExpiryMonth',
        'card_expiry_year': 'cardExpiryYear',
        'card_type': 'cardType',
        'additional_updates': 'additionalUpdates'
    }

    def __init__(self, response=None, reason=None, token=None, instrument_identifier_id=None, instrument_identifier_created=None, card_number=None, card_expiry_month=None, card_expiry_year=None, card_type=None, additional_updates=None):
        """
        InlineResponse2004ResponseRecord - a model defined in Swagger
        """

        self._response = None
        self._reason = None
        self._token = None
        self._instrument_identifier_id = None
        self._instrument_identifier_created = None
        self._card_number = None
        self._card_expiry_month = None
        self._card_expiry_year = None
        self._card_type = None
        self._additional_updates = None

        if response is not None:
          self.response = response
        if reason is not None:
          self.reason = reason
        if token is not None:
          self.token = token
        if instrument_identifier_id is not None:
          self.instrument_identifier_id = instrument_identifier_id
        if instrument_identifier_created is not None:
          self.instrument_identifier_created = instrument_identifier_created
        if card_number is not None:
          self.card_number = card_number
        if card_expiry_month is not None:
          self.card_expiry_month = card_expiry_month
        if card_expiry_year is not None:
          self.card_expiry_year = card_expiry_year
        if card_type is not None:
          self.card_type = card_type
        if additional_updates is not None:
          self.additional_updates = additional_updates

    @property
    def response(self):
        """
        Gets the response of this InlineResponse2004ResponseRecord.
        Valid Values:   * NAN   * NED   * ACL   * CCH   * CUR   * NUP   * UNA   * ERR   * DEC 

        :return: The response of this InlineResponse2004ResponseRecord.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """
        Sets the response of this InlineResponse2004ResponseRecord.
        Valid Values:   * NAN   * NED   * ACL   * CCH   * CUR   * NUP   * UNA   * ERR   * DEC 

        :param response: The response of this InlineResponse2004ResponseRecord.
        :type: str
        """

        self._response = response

    @property
    def reason(self):
        """
        Gets the reason of this InlineResponse2004ResponseRecord.

        :return: The reason of this InlineResponse2004ResponseRecord.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this InlineResponse2004ResponseRecord.

        :param reason: The reason of this InlineResponse2004ResponseRecord.
        :type: str
        """

        self._reason = reason

    @property
    def token(self):
        """
        Gets the token of this InlineResponse2004ResponseRecord.

        :return: The token of this InlineResponse2004ResponseRecord.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this InlineResponse2004ResponseRecord.

        :param token: The token of this InlineResponse2004ResponseRecord.
        :type: str
        """

        self._token = token

    @property
    def instrument_identifier_id(self):
        """
        Gets the instrument_identifier_id of this InlineResponse2004ResponseRecord.

        :return: The instrument_identifier_id of this InlineResponse2004ResponseRecord.
        :rtype: str
        """
        return self._instrument_identifier_id

    @instrument_identifier_id.setter
    def instrument_identifier_id(self, instrument_identifier_id):
        """
        Sets the instrument_identifier_id of this InlineResponse2004ResponseRecord.

        :param instrument_identifier_id: The instrument_identifier_id of this InlineResponse2004ResponseRecord.
        :type: str
        """

        self._instrument_identifier_id = instrument_identifier_id

    @property
    def instrument_identifier_created(self):
        """
        Gets the instrument_identifier_created of this InlineResponse2004ResponseRecord.
        Valid Values:   * true   * false 

        :return: The instrument_identifier_created of this InlineResponse2004ResponseRecord.
        :rtype: str
        """
        return self._instrument_identifier_created

    @instrument_identifier_created.setter
    def instrument_identifier_created(self, instrument_identifier_created):
        """
        Sets the instrument_identifier_created of this InlineResponse2004ResponseRecord.
        Valid Values:   * true   * false 

        :param instrument_identifier_created: The instrument_identifier_created of this InlineResponse2004ResponseRecord.
        :type: str
        """

        self._instrument_identifier_created = instrument_identifier_created

    @property
    def card_number(self):
        """
        Gets the card_number of this InlineResponse2004ResponseRecord.

        :return: The card_number of this InlineResponse2004ResponseRecord.
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """
        Sets the card_number of this InlineResponse2004ResponseRecord.

        :param card_number: The card_number of this InlineResponse2004ResponseRecord.
        :type: str
        """

        self._card_number = card_number

    @property
    def card_expiry_month(self):
        """
        Gets the card_expiry_month of this InlineResponse2004ResponseRecord.

        :return: The card_expiry_month of this InlineResponse2004ResponseRecord.
        :rtype: str
        """
        return self._card_expiry_month

    @card_expiry_month.setter
    def card_expiry_month(self, card_expiry_month):
        """
        Sets the card_expiry_month of this InlineResponse2004ResponseRecord.

        :param card_expiry_month: The card_expiry_month of this InlineResponse2004ResponseRecord.
        :type: str
        """

        self._card_expiry_month = card_expiry_month

    @property
    def card_expiry_year(self):
        """
        Gets the card_expiry_year of this InlineResponse2004ResponseRecord.

        :return: The card_expiry_year of this InlineResponse2004ResponseRecord.
        :rtype: str
        """
        return self._card_expiry_year

    @card_expiry_year.setter
    def card_expiry_year(self, card_expiry_year):
        """
        Sets the card_expiry_year of this InlineResponse2004ResponseRecord.

        :param card_expiry_year: The card_expiry_year of this InlineResponse2004ResponseRecord.
        :type: str
        """

        self._card_expiry_year = card_expiry_year

    @property
    def card_type(self):
        """
        Gets the card_type of this InlineResponse2004ResponseRecord.

        :return: The card_type of this InlineResponse2004ResponseRecord.
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """
        Sets the card_type of this InlineResponse2004ResponseRecord.

        :param card_type: The card_type of this InlineResponse2004ResponseRecord.
        :type: str
        """

        self._card_type = card_type

    @property
    def additional_updates(self):
        """
        Gets the additional_updates of this InlineResponse2004ResponseRecord.

        :return: The additional_updates of this InlineResponse2004ResponseRecord.
        :rtype: list[InlineResponse2004ResponseRecordAdditionalUpdates]
        """
        return self._additional_updates

    @additional_updates.setter
    def additional_updates(self, additional_updates):
        """
        Sets the additional_updates of this InlineResponse2004ResponseRecord.

        :param additional_updates: The additional_updates of this InlineResponse2004ResponseRecord.
        :type: list[InlineResponse2004ResponseRecordAdditionalUpdates]
        """

        self._additional_updates = additional_updates

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
        if not isinstance(other, InlineResponse2004ResponseRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other