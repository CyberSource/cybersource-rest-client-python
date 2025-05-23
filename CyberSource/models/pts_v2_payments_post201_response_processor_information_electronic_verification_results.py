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


class PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults(object):
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
        'code': 'str',
        'code_raw': 'str',
        'email': 'str',
        'email_raw': 'str',
        'phone_number': 'str',
        'phone_number_raw': 'str',
        'postal_code': 'str',
        'postal_code_raw': 'str',
        'street': 'str',
        'street_raw': 'str',
        'name': 'str',
        'name_raw': 'str',
        'first_name_raw': 'str',
        'first_name': 'str',
        'middle_name_raw': 'str',
        'middle_name': 'str',
        'last_name_raw': 'str',
        'last_name': 'str'
    }

    attribute_map = {
        'code': 'code',
        'code_raw': 'codeRaw',
        'email': 'email',
        'email_raw': 'emailRaw',
        'phone_number': 'phoneNumber',
        'phone_number_raw': 'phoneNumberRaw',
        'postal_code': 'postalCode',
        'postal_code_raw': 'postalCodeRaw',
        'street': 'street',
        'street_raw': 'streetRaw',
        'name': 'name',
        'name_raw': 'nameRaw',
        'first_name_raw': 'firstNameRaw',
        'first_name': 'firstName',
        'middle_name_raw': 'middleNameRaw',
        'middle_name': 'middleName',
        'last_name_raw': 'lastNameRaw',
        'last_name': 'lastName'
    }

    def __init__(self, code=None, code_raw=None, email=None, email_raw=None, phone_number=None, phone_number_raw=None, postal_code=None, postal_code_raw=None, street=None, street_raw=None, name=None, name_raw=None, first_name_raw=None, first_name=None, middle_name_raw=None, middle_name=None, last_name_raw=None, last_name=None):
        """
        PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults - a model defined in Swagger
        """

        self._code = None
        self._code_raw = None
        self._email = None
        self._email_raw = None
        self._phone_number = None
        self._phone_number_raw = None
        self._postal_code = None
        self._postal_code_raw = None
        self._street = None
        self._street_raw = None
        self._name = None
        self._name_raw = None
        self._first_name_raw = None
        self._first_name = None
        self._middle_name_raw = None
        self._middle_name = None
        self._last_name_raw = None
        self._last_name = None

        if code is not None:
          self.code = code
        if code_raw is not None:
          self.code_raw = code_raw
        if email is not None:
          self.email = email
        if email_raw is not None:
          self.email_raw = email_raw
        if phone_number is not None:
          self.phone_number = phone_number
        if phone_number_raw is not None:
          self.phone_number_raw = phone_number_raw
        if postal_code is not None:
          self.postal_code = postal_code
        if postal_code_raw is not None:
          self.postal_code_raw = postal_code_raw
        if street is not None:
          self.street = street
        if street_raw is not None:
          self.street_raw = street_raw
        if name is not None:
          self.name = name
        if name_raw is not None:
          self.name_raw = name_raw
        if first_name_raw is not None:
          self.first_name_raw = first_name_raw
        if first_name is not None:
          self.first_name = first_name
        if middle_name_raw is not None:
          self.middle_name_raw = middle_name_raw
        if middle_name is not None:
          self.middle_name = middle_name
        if last_name_raw is not None:
          self.last_name_raw = last_name_raw
        if last_name is not None:
          self.last_name = last_name

    @property
    def code(self):
        """
        Gets the code of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Mapped Electronic Verification response code for the customer's name. 

        :return: The code of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Mapped Electronic Verification response code for the customer's name. 

        :param code: The code of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._code = code

    @property
    def code_raw(self):
        """
        Gets the code_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Raw Electronic Verification response code from the processor for the customer's last name

        :return: The code_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._code_raw

    @code_raw.setter
    def code_raw(self, code_raw):
        """
        Sets the code_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Raw Electronic Verification response code from the processor for the customer's last name

        :param code_raw: The code_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._code_raw = code_raw

    @property
    def email(self):
        """
        Gets the email of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Mapped Electronic Verification response code for the customer's email address. 

        :return: The email of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Mapped Electronic Verification response code for the customer's email address. 

        :param email: The email of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._email = email

    @property
    def email_raw(self):
        """
        Gets the email_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Raw Electronic Verification response code from the processor for the customer's email address.

        :return: The email_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._email_raw

    @email_raw.setter
    def email_raw(self, email_raw):
        """
        Sets the email_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Raw Electronic Verification response code from the processor for the customer's email address.

        :param email_raw: The email_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._email_raw = email_raw

    @property
    def phone_number(self):
        """
        Gets the phone_number of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Mapped Electronic Verification response code for the customer's phone number. 

        :return: The phone_number of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Mapped Electronic Verification response code for the customer's phone number. 

        :param phone_number: The phone_number of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def phone_number_raw(self):
        """
        Gets the phone_number_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Raw Electronic Verification response code from the processor for the customer's phone number.

        :return: The phone_number_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._phone_number_raw

    @phone_number_raw.setter
    def phone_number_raw(self, phone_number_raw):
        """
        Sets the phone_number_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Raw Electronic Verification response code from the processor for the customer's phone number.

        :param phone_number_raw: The phone_number_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._phone_number_raw = phone_number_raw

    @property
    def postal_code(self):
        """
        Gets the postal_code of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Mapped Electronic Verification response code for the customer's postal code. 

        :return: The postal_code of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Mapped Electronic Verification response code for the customer's postal code. 

        :param postal_code: The postal_code of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def postal_code_raw(self):
        """
        Gets the postal_code_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Raw Electronic Verification response code from the processor for the customer's postal code.

        :return: The postal_code_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._postal_code_raw

    @postal_code_raw.setter
    def postal_code_raw(self, postal_code_raw):
        """
        Sets the postal_code_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Raw Electronic Verification response code from the processor for the customer's postal code.

        :param postal_code_raw: The postal_code_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._postal_code_raw = postal_code_raw

    @property
    def street(self):
        """
        Gets the street of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Mapped Electronic Verification response code for the customer's street address. 

        :return: The street of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """
        Sets the street of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Mapped Electronic Verification response code for the customer's street address. 

        :param street: The street of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._street = street

    @property
    def street_raw(self):
        """
        Gets the street_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Raw Electronic Verification response code from the processor for the customer's street address.

        :return: The street_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._street_raw

    @street_raw.setter
    def street_raw(self, street_raw):
        """
        Sets the street_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        Raw Electronic Verification response code from the processor for the customer's street address.

        :param street_raw: The street_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._street_raw = street_raw

    @property
    def name(self):
        """
        Gets the name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Mapped Electronic Verification response code for the customer's name.  Valid values :  'Y'   Yes, the data Matches 'N'   No Match 'O'   Partial Match 

        :return: The name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Mapped Electronic Verification response code for the customer's name.  Valid values :  'Y'   Yes, the data Matches 'N'   No Match 'O'   Partial Match 

        :param name: The name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._name = name

    @property
    def name_raw(self):
        """
        Gets the name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Raw Electronic Verification response code from the processor for the customer's name.  Valid values :  '01'     Match '50'     Partial Match '99'     No Match 

        :return: The name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._name_raw

    @name_raw.setter
    def name_raw(self, name_raw):
        """
        Sets the name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Raw Electronic Verification response code from the processor for the customer's name.  Valid values :  '01'     Match '50'     Partial Match '99'     No Match 

        :param name_raw: The name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._name_raw = name_raw

    @property
    def first_name_raw(self):
        """
        Gets the first_name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Raw electronic verification response code from the processor for the customer's first name.  Valid values :  '01'     Match '50'     Partial Match '99'     No Match 

        :return: The first_name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._first_name_raw

    @first_name_raw.setter
    def first_name_raw(self, first_name_raw):
        """
        Sets the first_name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Raw electronic verification response code from the processor for the customer's first name.  Valid values :  '01'     Match '50'     Partial Match '99'     No Match 

        :param first_name_raw: The first_name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._first_name_raw = first_name_raw

    @property
    def first_name(self):
        """
        Gets the first_name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Mapped electronic verification response code from the processor for the customer's first name.  Valid values :  'Y'   Yes, the data Matches 'N'   No Match 'O'   Partial Match 

        :return: The first_name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Mapped electronic verification response code from the processor for the customer's first name.  Valid values :  'Y'   Yes, the data Matches 'N'   No Match 'O'   Partial Match 

        :param first_name: The first_name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name_raw(self):
        """
        Gets the middle_name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Raw electronic verification response code from the processor for the customer's middle name.  Valid values :  '01'     Match '50'     Partial Match '99'     No Match 

        :return: The middle_name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._middle_name_raw

    @middle_name_raw.setter
    def middle_name_raw(self, middle_name_raw):
        """
        Sets the middle_name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Raw electronic verification response code from the processor for the customer's middle name.  Valid values :  '01'     Match '50'     Partial Match '99'     No Match 

        :param middle_name_raw: The middle_name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._middle_name_raw = middle_name_raw

    @property
    def middle_name(self):
        """
        Gets the middle_name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Mapped electronic verification response code from the processor for the customer's middle name.  Valid values :  'Y'   Yes, the data Matches 'N'   No Match 'O'   Partial Match 

        :return: The middle_name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Mapped electronic verification response code from the processor for the customer's middle name.  Valid values :  'Y'   Yes, the data Matches 'N'   No Match 'O'   Partial Match 

        :param middle_name: The middle_name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name_raw(self):
        """
        Gets the last_name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Raw electronic verification response code from the processor for the customer's last name.  Valid values :  '01'     Match '50'     Partial Match '99'     No Match 

        :return: The last_name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._last_name_raw

    @last_name_raw.setter
    def last_name_raw(self, last_name_raw):
        """
        Sets the last_name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Raw electronic verification response code from the processor for the customer's last name.  Valid values :  '01'     Match '50'     Partial Match '99'     No Match 

        :param last_name_raw: The last_name_raw of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._last_name_raw = last_name_raw

    @property
    def last_name(self):
        """
        Gets the last_name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Mapped electronic verification response code from the processor for the customer's last name.  Valid values :  'Y'   Yes, the data Matches 'N'   No Match 'O'   Partial Match 

        :return: The last_name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        #### Visa Platform Connect Mapped electronic verification response code from the processor for the customer's last name.  Valid values :  'Y'   Yes, the data Matches 'N'   No Match 'O'   Partial Match 

        :param last_name: The last_name of this PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults.
        :type: str
        """

        self._last_name = last_name

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseProcessorInformationElectronicVerificationResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
