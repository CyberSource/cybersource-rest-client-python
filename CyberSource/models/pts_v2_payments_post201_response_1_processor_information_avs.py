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


class PtsV2PaymentsPost201Response1ProcessorInformationAvs(object):
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
        'code_raw': 'str'
    }

    attribute_map = {
        'code_raw': 'codeRaw'
    }

    def __init__(self, code_raw=None):
        """
        PtsV2PaymentsPost201Response1ProcessorInformationAvs - a model defined in Swagger
        """

        self._code_raw = None

        if code_raw is not None:
          self.code_raw = code_raw

    @property
    def code_raw(self):
        """
        Gets the code_raw of this PtsV2PaymentsPost201Response1ProcessorInformationAvs.
        AVS result code sent directly from the processor. Returned only when the processor returns this value. **Important** Do not use this field to evaluate the result of AVS. Use for debugging purposes only.  Returned by authorization service. 

        :return: The code_raw of this PtsV2PaymentsPost201Response1ProcessorInformationAvs.
        :rtype: str
        """
        return self._code_raw

    @code_raw.setter
    def code_raw(self, code_raw):
        """
        Sets the code_raw of this PtsV2PaymentsPost201Response1ProcessorInformationAvs.
        AVS result code sent directly from the processor. Returned only when the processor returns this value. **Important** Do not use this field to evaluate the result of AVS. Use for debugging purposes only.  Returned by authorization service. 

        :param code_raw: The code_raw of this PtsV2PaymentsPost201Response1ProcessorInformationAvs.
        :type: str
        """

        self._code_raw = code_raw

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
        if not isinstance(other, PtsV2PaymentsPost201Response1ProcessorInformationAvs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other