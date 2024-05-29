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


class Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification(object):
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
        'id': 'str',
        'type': 'str',
        'issued_by': 'Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationIssuedBy'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'issued_by': 'issuedBy'
    }

    def __init__(self, id=None, type=None, issued_by=None):
        """
        Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification - a model defined in Swagger
        """

        self._id = None
        self._type = None
        self._issued_by = None

        if id is not None:
          self.id = id
        if type is not None:
          self.type = type
        if issued_by is not None:
          self.issued_by = issued_by

    @property
    def id(self):
        """
        Gets the id of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification.
        The value of the identification type. 

        :return: The id of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification.
        The value of the identification type. 

        :param id: The id of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification.
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """
        Gets the type of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification.
        The type of the identification.  Possible Values:   - driver license 

        :return: The type of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification.
        The type of the identification.  Possible Values:   - driver license 

        :param type: The type of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification.
        :type: str
        """

        self._type = type

    @property
    def issued_by(self):
        """
        Gets the issued_by of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification.

        :return: The issued_by of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification.
        :rtype: Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationIssuedBy
        """
        return self._issued_by

    @issued_by.setter
    def issued_by(self, issued_by):
        """
        Sets the issued_by of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification.

        :param issued_by: The issued_by of this Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification.
        :type: Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationIssuedBy
        """

        self._issued_by = issued_by

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
        if not isinstance(other, Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformationPersonalIdentification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other