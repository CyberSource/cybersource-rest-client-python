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


class Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'company': 'str',
        'address1': 'str',
        'address2': 'str',
        'locality': 'str',
        'administrative_area': 'str',
        'postal_code': 'str',
        'country': 'str',
        'email': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'company': 'company',
        'address1': 'address1',
        'address2': 'address2',
        'locality': 'locality',
        'administrative_area': 'administrativeArea',
        'postal_code': 'postalCode',
        'country': 'country',
        'email': 'email',
        'phone_number': 'phoneNumber'
    }

    def __init__(self, first_name=None, last_name=None, company=None, address1=None, address2=None, locality=None, administrative_area=None, postal_code=None, country=None, email=None, phone_number=None):
        """
        Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo - a model defined in Swagger
        """

        self._first_name = None
        self._last_name = None
        self._company = None
        self._address1 = None
        self._address2 = None
        self._locality = None
        self._administrative_area = None
        self._postal_code = None
        self._country = None
        self._email = None
        self._phone_number = None

        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if company is not None:
          self.company = company
        if address1 is not None:
          self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if locality is not None:
          self.locality = locality
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if postal_code is not None:
          self.postal_code = postal_code
        if country is not None:
          self.country = country
        if email is not None:
          self.email = email
        if phone_number is not None:
          self.phone_number = phone_number

    @property
    def first_name(self):
        """
        Gets the first_name of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Customer's first name. This name must be the same as the name on the card. 

        :return: The first_name of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Customer's first name. This name must be the same as the name on the card. 

        :param first_name: The first_name of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Customer's last name. This name must be the same as the name on the card. 

        :return: The last_name of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Customer's last name. This name must be the same as the name on the card. 

        :param last_name: The last_name of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :type: str
        """

        self._last_name = last_name

    @property
    def company(self):
        """
        Gets the company of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Name of the customer's company. 

        :return: The company of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Name of the customer's company. 

        :param company: The company of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :type: str
        """

        self._company = company

    @property
    def address1(self):
        """
        Gets the address1 of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Payment card billing street address as it appears on the credit card issuer's records. 

        :return: The address1 of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Payment card billing street address as it appears on the credit card issuer's records. 

        :param address1: The address1 of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Additional address information. 

        :return: The address2 of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Additional address information. 

        :param address2: The address2 of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :type: str
        """

        self._address2 = address2

    @property
    def locality(self):
        """
        Gets the locality of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Payment card billing city. 

        :return: The locality of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Payment card billing city. 

        :param locality: The locality of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :type: str
        """

        self._locality = locality

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        State or province of the billing address. Use the State, Province, and Territory Codes for the United States and Canada. 

        :return: The administrative_area of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        State or province of the billing address. Use the State, Province, and Territory Codes for the United States and Canada. 

        :param administrative_area: The administrative_area of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :type: str
        """

        self._administrative_area = administrative_area

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Postal code for the billing address. The postal code must consist of 5 to 9 digits.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]  **Example** `12345-6789`  When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric]  **Example** `A1B 2C3` 

        :return: The postal_code of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Postal code for the billing address. The postal code must consist of 5 to 9 digits.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]  **Example** `12345-6789`  When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric]  **Example** `A1B 2C3` 

        :param postal_code: The postal_code of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """
        Gets the country of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Payment card billing country. Use the two-character ISO Standard Country Codes. 

        :return: The country of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Payment card billing country. Use the two-character ISO Standard Country Codes. 

        :param country: The country of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :type: str
        """

        self._country = country

    @property
    def email(self):
        """
        Gets the email of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Customer's email address, including the full domain name. 

        :return: The email of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Customer's email address, including the full domain name. 

        :param email: The email of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :type: str
        """

        self._email = email

    @property
    def phone_number(self):
        """
        Gets the phone_number of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Customer's phone number. 

        :return: The phone_number of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        Customer's phone number. 

        :param phone_number: The phone_number of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo.
        :type: str
        """

        self._phone_number = phone_number

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
        if not isinstance(other, Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other