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


class Ptsv1pushfundstransferAggregatorInformation(object):
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
        'aggregator_id': 'str',
        'name': 'str',
        'independent_sales_organization_id': 'str',
        'sub_merchant': 'Ptsv1pushfundstransferAggregatorInformationSubMerchant'
    }

    attribute_map = {
        'aggregator_id': 'aggregatorId',
        'name': 'name',
        'independent_sales_organization_id': 'independentSalesOrganizationID',
        'sub_merchant': 'subMerchant'
    }

    def __init__(self, aggregator_id=None, name=None, independent_sales_organization_id=None, sub_merchant=None):
        """
        Ptsv1pushfundstransferAggregatorInformation - a model defined in Swagger
        """

        self._aggregator_id = None
        self._name = None
        self._independent_sales_organization_id = None
        self._sub_merchant = None

        if aggregator_id is not None:
          self.aggregator_id = aggregator_id
        if name is not None:
          self.name = name
        if independent_sales_organization_id is not None:
          self.independent_sales_organization_id = independent_sales_organization_id
        if sub_merchant is not None:
          self.sub_merchant = sub_merchant

    @property
    def aggregator_id(self):
        """
        Gets the aggregator_id of this Ptsv1pushfundstransferAggregatorInformation.
        Value that identifies you as a payment aggregator. Get this value from the processor. 

        :return: The aggregator_id of this Ptsv1pushfundstransferAggregatorInformation.
        :rtype: str
        """
        return self._aggregator_id

    @aggregator_id.setter
    def aggregator_id(self, aggregator_id):
        """
        Sets the aggregator_id of this Ptsv1pushfundstransferAggregatorInformation.
        Value that identifies you as a payment aggregator. Get this value from the processor. 

        :param aggregator_id: The aggregator_id of this Ptsv1pushfundstransferAggregatorInformation.
        :type: str
        """

        self._aggregator_id = aggregator_id

    @property
    def name(self):
        """
        Gets the name of this Ptsv1pushfundstransferAggregatorInformation.
        Your payment aggregator business name. This field is conditionally required when aggregator id is present. 

        :return: The name of this Ptsv1pushfundstransferAggregatorInformation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Ptsv1pushfundstransferAggregatorInformation.
        Your payment aggregator business name. This field is conditionally required when aggregator id is present. 

        :param name: The name of this Ptsv1pushfundstransferAggregatorInformation.
        :type: str
        """

        self._name = name

    @property
    def independent_sales_organization_id(self):
        """
        Gets the independent_sales_organization_id of this Ptsv1pushfundstransferAggregatorInformation.
        Independent sales organization ID. This field is only used for Mastercard transactions submitted through PPGS. 

        :return: The independent_sales_organization_id of this Ptsv1pushfundstransferAggregatorInformation.
        :rtype: str
        """
        return self._independent_sales_organization_id

    @independent_sales_organization_id.setter
    def independent_sales_organization_id(self, independent_sales_organization_id):
        """
        Sets the independent_sales_organization_id of this Ptsv1pushfundstransferAggregatorInformation.
        Independent sales organization ID. This field is only used for Mastercard transactions submitted through PPGS. 

        :param independent_sales_organization_id: The independent_sales_organization_id of this Ptsv1pushfundstransferAggregatorInformation.
        :type: str
        """

        self._independent_sales_organization_id = independent_sales_organization_id

    @property
    def sub_merchant(self):
        """
        Gets the sub_merchant of this Ptsv1pushfundstransferAggregatorInformation.

        :return: The sub_merchant of this Ptsv1pushfundstransferAggregatorInformation.
        :rtype: Ptsv1pushfundstransferAggregatorInformationSubMerchant
        """
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, sub_merchant):
        """
        Sets the sub_merchant of this Ptsv1pushfundstransferAggregatorInformation.

        :param sub_merchant: The sub_merchant of this Ptsv1pushfundstransferAggregatorInformation.
        :type: Ptsv1pushfundstransferAggregatorInformationSubMerchant
        """

        self._sub_merchant = sub_merchant

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
        if not isinstance(other, Ptsv1pushfundstransferAggregatorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
