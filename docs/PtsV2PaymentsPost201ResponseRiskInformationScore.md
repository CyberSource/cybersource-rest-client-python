# PtsV2PaymentsPost201ResponseRiskInformationScore

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor_codes** | **list[str]** |  | [optional] 
**model_used** | **str** | Name of the score model used for the transaction. If you did not include a custom model in your request, this field contains the name of CyberSource&#39;s default model.  For all possible values, see the &#x60;score_model_used&#x60; field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** &gt; **Documentation** &gt; **Guides** &gt; _Decision Manager Using the SCMP API Developer Guide_ (PDF link).  | [optional] 
**result** | **str** | Total score calculated for this order. The value cannot be negative.  For all possible values, see the &#x60;score_score_result&#x60; field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** &gt; **Documentation** &gt; **Guides** &gt; _Decision Manager Using the SCMP API Developer Guide_ (PDF link).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


