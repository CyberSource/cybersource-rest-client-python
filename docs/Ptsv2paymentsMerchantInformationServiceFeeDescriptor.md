# Ptsv2paymentsMerchantInformationServiceFeeDescriptor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the service provider that is collecting the service fee. The service provider name must consist of 3, 7, or 12 characters followed by an asterisk (*). This value must also include the words \&quot;Service Fee.\&quot;  When you include more than one consecutive space, extra spaces are removed. Use one of the following formats for this value: - &lt;3-character name&gt;*Service Fee - &lt;7-character name&gt;*Service Fee - &lt;12-character name&gt;*Service Fee  When payments are made in installments, this value must also include installment information such as \&quot;1 of 5\&quot; or \&quot;3 of 7.\&quot; For installment payments, use one of the following formats for this value: - &lt;3-character name&gt;*Service Fee*&lt;N&gt; of &lt;M&gt; - &lt;7-character name&gt;*Service Fee*&lt;N&gt; of &lt;M&gt; - &lt;12-character name&gt;*Service Fee*&lt;N&gt; of &lt;M&gt;  where &lt;N&gt; is the payment number and &lt;M&gt; is the total number of payments.  When you do not include this value in your request, CyberSource uses the value that is in your CyberSource account.  This value might be displayed on the cardholder&#39;s statement.  | [optional] 
**contact** | **str** | Contact information for the service provider that is collecting the service fee. when you include more than one consecutive space, extra spaces are removed.  When you do not include this value in your request, CyberSource uses the value that is in your CyberSource account.  This value might be displayed on the cardholder&#39;s statement.  | [optional] 
**state** | **str** | State or territory in which the service provider is located.  When you do not include this value in your request, CyberSource uses the value that is in your CyberSource account.  This value might be displayed on the cardholder&#39;s statement.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


