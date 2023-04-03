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


class InlineResponse2011Links(object):
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
        'update': 'PtsV2PaymentsPost201ResponseLinksSelf',
        'cancel': 'PtsV2PaymentsPost201ResponseLinksSelf',
        'suspend': 'PtsV2PaymentsPost201ResponseLinksSelf',
        'activate': 'PtsV2PaymentsPost201ResponseLinksSelf'
    }

    attribute_map = {
        '_self': 'self',
        'update': 'update',
        'cancel': 'cancel',
        'suspend': 'suspend',
        'activate': 'activate'
    }

    def __init__(self, _self=None, update=None, cancel=None, suspend=None, activate=None):
        """
        InlineResponse2011Links - a model defined in Swagger
        """

        self.__self = None
        self._update = None
        self._cancel = None
        self._suspend = None
        self._activate = None

        if _self is not None:
          self._self = _self
        if update is not None:
          self.update = update
        if cancel is not None:
          self.cancel = cancel
        if suspend is not None:
          self.suspend = suspend
        if activate is not None:
          self.activate = activate

    @property
    def _self(self):
        """
        Gets the _self of this InlineResponse2011Links.

        :return: The _self of this InlineResponse2011Links.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this InlineResponse2011Links.

        :param _self: The _self of this InlineResponse2011Links.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self.__self = _self

    @property
    def update(self):
        """
        Gets the update of this InlineResponse2011Links.

        :return: The update of this InlineResponse2011Links.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self._update

    @update.setter
    def update(self, update):
        """
        Sets the update of this InlineResponse2011Links.

        :param update: The update of this InlineResponse2011Links.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self._update = update

    @property
    def cancel(self):
        """
        Gets the cancel of this InlineResponse2011Links.

        :return: The cancel of this InlineResponse2011Links.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self._cancel

    @cancel.setter
    def cancel(self, cancel):
        """
        Sets the cancel of this InlineResponse2011Links.

        :param cancel: The cancel of this InlineResponse2011Links.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self._cancel = cancel

    @property
    def suspend(self):
        """
        Gets the suspend of this InlineResponse2011Links.

        :return: The suspend of this InlineResponse2011Links.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """
        Sets the suspend of this InlineResponse2011Links.

        :param suspend: The suspend of this InlineResponse2011Links.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self._suspend = suspend

    @property
    def activate(self):
        """
        Gets the activate of this InlineResponse2011Links.

        :return: The activate of this InlineResponse2011Links.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self._activate

    @activate.setter
    def activate(self, activate):
        """
        Sets the activate of this InlineResponse2011Links.

        :param activate: The activate of this InlineResponse2011Links.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self._activate = activate

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
        if not isinstance(other, InlineResponse2011Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other