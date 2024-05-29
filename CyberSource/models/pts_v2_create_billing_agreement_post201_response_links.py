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


class PtsV2CreateBillingAgreementPost201ResponseLinks(object):
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
        '_self': 'PtsV2PaymentsPost201ResponseLinksSelf',
        'update_agreement': 'PtsV2PaymentsPost201ResponseLinksSelf',
        'revoke_agreement': 'PtsV2PaymentsPost201ResponseLinksSelf',
        'status': 'PtsV2PaymentsPost201ResponseLinksSelf'
    }

    attribute_map = {
        '_self': 'self',
        'update_agreement': 'updateAgreement',
        'revoke_agreement': 'revokeAgreement',
        'status': 'status'
    }

    def __init__(self, _self=None, update_agreement=None, revoke_agreement=None, status=None):
        """
        PtsV2CreateBillingAgreementPost201ResponseLinks - a model defined in Swagger
        """

        self.__self = None
        self._update_agreement = None
        self._revoke_agreement = None
        self._status = None

        if _self is not None:
          self._self = _self
        if update_agreement is not None:
          self.update_agreement = update_agreement
        if revoke_agreement is not None:
          self.revoke_agreement = revoke_agreement
        if status is not None:
          self.status = status

    @property
    def _self(self):
        """
        Gets the _self of this PtsV2CreateBillingAgreementPost201ResponseLinks.

        :return: The _self of this PtsV2CreateBillingAgreementPost201ResponseLinks.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this PtsV2CreateBillingAgreementPost201ResponseLinks.

        :param _self: The _self of this PtsV2CreateBillingAgreementPost201ResponseLinks.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self.__self = _self

    @property
    def update_agreement(self):
        """
        Gets the update_agreement of this PtsV2CreateBillingAgreementPost201ResponseLinks.

        :return: The update_agreement of this PtsV2CreateBillingAgreementPost201ResponseLinks.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self._update_agreement

    @update_agreement.setter
    def update_agreement(self, update_agreement):
        """
        Sets the update_agreement of this PtsV2CreateBillingAgreementPost201ResponseLinks.

        :param update_agreement: The update_agreement of this PtsV2CreateBillingAgreementPost201ResponseLinks.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self._update_agreement = update_agreement

    @property
    def revoke_agreement(self):
        """
        Gets the revoke_agreement of this PtsV2CreateBillingAgreementPost201ResponseLinks.

        :return: The revoke_agreement of this PtsV2CreateBillingAgreementPost201ResponseLinks.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self._revoke_agreement

    @revoke_agreement.setter
    def revoke_agreement(self, revoke_agreement):
        """
        Sets the revoke_agreement of this PtsV2CreateBillingAgreementPost201ResponseLinks.

        :param revoke_agreement: The revoke_agreement of this PtsV2CreateBillingAgreementPost201ResponseLinks.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self._revoke_agreement = revoke_agreement

    @property
    def status(self):
        """
        Gets the status of this PtsV2CreateBillingAgreementPost201ResponseLinks.

        :return: The status of this PtsV2CreateBillingAgreementPost201ResponseLinks.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PtsV2CreateBillingAgreementPost201ResponseLinks.

        :param status: The status of this PtsV2CreateBillingAgreementPost201ResponseLinks.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self._status = status

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
        if not isinstance(other, PtsV2CreateBillingAgreementPost201ResponseLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other