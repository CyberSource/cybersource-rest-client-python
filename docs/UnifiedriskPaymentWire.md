# UnifiedriskPaymentWire

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addenda** | **str** | Additional payment information or remittance data appended to the wire transfer message for beneficiary reconciliation purposes | [optional] 
**agent_to_agent_msg** | **str** | Free-text message transmitted between the originating and receiving financial agents for internal communication or compliance notes | [optional] 
**business_function_code** | **str** | Fedwire Business Function Code indicating the specific type of wire transfer (e.g., BTR for bank transfer, FFR for fed funds returned) | [optional] 
**debtor_to_creditor_msg** | **str** | Message from the payer to the payee providing remittance information, invoice references, or payment instructions | [optional] 
**imad_input_cycle_date** | **date** | Fedwire IMAD (Input Message Accountability Data) input cycle date in YYYYMMDD format, used to uniquely identify outgoing wire messages | [optional] 
**imad_input_sequence_number** | **str** | Sequential number within the IMAD cycle identifying this specific wire message within the processing day | [optional] 
**imad_input_source** | **str** | Source identifier in the IMAD, typically the Federal Reserve district code and routing information of the originating institution | [optional] 
**ofac_check_completed_flag** | **str** | Indicates whether OFAC (Office of Foreign Assets Control) sanctions screening has been completed for this wire transfer. Required for regulatory compliance | [optional] 
**omad_output_cycle_date** | **date** | Fedwire OMAD (Output Message Accountability Data) output cycle date, used to identify and track the received wire message at the destination institution | [optional] 
**omad_output_date** | **date** | Date component of the OMAD for the received wire, confirming the settlement date at the receiving institution | [optional] 
**omad_output_destination_id** | **str** | Destination routing identifier in the OMAD, identifying the Federal Reserve office that delivered the wire message | [optional] 
**omad_output_sequencer** | **str** | Sequential output identifier in the OMAD, used for uniquely identifying wire messages at the receiving end | [optional] 
**omad_output_time** | **int** | Time component of the OMAD in HHMM format (24-hour), indicating when the wire was delivered to the receiving institution | [optional] 
**supervisor_override_flag** | **str** | Indicates whether a supervisor manually overrode a compliance hold or exception flag on this wire transfer. Overrides require audit logging | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


