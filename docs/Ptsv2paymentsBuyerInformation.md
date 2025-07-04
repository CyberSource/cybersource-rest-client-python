# Ptsv2paymentsBuyerInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_customer_id** | **str** | Your identifier for the customer.  When a subscription or customer profile is being created, the maximum length for this field for most processors is 30. Otherwise, the maximum length is 100.  #### Comercio Latino For recurring payments in Mexico, the value is the customer&#39;s contract number. Note Before you request the authorization, you must inform the issuer of the customer contract numbers that will be used for recurring transactions.  #### Worldpay VAP For a follow-on credit with Worldpay VAP, CyberSource checks the following locations, in the order given, for a customer account ID value and uses the first value it finds: 1. &#x60;customer_account_id&#x60; value in the follow-on credit request 2. Customer account ID value that was used for the capture that is being credited 3. Customer account ID value that was used for the original authorization If a customer account ID value cannot be found in any of these locations, then no value is used.  | [optional] 
**date_of_birth** | **str** | Recipient&#39;s date of birth. **Format**: &#x60;YYYYMMDD&#x60;.  This field is a &#x60;pass-through&#x60;, which means that CyberSource ensures that the value is eight numeric characters but otherwise does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  | [optional] 
**vat_registration_number** | **str** | Customer&#39;s government-assigned tax identification number.  #### Tax Calculation Optional for international and value added taxes only. Not applicable to U.S. and Canadian taxes.  | [optional] 
**company_tax_id** | **str** | Company&#39;s tax identifier. This is only used for eCheck service.  ** TeleCheck ** Contact your TeleCheck representative to find out whether this field is required or optional.  ** All Other Processors ** Not used.  | [optional] 
**personal_identification** | [**list[Ptsv2paymentsBuyerInformationPersonalIdentification]**](Ptsv2paymentsBuyerInformationPersonalIdentification.md) |  | [optional] 
**hashed_password** | **str** | The merchant&#39;s password that CyberSource hashes and stores as a hashed password.  | [optional] 
**gender** | **str** | Customer&#39;s gender. Possible values are F (female), M (male),O (other). | [optional] 
**language** | **str** | language setting of the user.  Supports 2-character language codes (e.g., en, fr) and 5-character locale values (e.g., en-US, fr-CA).  | [optional] 
**note_to_seller** | **str** | Note to the recipient of the funds in this transaction | [optional] 
**mobile_phone** | **int** | Cardholder&#39;s mobile phone number. **Important** Required for Visa Secure transactions in Brazil. Do not use this request field for any other types of transactions.  | [optional] 
**wallet_id** | **str** | The one-time identification code of the Alipay wallet user.  It is scanned from the barcode that is shown by the mobile application.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


