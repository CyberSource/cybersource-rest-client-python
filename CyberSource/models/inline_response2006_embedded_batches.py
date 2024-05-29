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


class InlineResponse2006EmbeddedBatches(object):
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
        'links': 'InlineResponse2006EmbeddedLinks',
        'batch_id': 'str',
        'batch_created_date': 'str',
        'batch_modified_date': 'str',
        'batch_source': 'str',
        'token_source': 'str',
        'merchant_reference': 'str',
        'batch_ca_endpoints': 'list[str]',
        'status': 'str',
        'totals': 'InlineResponse2006EmbeddedTotals'
    }

    attribute_map = {
        'links': '_links',
        'batch_id': 'batchId',
        'batch_created_date': 'batchCreatedDate',
        'batch_modified_date': 'batchModifiedDate',
        'batch_source': 'batchSource',
        'token_source': 'tokenSource',
        'merchant_reference': 'merchantReference',
        'batch_ca_endpoints': 'batchCaEndpoints',
        'status': 'status',
        'totals': 'totals'
    }

    def __init__(self, links=None, batch_id=None, batch_created_date=None, batch_modified_date=None, batch_source=None, token_source=None, merchant_reference=None, batch_ca_endpoints=None, status=None, totals=None):
        """
        InlineResponse2006EmbeddedBatches - a model defined in Swagger
        """

        self._links = None
        self._batch_id = None
        self._batch_created_date = None
        self._batch_modified_date = None
        self._batch_source = None
        self._token_source = None
        self._merchant_reference = None
        self._batch_ca_endpoints = None
        self._status = None
        self._totals = None

        if links is not None:
          self.links = links
        if batch_id is not None:
          self.batch_id = batch_id
        if batch_created_date is not None:
          self.batch_created_date = batch_created_date
        if batch_modified_date is not None:
          self.batch_modified_date = batch_modified_date
        if batch_source is not None:
          self.batch_source = batch_source
        if token_source is not None:
          self.token_source = token_source
        if merchant_reference is not None:
          self.merchant_reference = merchant_reference
        if batch_ca_endpoints is not None:
          self.batch_ca_endpoints = batch_ca_endpoints
        if status is not None:
          self.status = status
        if totals is not None:
          self.totals = totals

    @property
    def links(self):
        """
        Gets the links of this InlineResponse2006EmbeddedBatches.

        :return: The links of this InlineResponse2006EmbeddedBatches.
        :rtype: InlineResponse2006EmbeddedLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this InlineResponse2006EmbeddedBatches.

        :param links: The links of this InlineResponse2006EmbeddedBatches.
        :type: InlineResponse2006EmbeddedLinks
        """

        self._links = links

    @property
    def batch_id(self):
        """
        Gets the batch_id of this InlineResponse2006EmbeddedBatches.
        Unique identification number assigned to the submitted request.

        :return: The batch_id of this InlineResponse2006EmbeddedBatches.
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """
        Sets the batch_id of this InlineResponse2006EmbeddedBatches.
        Unique identification number assigned to the submitted request.

        :param batch_id: The batch_id of this InlineResponse2006EmbeddedBatches.
        :type: str
        """

        self._batch_id = batch_id

    @property
    def batch_created_date(self):
        """
        Gets the batch_created_date of this InlineResponse2006EmbeddedBatches.
        ISO-8601 format: yyyy-MM-ddTHH:mm:ssZ

        :return: The batch_created_date of this InlineResponse2006EmbeddedBatches.
        :rtype: str
        """
        return self._batch_created_date

    @batch_created_date.setter
    def batch_created_date(self, batch_created_date):
        """
        Sets the batch_created_date of this InlineResponse2006EmbeddedBatches.
        ISO-8601 format: yyyy-MM-ddTHH:mm:ssZ

        :param batch_created_date: The batch_created_date of this InlineResponse2006EmbeddedBatches.
        :type: str
        """

        self._batch_created_date = batch_created_date

    @property
    def batch_modified_date(self):
        """
        Gets the batch_modified_date of this InlineResponse2006EmbeddedBatches.
        ISO-8601 format: yyyy-MM-ddTHH:mm:ssZ

        :return: The batch_modified_date of this InlineResponse2006EmbeddedBatches.
        :rtype: str
        """
        return self._batch_modified_date

    @batch_modified_date.setter
    def batch_modified_date(self, batch_modified_date):
        """
        Sets the batch_modified_date of this InlineResponse2006EmbeddedBatches.
        ISO-8601 format: yyyy-MM-ddTHH:mm:ssZ

        :param batch_modified_date: The batch_modified_date of this InlineResponse2006EmbeddedBatches.
        :type: str
        """

        self._batch_modified_date = batch_modified_date

    @property
    def batch_source(self):
        """
        Gets the batch_source of this InlineResponse2006EmbeddedBatches.
        Valid Values:   * SCHEDULER   * TOKEN_API   * CREDIT_CARD_FILE_UPLOAD   * AMEX_REGSITRY   * AMEX_REGISTRY_API   * AMEX_REGISTRY_API_SYNC   * AMEX_MAINTENANCE 

        :return: The batch_source of this InlineResponse2006EmbeddedBatches.
        :rtype: str
        """
        return self._batch_source

    @batch_source.setter
    def batch_source(self, batch_source):
        """
        Sets the batch_source of this InlineResponse2006EmbeddedBatches.
        Valid Values:   * SCHEDULER   * TOKEN_API   * CREDIT_CARD_FILE_UPLOAD   * AMEX_REGSITRY   * AMEX_REGISTRY_API   * AMEX_REGISTRY_API_SYNC   * AMEX_MAINTENANCE 

        :param batch_source: The batch_source of this InlineResponse2006EmbeddedBatches.
        :type: str
        """

        self._batch_source = batch_source

    @property
    def token_source(self):
        """
        Gets the token_source of this InlineResponse2006EmbeddedBatches.
        Valid Values:   * SECURE_STORAGE   * TMS   * CYBERSOURCE 

        :return: The token_source of this InlineResponse2006EmbeddedBatches.
        :rtype: str
        """
        return self._token_source

    @token_source.setter
    def token_source(self, token_source):
        """
        Sets the token_source of this InlineResponse2006EmbeddedBatches.
        Valid Values:   * SECURE_STORAGE   * TMS   * CYBERSOURCE 

        :param token_source: The token_source of this InlineResponse2006EmbeddedBatches.
        :type: str
        """

        self._token_source = token_source

    @property
    def merchant_reference(self):
        """
        Gets the merchant_reference of this InlineResponse2006EmbeddedBatches.
        Reference used by merchant to identify batch.

        :return: The merchant_reference of this InlineResponse2006EmbeddedBatches.
        :rtype: str
        """
        return self._merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, merchant_reference):
        """
        Sets the merchant_reference of this InlineResponse2006EmbeddedBatches.
        Reference used by merchant to identify batch.

        :param merchant_reference: The merchant_reference of this InlineResponse2006EmbeddedBatches.
        :type: str
        """

        self._merchant_reference = merchant_reference

    @property
    def batch_ca_endpoints(self):
        """
        Gets the batch_ca_endpoints of this InlineResponse2006EmbeddedBatches.
        Valid Values:   * VISA   * MASTERCARD   * AMEX 

        :return: The batch_ca_endpoints of this InlineResponse2006EmbeddedBatches.
        :rtype: list[str]
        """
        return self._batch_ca_endpoints

    @batch_ca_endpoints.setter
    def batch_ca_endpoints(self, batch_ca_endpoints):
        """
        Sets the batch_ca_endpoints of this InlineResponse2006EmbeddedBatches.
        Valid Values:   * VISA   * MASTERCARD   * AMEX 

        :param batch_ca_endpoints: The batch_ca_endpoints of this InlineResponse2006EmbeddedBatches.
        :type: list[str]
        """

        self._batch_ca_endpoints = batch_ca_endpoints

    @property
    def status(self):
        """
        Gets the status of this InlineResponse2006EmbeddedBatches.
        Valid Values:   * REJECTED   * RECEIVED   * VALIDATED   * DECLINED   * PROCESSING   * COMPLETE 

        :return: The status of this InlineResponse2006EmbeddedBatches.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InlineResponse2006EmbeddedBatches.
        Valid Values:   * REJECTED   * RECEIVED   * VALIDATED   * DECLINED   * PROCESSING   * COMPLETE 

        :param status: The status of this InlineResponse2006EmbeddedBatches.
        :type: str
        """

        self._status = status

    @property
    def totals(self):
        """
        Gets the totals of this InlineResponse2006EmbeddedBatches.

        :return: The totals of this InlineResponse2006EmbeddedBatches.
        :rtype: InlineResponse2006EmbeddedTotals
        """
        return self._totals

    @totals.setter
    def totals(self, totals):
        """
        Sets the totals of this InlineResponse2006EmbeddedBatches.

        :param totals: The totals of this InlineResponse2006EmbeddedBatches.
        :type: InlineResponse2006EmbeddedTotals
        """

        self._totals = totals

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
        if not isinstance(other, InlineResponse2006EmbeddedBatches):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other