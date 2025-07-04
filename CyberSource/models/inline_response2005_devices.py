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


class InlineResponse2005Devices(object):
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
        'reader_id': 'str',
        'terminal_serial_number': 'str',
        'terminal_id': 'str',
        'model': 'str',
        'make': 'str',
        'hardware_revision': 'str',
        'status': 'str',
        'creation_date': 'str',
        'pin': 'str'
    }

    attribute_map = {
        'reader_id': 'readerId',
        'terminal_serial_number': 'terminalSerialNumber',
        'terminal_id': 'terminalId',
        'model': 'model',
        'make': 'make',
        'hardware_revision': 'hardwareRevision',
        'status': 'status',
        'creation_date': 'creationDate',
        'pin': 'pin'
    }

    def __init__(self, reader_id=None, terminal_serial_number=None, terminal_id=None, model=None, make=None, hardware_revision=None, status=None, creation_date=None, pin=None):
        """
        InlineResponse2005Devices - a model defined in Swagger
        """

        self._reader_id = None
        self._terminal_serial_number = None
        self._terminal_id = None
        self._model = None
        self._make = None
        self._hardware_revision = None
        self._status = None
        self._creation_date = None
        self._pin = None

        if reader_id is not None:
          self.reader_id = reader_id
        if terminal_serial_number is not None:
          self.terminal_serial_number = terminal_serial_number
        if terminal_id is not None:
          self.terminal_id = terminal_id
        if model is not None:
          self.model = model
        if make is not None:
          self.make = make
        if hardware_revision is not None:
          self.hardware_revision = hardware_revision
        if status is not None:
          self.status = status
        if creation_date is not None:
          self.creation_date = creation_date
        if pin is not None:
          self.pin = pin

    @property
    def reader_id(self):
        """
        Gets the reader_id of this InlineResponse2005Devices.

        :return: The reader_id of this InlineResponse2005Devices.
        :rtype: str
        """
        return self._reader_id

    @reader_id.setter
    def reader_id(self, reader_id):
        """
        Sets the reader_id of this InlineResponse2005Devices.

        :param reader_id: The reader_id of this InlineResponse2005Devices.
        :type: str
        """

        self._reader_id = reader_id

    @property
    def terminal_serial_number(self):
        """
        Gets the terminal_serial_number of this InlineResponse2005Devices.

        :return: The terminal_serial_number of this InlineResponse2005Devices.
        :rtype: str
        """
        return self._terminal_serial_number

    @terminal_serial_number.setter
    def terminal_serial_number(self, terminal_serial_number):
        """
        Sets the terminal_serial_number of this InlineResponse2005Devices.

        :param terminal_serial_number: The terminal_serial_number of this InlineResponse2005Devices.
        :type: str
        """

        self._terminal_serial_number = terminal_serial_number

    @property
    def terminal_id(self):
        """
        Gets the terminal_id of this InlineResponse2005Devices.

        :return: The terminal_id of this InlineResponse2005Devices.
        :rtype: str
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """
        Sets the terminal_id of this InlineResponse2005Devices.

        :param terminal_id: The terminal_id of this InlineResponse2005Devices.
        :type: str
        """

        self._terminal_id = terminal_id

    @property
    def model(self):
        """
        Gets the model of this InlineResponse2005Devices.

        :return: The model of this InlineResponse2005Devices.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this InlineResponse2005Devices.

        :param model: The model of this InlineResponse2005Devices.
        :type: str
        """

        self._model = model

    @property
    def make(self):
        """
        Gets the make of this InlineResponse2005Devices.

        :return: The make of this InlineResponse2005Devices.
        :rtype: str
        """
        return self._make

    @make.setter
    def make(self, make):
        """
        Sets the make of this InlineResponse2005Devices.

        :param make: The make of this InlineResponse2005Devices.
        :type: str
        """

        self._make = make

    @property
    def hardware_revision(self):
        """
        Gets the hardware_revision of this InlineResponse2005Devices.

        :return: The hardware_revision of this InlineResponse2005Devices.
        :rtype: str
        """
        return self._hardware_revision

    @hardware_revision.setter
    def hardware_revision(self, hardware_revision):
        """
        Sets the hardware_revision of this InlineResponse2005Devices.

        :param hardware_revision: The hardware_revision of this InlineResponse2005Devices.
        :type: str
        """

        self._hardware_revision = hardware_revision

    @property
    def status(self):
        """
        Gets the status of this InlineResponse2005Devices.
        Status of the device. Possible Values:   - 'ACTIVE'   - 'INACTIVE' 

        :return: The status of this InlineResponse2005Devices.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InlineResponse2005Devices.
        Status of the device. Possible Values:   - 'ACTIVE'   - 'INACTIVE' 

        :param status: The status of this InlineResponse2005Devices.
        :type: str
        """

        self._status = status

    @property
    def creation_date(self):
        """
        Gets the creation_date of this InlineResponse2005Devices.

        :return: The creation_date of this InlineResponse2005Devices.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this InlineResponse2005Devices.

        :param creation_date: The creation_date of this InlineResponse2005Devices.
        :type: str
        """

        self._creation_date = creation_date

    @property
    def pin(self):
        """
        Gets the pin of this InlineResponse2005Devices.

        :return: The pin of this InlineResponse2005Devices.
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """
        Sets the pin of this InlineResponse2005Devices.

        :param pin: The pin of this InlineResponse2005Devices.
        :type: str
        """

        self._pin = pin

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
        if not isinstance(other, InlineResponse2005Devices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
