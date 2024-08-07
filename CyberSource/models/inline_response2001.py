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


class InlineResponse2001(object):
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
        'total_count': 'int',
        'offset': 'int',
        'limit': 'int',
        'sort': 'str',
        'keys': 'list[InlineResponse2001Keys]'
    }

    attribute_map = {
        'submit_time_utc': 'submitTimeUtc',
        'total_count': 'totalCount',
        'offset': 'offset',
        'limit': 'limit',
        'sort': 'sort',
        'keys': 'keys'
    }

    def __init__(self, submit_time_utc=None, total_count=None, offset=None, limit=None, sort=None, keys=None):
        """
        InlineResponse2001 - a model defined in Swagger
        """

        self._submit_time_utc = None
        self._total_count = None
        self._offset = None
        self._limit = None
        self._sort = None
        self._keys = None

        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if total_count is not None:
          self.total_count = total_count
        if offset is not None:
          self.offset = offset
        if limit is not None:
          self.limit = limit
        if sort is not None:
          self.sort = sort
        if keys is not None:
          self.keys = keys

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this InlineResponse2001.
        Time of request in UTC. `Format: YYYY-MM-DDThh:mm:ssZ`  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :return: The submit_time_utc of this InlineResponse2001.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this InlineResponse2001.
        Time of request in UTC. `Format: YYYY-MM-DDThh:mm:ssZ`  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :param submit_time_utc: The submit_time_utc of this InlineResponse2001.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def total_count(self):
        """
        Gets the total_count of this InlineResponse2001.
        Specifies the total number of items found based on the request

        :return: The total_count of this InlineResponse2001.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this InlineResponse2001.
        Specifies the total number of items found based on the request

        :param total_count: The total_count of this InlineResponse2001.
        :type: int
        """

        self._total_count = total_count

    @property
    def offset(self):
        """
        Gets the offset of this InlineResponse2001.
        Specifies the record offset from the records are returned part of the response

        :return: The offset of this InlineResponse2001.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this InlineResponse2001.
        Specifies the record offset from the records are returned part of the response

        :param offset: The offset of this InlineResponse2001.
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """
        Gets the limit of this InlineResponse2001.
        Specifies the maximum number of records requested part of the response

        :return: The limit of this InlineResponse2001.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this InlineResponse2001.
        Specifies the maximum number of records requested part of the response

        :param limit: The limit of this InlineResponse2001.
        :type: int
        """

        self._limit = limit

    @property
    def sort(self):
        """
        Gets the sort of this InlineResponse2001.
        Specifies a comma separated list of field names based on which the result is sorted.

        :return: The sort of this InlineResponse2001.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this InlineResponse2001.
        Specifies a comma separated list of field names based on which the result is sorted.

        :param sort: The sort of this InlineResponse2001.
        :type: str
        """

        self._sort = sort

    @property
    def keys(self):
        """
        Gets the keys of this InlineResponse2001.

        :return: The keys of this InlineResponse2001.
        :rtype: list[InlineResponse2001Keys]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """
        Sets the keys of this InlineResponse2001.

        :param keys: The keys of this InlineResponse2001.
        :type: list[InlineResponse2001Keys]
        """

        self._keys = keys

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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
