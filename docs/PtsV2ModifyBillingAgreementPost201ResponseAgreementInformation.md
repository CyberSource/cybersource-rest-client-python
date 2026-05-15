# PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the mandate.  | [optional] 
**date_signed** | **str** | Date the mandate has been signed.  Format YYYYMMdd | [optional] 
**date_created** | **str** | Date the mandate has been created.  Format YYYYMMdd | [optional] 
**date_revoked** | **str** | Date the mandate has been revoked.  Format YYYYMMdd | [optional] 
**type** | **str** | Identifies the type of schedule as either recurring, one-off, split or usage.  Possible values: - recurring - oneoff - split - usage | [optional] 
**frequency** | **str** | Regularity with which the event occurs.  Possible values: - annual - monthly - quarterly - semiannual - weekly - daily - adhoc - intraday - fortnightly | [optional] 
**encoded_html** | **str** | Base64 encoded html string | [optional] 
**encoded_html_popup** | **str** | Base64 encoded popup html string | [optional] 
**url** | **str** | URL for redirecting the customer for creating the mandate.  | [optional] 
**transaction_id** | **str** | The Billing Agreement ID returned by processor (PayPal).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


