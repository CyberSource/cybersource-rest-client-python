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


class Ptsv2paymentsPaymentInformationTokenizedCard(object):
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
        'number': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'type': 'str',
        'cryptogram': 'str',
        'requestor_id': 'str',
        'transaction_type': 'str',
        'assurance_level': 'str',
        'storage_method': 'str',
        'security_code': 'str',
        'security_code_indicator': 'str',
        'assurance_method': 'str'
    }

    attribute_map = {
        'number': 'number',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'type': 'type',
        'cryptogram': 'cryptogram',
        'requestor_id': 'requestorId',
        'transaction_type': 'transactionType',
        'assurance_level': 'assuranceLevel',
        'storage_method': 'storageMethod',
        'security_code': 'securityCode',
        'security_code_indicator': 'securityCodeIndicator',
        'assurance_method': 'assuranceMethod'
    }

    def __init__(self, number=None, expiration_month=None, expiration_year=None, type=None, cryptogram=None, requestor_id=None, transaction_type=None, assurance_level=None, storage_method=None, security_code=None, security_code_indicator=None, assurance_method=None):
        """
        Ptsv2paymentsPaymentInformationTokenizedCard - a model defined in Swagger
        """

        self._number = None
        self._expiration_month = None
        self._expiration_year = None
        self._type = None
        self._cryptogram = None
        self._requestor_id = None
        self._transaction_type = None
        self._assurance_level = None
        self._storage_method = None
        self._security_code = None
        self._security_code_indicator = None
        self._assurance_method = None

        if number is not None:
          self.number = number
        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        if type is not None:
          self.type = type
        if cryptogram is not None:
          self.cryptogram = cryptogram
        if requestor_id is not None:
          self.requestor_id = requestor_id
        if transaction_type is not None:
          self.transaction_type = transaction_type
        if assurance_level is not None:
          self.assurance_level = assurance_level
        if storage_method is not None:
          self.storage_method = storage_method
        if security_code is not None:
          self.security_code = security_code
        if security_code_indicator is not None:
          self.security_code_indicator = security_code_indicator
        if assurance_method is not None:
          self.assurance_method = assurance_method

    @property
    def number(self):
        """
        Gets the number of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Customer's payment network token value. 

        :return: The number of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Customer's payment network token value. 

        :param number: The number of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """

        self._number = number

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this Ptsv2paymentsPaymentInformationTokenizedCard.
        One of two possible meanings: - The two-digit month in which a token expires. - The two-digit month in which a card expires. Format: `MM` Possible values: `01` through `12`  **NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (`card_type=039`), if there is no expiration date on the card, use `12`.\\ **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Samsung Pay and Apple Pay Month in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction. 

        :return: The expiration_month of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this Ptsv2paymentsPaymentInformationTokenizedCard.
        One of two possible meanings: - The two-digit month in which a token expires. - The two-digit month in which a card expires. Format: `MM` Possible values: `01` through `12`  **NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (`card_type=039`), if there is no expiration date on the card, use `12`.\\ **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Samsung Pay and Apple Pay Month in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction. 

        :param expiration_month: The expiration_month of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this Ptsv2paymentsPaymentInformationTokenizedCard.
        One of two possible meanings: - The four-digit year in which a token expires. - The four-digit year in which a card expires. Format: `YYYY` Possible values: `1900` through `3000` Data type: Non-negative integer  **NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (1900 through 3000) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (`card_ type=039`), if there is no expiration date on the card, use `2021`.  #### FDC Nashville Global and FDMS South You can send in 2 digits or 4 digits. When you send in 2 digits, they must be the last 2 digits of the year.  #### Samsung Pay and Apple Pay Year in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting. 

        :return: The expiration_year of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this Ptsv2paymentsPaymentInformationTokenizedCard.
        One of two possible meanings: - The four-digit year in which a token expires. - The four-digit year in which a card expires. Format: `YYYY` Possible values: `1900` through `3000` Data type: Non-negative integer  **NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (1900 through 3000) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (`card_ type=039`), if there is no expiration date on the card, use `2021`.  #### FDC Nashville Global and FDMS South You can send in 2 digits or 4 digits. When you send in 2 digits, they must be the last 2 digits of the year.  #### Samsung Pay and Apple Pay Year in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting. 

        :param expiration_year: The expiration_year of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """

        self._expiration_year = expiration_year

    @property
    def type(self):
        """
        Gets the type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Three-digit value that indicates the card type.  **IMPORTANT** It is strongly recommended that you include the card type field in request messages even if it is optional for your processor and card type. Omitting the card type can cause the transaction to be processed with the wrong card type.  Possible values: - `001`: Visa. Use card type value `001` for Visa Electron. - `002`: Mastercard, Eurocard[^1], which is a European regional brand of Mastercard. - `003`: American Express - `004`: Discover - `005`: Diners Club - `006`: Carte Blanche[^1] - `007`: JCB[^1] - `014`: Enroute[^1] - `021`: JAL[^1] - `024`: Maestro (UK Domestic)[^1] - `033`: Visa Electron[^1]. Do not use this value. Use `001` for all Visa card types. - `034`: Dankort[^1] - `036`: Cartes Bancaires[^1,4] - `037`: Carta Si[^1] - `039`: Encoded account number[^1] - `040`: UATP[^1] - `042`: Maestro (International)[^1] - `050`: Hipercard[^2,3] - `051`: Aura - `054`: Elo[^3] - `062`: China UnionPay - '070': EFTPOS  [^1]: For this card type, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in your request for an authorization or a stand-alone credit. [^2]: For this card type on Cielo 3.0, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. This card type is not supported on Cielo 1.5. [^3]: For this card type on Getnet and Rede, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. [^4]: For this card type, you must include the `paymentInformation.card.type` in your request for any payer authentication services.  #### Used by **Authorization** Required for Carte Blanche and JCB. Optional for all other card types.  #### Card Present reply This field is included in the reply message when the client software that is installed on the POS terminal uses the token management service (TMS) to retrieve tokenized payment details. You must contact customer support to have your account enabled to receive these fields in the credit reply message.  Returned by the Credit service.  This reply field is only supported by the following processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response.  #### GPX This field only supports transactions from the following card types: - Visa - Mastercard - AMEX - Discover - Diners - JCB - Union Pay International 

        :return: The type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Three-digit value that indicates the card type.  **IMPORTANT** It is strongly recommended that you include the card type field in request messages even if it is optional for your processor and card type. Omitting the card type can cause the transaction to be processed with the wrong card type.  Possible values: - `001`: Visa. Use card type value `001` for Visa Electron. - `002`: Mastercard, Eurocard[^1], which is a European regional brand of Mastercard. - `003`: American Express - `004`: Discover - `005`: Diners Club - `006`: Carte Blanche[^1] - `007`: JCB[^1] - `014`: Enroute[^1] - `021`: JAL[^1] - `024`: Maestro (UK Domestic)[^1] - `033`: Visa Electron[^1]. Do not use this value. Use `001` for all Visa card types. - `034`: Dankort[^1] - `036`: Cartes Bancaires[^1,4] - `037`: Carta Si[^1] - `039`: Encoded account number[^1] - `040`: UATP[^1] - `042`: Maestro (International)[^1] - `050`: Hipercard[^2,3] - `051`: Aura - `054`: Elo[^3] - `062`: China UnionPay - '070': EFTPOS  [^1]: For this card type, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in your request for an authorization or a stand-alone credit. [^2]: For this card type on Cielo 3.0, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. This card type is not supported on Cielo 1.5. [^3]: For this card type on Getnet and Rede, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. [^4]: For this card type, you must include the `paymentInformation.card.type` in your request for any payer authentication services.  #### Used by **Authorization** Required for Carte Blanche and JCB. Optional for all other card types.  #### Card Present reply This field is included in the reply message when the client software that is installed on the POS terminal uses the token management service (TMS) to retrieve tokenized payment details. You must contact customer support to have your account enabled to receive these fields in the credit reply message.  Returned by the Credit service.  This reply field is only supported by the following processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response.  #### GPX This field only supports transactions from the following card types: - Visa - Mastercard - AMEX - Discover - Diners - JCB - Union Pay International 

        :param type: The type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """

        self._type = type

    @property
    def cryptogram(self):
        """
        Gets the cryptogram of this Ptsv2paymentsPaymentInformationTokenizedCard.
        This field contains token information.

        :return: The cryptogram of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._cryptogram

    @cryptogram.setter
    def cryptogram(self, cryptogram):
        """
        Sets the cryptogram of this Ptsv2paymentsPaymentInformationTokenizedCard.
        This field contains token information.

        :param cryptogram: The cryptogram of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """

        self._cryptogram = cryptogram

    @property
    def requestor_id(self):
        """
        Gets the requestor_id of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Value that identifies your business and indicates that the cardholder's account number is tokenized. This value is assigned by the token service provider and is unique within the token service provider's database.  **Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**.  #### PIN debit Optional field for PIN debit credit or PIN debit purchase transactions that use payment network tokens; otherwise, not used. 

        :return: The requestor_id of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._requestor_id

    @requestor_id.setter
    def requestor_id(self, requestor_id):
        """
        Sets the requestor_id of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Value that identifies your business and indicates that the cardholder's account number is tokenized. This value is assigned by the token service provider and is unique within the token service provider's database.  **Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**.  #### PIN debit Optional field for PIN debit credit or PIN debit purchase transactions that use payment network tokens; otherwise, not used. 

        :param requestor_id: The requestor_id of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """

        self._requestor_id = requestor_id

    @property
    def transaction_type(self):
        """
        Gets the transaction_type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Type of transaction that provided the token data. This value does not specify the token service provider; it specifies the entity that provided you with information about the token.  Possible value: - `2`: Near-field communication (NFC) transaction. The customer's mobile device provided the token data for a contactless EMV transaction. For recurring transactions, use this value if the original transaction was a contactless EMV transaction.  #### Visa Platform Connect - `1`: For Rupay and In App tokenization. Example: InApp apple pay. - `3`: Card/Credential On File Tokenization.  **NOTE** No CyberSource through VisaNet acquirers support EMV at this time.  Required field for PIN debit credit or PIN debit purchase transactions that use payment network tokens; otherwise, not used.  #### Rupay - `3`: Card/Credential On File Tokenization. - `4`: Tokenizined Transaction. Should be used for Guest Checkout transactions with token. 

        :return: The transaction_type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """
        Sets the transaction_type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Type of transaction that provided the token data. This value does not specify the token service provider; it specifies the entity that provided you with information about the token.  Possible value: - `2`: Near-field communication (NFC) transaction. The customer's mobile device provided the token data for a contactless EMV transaction. For recurring transactions, use this value if the original transaction was a contactless EMV transaction.  #### Visa Platform Connect - `1`: For Rupay and In App tokenization. Example: InApp apple pay. - `3`: Card/Credential On File Tokenization.  **NOTE** No CyberSource through VisaNet acquirers support EMV at this time.  Required field for PIN debit credit or PIN debit purchase transactions that use payment network tokens; otherwise, not used.  #### Rupay - `3`: Card/Credential On File Tokenization. - `4`: Tokenizined Transaction. Should be used for Guest Checkout transactions with token. 

        :param transaction_type: The transaction_type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """

        self._transaction_type = transaction_type

    @property
    def assurance_level(self):
        """
        Gets the assurance_level of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Confidence level of the tokenization. This value is assigned by the token service provider.  **Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**.  Returned by PIN debit credit or PIN debit purchase.  **Note** Merchants supported for **CyberSource through VisaNet**/**Visa Platform Connect** are advised not to use this field. 

        :return: The assurance_level of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._assurance_level

    @assurance_level.setter
    def assurance_level(self, assurance_level):
        """
        Sets the assurance_level of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Confidence level of the tokenization. This value is assigned by the token service provider.  **Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**.  Returned by PIN debit credit or PIN debit purchase.  **Note** Merchants supported for **CyberSource through VisaNet**/**Visa Platform Connect** are advised not to use this field. 

        :param assurance_level: The assurance_level of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """

        self._assurance_level = assurance_level

    @property
    def storage_method(self):
        """
        Gets the storage_method of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Type of technology used in the device to store token data. Possible values:  - `001`: Secure Element (SE). Smart card or memory with restricted access and encryption to prevent data tampering. For storing payment    credentials, a SE is tested against a set of requirements defined by the payment networks.     **Note** This field is supported only for _FDC Compass_.  - 002: Host Card Emulation (HCE). Emulation of a smart card by using software to create a virtual and exact representation of the card. Sensitive data is stored in a database that is hosted in the cloud. For storing payment credentials, a database must meet very stringent security requirements that exceed PCI DSS.  **Note** This field is supported only for _FDC Compass_. 

        :return: The storage_method of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._storage_method

    @storage_method.setter
    def storage_method(self, storage_method):
        """
        Sets the storage_method of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Type of technology used in the device to store token data. Possible values:  - `001`: Secure Element (SE). Smart card or memory with restricted access and encryption to prevent data tampering. For storing payment    credentials, a SE is tested against a set of requirements defined by the payment networks.     **Note** This field is supported only for _FDC Compass_.  - 002: Host Card Emulation (HCE). Emulation of a smart card by using software to create a virtual and exact representation of the card. Sensitive data is stored in a database that is hosted in the cloud. For storing payment credentials, a database must meet very stringent security requirements that exceed PCI DSS.  **Note** This field is supported only for _FDC Compass_. 

        :param storage_method: The storage_method of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """

        self._storage_method = storage_method

    @property
    def security_code(self):
        """
        Gets the security_code of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Card Verification Number (CVN).  #### Ingenico ePayments Do not include this field when **commerceIndicator=recurring**. **Note** Ingenico ePayments was previously called _Global Collect_. 

        :return: The security_code of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """
        Sets the security_code of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Card Verification Number (CVN).  #### Ingenico ePayments Do not include this field when **commerceIndicator=recurring**. **Note** Ingenico ePayments was previously called _Global Collect_. 

        :param security_code: The security_code of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """

        self._security_code = security_code

    @property
    def security_code_indicator(self):
        """
        Gets the security_code_indicator of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Indicates whether a CVN code was sent. Possible values:   - `0` (default): CVN service not requested. This default value is used when you do not include      `securityCode` field in the request.  - `1` (default): CVN service requested and supported. This default value is used when you include      `securityCode` field in the request.  - `2`: CVN on credit card is illegible.  - `9`: CVN was not imprinted on credit card.  #### FDMS Nashville Required for American Express cards; otherwise, optional.  #### TSYS Acquiring Solutions Optional if `pointOfSaleInformation.entryMode=keyed`; otherwise, not used.  #### All other processors Optional. 

        :return: The security_code_indicator of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._security_code_indicator

    @security_code_indicator.setter
    def security_code_indicator(self, security_code_indicator):
        """
        Sets the security_code_indicator of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Indicates whether a CVN code was sent. Possible values:   - `0` (default): CVN service not requested. This default value is used when you do not include      `securityCode` field in the request.  - `1` (default): CVN service requested and supported. This default value is used when you include      `securityCode` field in the request.  - `2`: CVN on credit card is illegible.  - `9`: CVN was not imprinted on credit card.  #### FDMS Nashville Required for American Express cards; otherwise, optional.  #### TSYS Acquiring Solutions Optional if `pointOfSaleInformation.entryMode=keyed`; otherwise, not used.  #### All other processors Optional. 

        :param security_code_indicator: The security_code_indicator of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """

        self._security_code_indicator = security_code_indicator

    @property
    def assurance_method(self):
        """
        Gets the assurance_method of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Confidence level of the tokenization. This value is assigned by the token service provider.  **Note** This field is supported only for **Visa Platform Connect** 

        :return: The assurance_method of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._assurance_method

    @assurance_method.setter
    def assurance_method(self, assurance_method):
        """
        Sets the assurance_method of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Confidence level of the tokenization. This value is assigned by the token service provider.  **Note** This field is supported only for **Visa Platform Connect** 

        :param assurance_method: The assurance_method of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """

        self._assurance_method = assurance_method

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
        if not isinstance(other, Ptsv2paymentsPaymentInformationTokenizedCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
