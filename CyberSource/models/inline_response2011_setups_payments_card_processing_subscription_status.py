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


class InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus(object):
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
        'submit_time_utc': 'str',
        'status': 'str',
        'reason': 'str',
        'details': 'list[dict(str, str)]',
        'message': 'str'
    }

    attribute_map = {
        'submit_time_utc': 'submitTimeUtc',
        'status': 'status',
        'reason': 'reason',
        'details': 'details',
        'message': 'message'
    }

    def __init__(self, submit_time_utc=None, status=None, reason=None, details=None, message=None):
        """
        InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus - a model defined in Swagger
        """

        self._submit_time_utc = None
        self._status = None
        self._reason = None
        self._details = None
        self._message = None

        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if status is not None:
          self.status = status
        if reason is not None:
          self.reason = reason
        if details is not None:
          self.details = details
        if message is not None:
          self.message = message

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.
        Time of request in UTC. `Format: YYYY-MM-DDThh:mm:ssZ`  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :return: The submit_time_utc of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.
        Time of request in UTC. `Format: YYYY-MM-DDThh:mm:ssZ`  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :param submit_time_utc: The submit_time_utc of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def status(self):
        """
        Gets the status of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.

        :return: The status of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.

        :param status: The status of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILURE", "PARTIAL", "PENDING"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def reason(self):
        """
        Gets the reason of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.

        :return: The reason of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.

        :param reason: The reason of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.
        :type: str
        """
        allowed_values = ["DEPENDENT_PRODUCT_NOT_CONTRACTED", "DEPENDENT_FEATURE_NOT_CHOSEN", "MISSING_DATA", "INVALID_DATA", "DUPLICATE_FIELD"]
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def details(self):
        """
        Gets the details of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.

        :return: The details of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.
        :rtype: list[dict(str, str)]
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.

        :param details: The details of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.
        :type: list[dict(str, str)]
        """

        self._details = details

    @property
    def message(self):
        """
        Gets the message of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.

        :return: The message of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.

        :param message: The message of this InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, InlineResponse2011SetupsPaymentsCardProcessingSubscriptionStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other