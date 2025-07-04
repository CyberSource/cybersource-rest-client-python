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


class InlineResponse20010Records(object):
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
        'source_record': 'InlineResponse20010SourceRecord',
        'response_record': 'InlineResponse20010ResponseRecord'
    }

    attribute_map = {
        'id': 'id',
        'source_record': 'sourceRecord',
        'response_record': 'responseRecord'
    }

    def __init__(self, id=None, source_record=None, response_record=None):
        """
        InlineResponse20010Records - a model defined in Swagger
        """

        self._id = None
        self._source_record = None
        self._response_record = None

        if id is not None:
          self.id = id
        if source_record is not None:
          self.source_record = source_record
        if response_record is not None:
          self.response_record = response_record

    @property
    def id(self):
        """
        Gets the id of this InlineResponse20010Records.

        :return: The id of this InlineResponse20010Records.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InlineResponse20010Records.

        :param id: The id of this InlineResponse20010Records.
        :type: str
        """

        self._id = id

    @property
    def source_record(self):
        """
        Gets the source_record of this InlineResponse20010Records.

        :return: The source_record of this InlineResponse20010Records.
        :rtype: InlineResponse20010SourceRecord
        """
        return self._source_record

    @source_record.setter
    def source_record(self, source_record):
        """
        Sets the source_record of this InlineResponse20010Records.

        :param source_record: The source_record of this InlineResponse20010Records.
        :type: InlineResponse20010SourceRecord
        """

        self._source_record = source_record

    @property
    def response_record(self):
        """
        Gets the response_record of this InlineResponse20010Records.

        :return: The response_record of this InlineResponse20010Records.
        :rtype: InlineResponse20010ResponseRecord
        """
        return self._response_record

    @response_record.setter
    def response_record(self, response_record):
        """
        Sets the response_record of this InlineResponse20010Records.

        :param response_record: The response_record of this InlineResponse20010Records.
        :type: InlineResponse20010ResponseRecord
        """

        self._response_record = response_record

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
        if not isinstance(other, InlineResponse20010Records):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
