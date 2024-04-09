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


class TssV2TransactionsGet200ResponseProcessingInformationCaptureOptions(object):
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
        'total_capture_count': 'int',
        'capture_sequence_number': 'int'
    }

    attribute_map = {
        'total_capture_count': 'totalCaptureCount',
        'capture_sequence_number': 'captureSequenceNumber'
    }

    def __init__(self, total_capture_count=None, capture_sequence_number=None):
        """
        TssV2TransactionsGet200ResponseProcessingInformationCaptureOptions - a model defined in Swagger
        """

        self._total_capture_count = None
        self._capture_sequence_number = None

        if total_capture_count is not None:
          self.total_capture_count = total_capture_count
        if capture_sequence_number is not None:
          self.capture_sequence_number = capture_sequence_number

    @property
    def total_capture_count(self):
        """
        Gets the total_capture_count of this TssV2TransactionsGet200ResponseProcessingInformationCaptureOptions.
        Total number of captures when requesting multiple partial captures for one payment. Used along with `captureSequenceNumber` field to track which capture is being processed.  For example, the second of five captures would be passed to CyberSource as:   - `captureSequenceNumber = 2`, and   - `totalCaptureCount = 5` 

        :return: The total_capture_count of this TssV2TransactionsGet200ResponseProcessingInformationCaptureOptions.
        :rtype: int
        """
        return self._total_capture_count

    @total_capture_count.setter
    def total_capture_count(self, total_capture_count):
        """
        Sets the total_capture_count of this TssV2TransactionsGet200ResponseProcessingInformationCaptureOptions.
        Total number of captures when requesting multiple partial captures for one payment. Used along with `captureSequenceNumber` field to track which capture is being processed.  For example, the second of five captures would be passed to CyberSource as:   - `captureSequenceNumber = 2`, and   - `totalCaptureCount = 5` 

        :param total_capture_count: The total_capture_count of this TssV2TransactionsGet200ResponseProcessingInformationCaptureOptions.
        :type: int
        """

        self._total_capture_count = total_capture_count

    @property
    def capture_sequence_number(self):
        """
        Gets the capture_sequence_number of this TssV2TransactionsGet200ResponseProcessingInformationCaptureOptions.
        Capture number when requesting multiple partial captures for one authorization. Used along with `totalCaptureCount` to track which capture is being processed.  For example, the second of five captures would be passed to CyberSource as:   - `captureSequenceNumber_ = 2`, and   - `totalCaptureCount = 5` 

        :return: The capture_sequence_number of this TssV2TransactionsGet200ResponseProcessingInformationCaptureOptions.
        :rtype: int
        """
        return self._capture_sequence_number

    @capture_sequence_number.setter
    def capture_sequence_number(self, capture_sequence_number):
        """
        Sets the capture_sequence_number of this TssV2TransactionsGet200ResponseProcessingInformationCaptureOptions.
        Capture number when requesting multiple partial captures for one authorization. Used along with `totalCaptureCount` to track which capture is being processed.  For example, the second of five captures would be passed to CyberSource as:   - `captureSequenceNumber_ = 2`, and   - `totalCaptureCount = 5` 

        :param capture_sequence_number: The capture_sequence_number of this TssV2TransactionsGet200ResponseProcessingInformationCaptureOptions.
        :type: int
        """

        self._capture_sequence_number = capture_sequence_number

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
        if not isinstance(other, TssV2TransactionsGet200ResponseProcessingInformationCaptureOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other