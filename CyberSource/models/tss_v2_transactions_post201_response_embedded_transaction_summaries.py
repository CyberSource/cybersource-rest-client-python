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


class TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries(object):
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
        'submit_time_utc': 'str',
        'merchant_id': 'str',
        'status': 'str',
        'application_information': 'TssV2TransactionsPost201ResponseEmbeddedApplicationInformation',
        'buyer_information': 'PtsV2CreateOrderPost201ResponseBuyerInformation',
        'client_reference_information': 'TssV2TransactionsPost201ResponseEmbeddedClientReferenceInformation',
        'consumer_authentication_information': 'TssV2TransactionsPost201ResponseEmbeddedConsumerAuthenticationInformation',
        'device_information': 'Riskv1authenticationresultsDeviceInformation',
        'error_information': 'TssV2TransactionsPost201ResponseEmbeddedErrorInformation',
        'fraud_marking_information': 'TssV2TransactionsGet200ResponseFraudMarkingInformation',
        'merchant_defined_information': 'list[Ptsv2paymentsMerchantDefinedInformation]',
        'merchant_information': 'TssV2TransactionsPost201ResponseEmbeddedMerchantInformation',
        'order_information': 'TssV2TransactionsPost201ResponseEmbeddedOrderInformation',
        'payment_information': 'TssV2TransactionsPost201ResponseEmbeddedPaymentInformation',
        'processing_information': 'TssV2TransactionsPost201ResponseEmbeddedProcessingInformation',
        'processor_information': 'TssV2TransactionsPost201ResponseEmbeddedProcessorInformation',
        'point_of_sale_information': 'TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation',
        'risk_information': 'TssV2TransactionsPost201ResponseEmbeddedRiskInformation',
        'links': 'TssV2TransactionsPost201ResponseEmbeddedLinks'
    }

    attribute_map = {
        'id': 'id',
        'submit_time_utc': 'submitTimeUtc',
        'merchant_id': 'merchantId',
        'status': 'status',
        'application_information': 'applicationInformation',
        'buyer_information': 'buyerInformation',
        'client_reference_information': 'clientReferenceInformation',
        'consumer_authentication_information': 'consumerAuthenticationInformation',
        'device_information': 'deviceInformation',
        'error_information': 'errorInformation',
        'fraud_marking_information': 'fraudMarkingInformation',
        'merchant_defined_information': 'merchantDefinedInformation',
        'merchant_information': 'merchantInformation',
        'order_information': 'orderInformation',
        'payment_information': 'paymentInformation',
        'processing_information': 'processingInformation',
        'processor_information': 'processorInformation',
        'point_of_sale_information': 'pointOfSaleInformation',
        'risk_information': 'riskInformation',
        'links': '_links'
    }

    def __init__(self, id=None, submit_time_utc=None, merchant_id=None, status=None, application_information=None, buyer_information=None, client_reference_information=None, consumer_authentication_information=None, device_information=None, error_information=None, fraud_marking_information=None, merchant_defined_information=None, merchant_information=None, order_information=None, payment_information=None, processing_information=None, processor_information=None, point_of_sale_information=None, risk_information=None, links=None):
        """
        TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries - a model defined in Swagger
        """

        self._id = None
        self._submit_time_utc = None
        self._merchant_id = None
        self._status = None
        self._application_information = None
        self._buyer_information = None
        self._client_reference_information = None
        self._consumer_authentication_information = None
        self._device_information = None
        self._error_information = None
        self._fraud_marking_information = None
        self._merchant_defined_information = None
        self._merchant_information = None
        self._order_information = None
        self._payment_information = None
        self._processing_information = None
        self._processor_information = None
        self._point_of_sale_information = None
        self._risk_information = None
        self._links = None

        if id is not None:
          self.id = id
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if merchant_id is not None:
          self.merchant_id = merchant_id
        if status is not None:
          self.status = status
        if application_information is not None:
          self.application_information = application_information
        if buyer_information is not None:
          self.buyer_information = buyer_information
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if consumer_authentication_information is not None:
          self.consumer_authentication_information = consumer_authentication_information
        if device_information is not None:
          self.device_information = device_information
        if error_information is not None:
          self.error_information = error_information
        if fraud_marking_information is not None:
          self.fraud_marking_information = fraud_marking_information
        if merchant_defined_information is not None:
          self.merchant_defined_information = merchant_defined_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if order_information is not None:
          self.order_information = order_information
        if payment_information is not None:
          self.payment_information = payment_information
        if processing_information is not None:
          self.processing_information = processing_information
        if processor_information is not None:
          self.processor_information = processor_information
        if point_of_sale_information is not None:
          self.point_of_sale_information = point_of_sale_information
        if risk_information is not None:
          self.risk_information = risk_information
        if links is not None:
          self.links = links

    @property
    def id(self):
        """
        Gets the id of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :return: The id of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :param id: The id of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: str
        """

        self._id = id

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :return: The submit_time_utc of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :param submit_time_utc: The submit_time_utc of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        Your CyberSource merchant ID.

        :return: The merchant_id of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        Your CyberSource merchant ID.

        :param merchant_id: The merchant_id of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def status(self):
        """
        Gets the status of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        The status of the submitted transaction. Note: This field may not be returned for all transactions. 

        :return: The status of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        The status of the submitted transaction. Note: This field may not be returned for all transactions. 

        :param status: The status of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: str
        """

        self._status = status

    @property
    def application_information(self):
        """
        Gets the application_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The application_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedApplicationInformation
        """
        return self._application_information

    @application_information.setter
    def application_information(self, application_information):
        """
        Sets the application_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param application_information: The application_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: TssV2TransactionsPost201ResponseEmbeddedApplicationInformation
        """

        self._application_information = application_information

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The buyer_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: PtsV2CreateOrderPost201ResponseBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param buyer_information: The buyer_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: PtsV2CreateOrderPost201ResponseBuyerInformation
        """

        self._buyer_information = buyer_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The client_reference_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param client_reference_information: The client_reference_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: TssV2TransactionsPost201ResponseEmbeddedClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def consumer_authentication_information(self):
        """
        Gets the consumer_authentication_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The consumer_authentication_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedConsumerAuthenticationInformation
        """
        return self._consumer_authentication_information

    @consumer_authentication_information.setter
    def consumer_authentication_information(self, consumer_authentication_information):
        """
        Sets the consumer_authentication_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param consumer_authentication_information: The consumer_authentication_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: TssV2TransactionsPost201ResponseEmbeddedConsumerAuthenticationInformation
        """

        self._consumer_authentication_information = consumer_authentication_information

    @property
    def device_information(self):
        """
        Gets the device_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The device_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: Riskv1authenticationresultsDeviceInformation
        """
        return self._device_information

    @device_information.setter
    def device_information(self, device_information):
        """
        Sets the device_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param device_information: The device_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: Riskv1authenticationresultsDeviceInformation
        """

        self._device_information = device_information

    @property
    def error_information(self):
        """
        Gets the error_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The error_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedErrorInformation
        """
        return self._error_information

    @error_information.setter
    def error_information(self, error_information):
        """
        Sets the error_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param error_information: The error_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: TssV2TransactionsPost201ResponseEmbeddedErrorInformation
        """

        self._error_information = error_information

    @property
    def fraud_marking_information(self):
        """
        Gets the fraud_marking_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The fraud_marking_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: TssV2TransactionsGet200ResponseFraudMarkingInformation
        """
        return self._fraud_marking_information

    @fraud_marking_information.setter
    def fraud_marking_information(self, fraud_marking_information):
        """
        Sets the fraud_marking_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param fraud_marking_information: The fraud_marking_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: TssV2TransactionsGet200ResponseFraudMarkingInformation
        """

        self._fraud_marking_information = fraud_marking_information

    @property
    def merchant_defined_information(self):
        """
        Gets the merchant_defined_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        The object containing the custom data that the merchant defines. 

        :return: The merchant_defined_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: list[Ptsv2paymentsMerchantDefinedInformation]
        """
        return self._merchant_defined_information

    @merchant_defined_information.setter
    def merchant_defined_information(self, merchant_defined_information):
        """
        Sets the merchant_defined_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        The object containing the custom data that the merchant defines. 

        :param merchant_defined_information: The merchant_defined_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: list[Ptsv2paymentsMerchantDefinedInformation]
        """

        self._merchant_defined_information = merchant_defined_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The merchant_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param merchant_information: The merchant_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: TssV2TransactionsPost201ResponseEmbeddedMerchantInformation
        """

        self._merchant_information = merchant_information

    @property
    def order_information(self):
        """
        Gets the order_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The order_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param order_information: The order_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: TssV2TransactionsPost201ResponseEmbeddedOrderInformation
        """

        self._order_information = order_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The payment_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedPaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param payment_information: The payment_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: TssV2TransactionsPost201ResponseEmbeddedPaymentInformation
        """

        self._payment_information = payment_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The processing_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param processing_information: The processing_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: TssV2TransactionsPost201ResponseEmbeddedProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def processor_information(self):
        """
        Gets the processor_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The processor_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedProcessorInformation
        """
        return self._processor_information

    @processor_information.setter
    def processor_information(self, processor_information):
        """
        Sets the processor_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param processor_information: The processor_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: TssV2TransactionsPost201ResponseEmbeddedProcessorInformation
        """

        self._processor_information = processor_information

    @property
    def point_of_sale_information(self):
        """
        Gets the point_of_sale_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The point_of_sale_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation
        """
        return self._point_of_sale_information

    @point_of_sale_information.setter
    def point_of_sale_information(self, point_of_sale_information):
        """
        Sets the point_of_sale_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param point_of_sale_information: The point_of_sale_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation
        """

        self._point_of_sale_information = point_of_sale_information

    @property
    def risk_information(self):
        """
        Gets the risk_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The risk_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedRiskInformation
        """
        return self._risk_information

    @risk_information.setter
    def risk_information(self, risk_information):
        """
        Sets the risk_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param risk_information: The risk_information of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: TssV2TransactionsPost201ResponseEmbeddedRiskInformation
        """

        self._risk_information = risk_information

    @property
    def links(self):
        """
        Gets the links of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :return: The links of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.

        :param links: The links of this TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries.
        :type: TssV2TransactionsPost201ResponseEmbeddedLinks
        """

        self._links = links

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
        if not isinstance(other, TssV2TransactionsPost201ResponseEmbeddedTransactionSummaries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
