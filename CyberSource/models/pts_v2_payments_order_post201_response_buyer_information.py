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


class PtsV2PaymentsOrderPost201ResponseBuyerInformation(object):
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
        'personal_identification': 'list[PtsV2PaymentsOrderPost201ResponseBuyerInformationPersonalIdentification]'
    }

    attribute_map = {
        'personal_identification': 'personalIdentification'
    }

    def __init__(self, personal_identification=None):
        """
        PtsV2PaymentsOrderPost201ResponseBuyerInformation - a model defined in Swagger
        """

        self._personal_identification = None

        if personal_identification is not None:
          self.personal_identification = personal_identification

    @property
    def personal_identification(self):
        """
        Gets the personal_identification of this PtsV2PaymentsOrderPost201ResponseBuyerInformation.

        :return: The personal_identification of this PtsV2PaymentsOrderPost201ResponseBuyerInformation.
        :rtype: list[PtsV2PaymentsOrderPost201ResponseBuyerInformationPersonalIdentification]
        """
        return self._personal_identification

    @personal_identification.setter
    def personal_identification(self, personal_identification):
        """
        Sets the personal_identification of this PtsV2PaymentsOrderPost201ResponseBuyerInformation.

        :param personal_identification: The personal_identification of this PtsV2PaymentsOrderPost201ResponseBuyerInformation.
        :type: list[PtsV2PaymentsOrderPost201ResponseBuyerInformationPersonalIdentification]
        """

        self._personal_identification = personal_identification

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
        if not isinstance(other, PtsV2PaymentsOrderPost201ResponseBuyerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other