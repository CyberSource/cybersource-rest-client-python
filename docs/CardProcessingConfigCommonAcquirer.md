# CardProcessingConfigCommonAcquirer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_id** | **str** | Identifier of the acquirer. This number is usually assigned by Visa. Applicable for VPC, GPX (gpx), CMCIC (cmcic), EFTPOS, CB2A, CUP, American Express Direct (amexdirect) and Six (six) processors.  Validation details (for selected processors)...  &lt;table&gt; &lt;thead&gt;&lt;tr&gt;&lt;th&gt;Processor&lt;/th&gt;&lt;th&gt;Acceptance Type&lt;/th&gt;&lt;th&gt;Required&lt;/th&gt;&lt;th&gt;Min. Length&lt;/th&gt;&lt;th&gt;Max. Length&lt;/th&gt;&lt;th&gt;Regex&lt;/th&gt;&lt;th&gt;Default Value&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt; &lt;tr&gt;&lt;td&gt;American Express Direct&lt;/td&gt;&lt;td&gt;cnp, cp, hybrid&lt;/td&gt;&lt;td&gt;Yes&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;13&lt;/td&gt;&lt;td&gt;^[0-9]+$&lt;/td&gt;&lt;td&gt;1111&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt;  | [optional] 
**interbank_card_association_id** | **str** | Number assigned by MasterCard to banks to identify the member in transactions. Applicable for VPC and GPX (gpx) processors. | [optional] 
**discover_institution_id** | **str** | Assigned by Discover to identify the acquirer. Applicable for VPC and GPX (gpx) processors. | [optional] 
**union_pay_institution_id** | **str** | Assigned by China Union Pay to identify the acquirer. Applicable for VPC processors. | [optional] 
**diners_club_institution_id** | **str** | Assigned by Diners Club to identify the acquirer. Applicable for VPC processors. | [optional] 
**country_code** | **str** | ISO 4217 format. Applicable for VPC, GPX (gpx), EFTPOS, RUPAY, Prisma (prisma) and CUP processors. | [optional] 
**file_destination_bin** | **str** | The BIN to which this capturefile is sent. This field must contain a valid BIN. Applicable for VPC and GPX (gpx) processors. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


