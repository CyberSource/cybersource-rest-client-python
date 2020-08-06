cd %~dp0

@echo off

REM Delete the previously generated SDK code

rd /s /q ..\docs
rd /s /q ..\CyberSource\apis
rd /s /q ..\CyberSource\models
rd /s /q ..\test

REM Command to generate SDK

java -jar swagger-codegen-cli-2.2.3.jar generate -t cybersource-python-template -i cybersource-rest-spec.json -l python -o ../ -c cybersource-python-config.json

REM Fixing file names
powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.error__links import ErrorLinks', 'from .models.error_links import ErrorLinks'} | Set-Content ..\CyberSource\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .error__links import ErrorLinks', 'from .error_links import ErrorLinks'} | Set-Content ..\CyberSource\models\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\apis\report_subscriptions_api.py) | ForEach-Object { $_ -replace '''/reporting/v3/report-subscriptions/{reportName}''', '''/reporting/v3/report-subscriptions/{report_name}'''} | Set-Content ..\CyberSource\apis\report_subscriptions_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\instrument_identifier_api.py) | ForEach-Object { $_ -replace '''/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}''', '''/tms/v1/instrumentidentifiers/{instrument_identifier_token_id}'''} | Set-Content ..\CyberSource\apis\instrument_identifier_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\instrument_identifier_api.py) | ForEach-Object { $_ -replace '''/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}/paymentinstruments''', '''/tms/v1/instrumentidentifiers/{instrument_identifier_token_id}/paymentinstruments'''} | Set-Content ..\CyberSource\apis\instrument_identifier_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\payment_instrument_api.py) | ForEach-Object { $_ -replace '''/tms/v1/paymentinstruments/{paymentInstrumentTokenId}''', '''/tms/v1/paymentinstruments/{payment_instrument_token_id}'''} | Set-Content ..\CyberSource\apis\payment_instrument_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\reports_api.py) | ForEach-Object { $_ -replace '''/reporting/v3/reports/{reportId}''', '''/reporting/v3/reports/{report_id}'''} | Set-Content ..\CyberSource\apis\reports_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\report_definitions_api.py) | ForEach-Object { $_ -replace '''/reporting/v3/report-definitions/{reportDefinitionName}''', '''/reporting/v3/report-definitions/{report_definition_name}'''} | Set-Content ..\CyberSource\apis\report_definitions_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\secure_file_share_api.py) | ForEach-Object { $_ -replace '''/sfs/v1/files/{fileId}''', '''/sfs/v1/files/{file_id}'''} | Set-Content ..\CyberSource\apis\secure_file_share_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\search_transactions_api.py) | ForEach-Object { $_ -replace '''/tss/v2/searches/{searchId}''', '''/tss/v2/searches/{search_id}'''} | Set-Content ..\CyberSource\apis\search_transactions_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\customer_api.py) | ForEach-Object { $_ -replace '''/tms/v2/customers/{customerTokenId}''', '''/tms/v2/customers/{customer_token_id}'''} | Set-Content ..\CyberSource\apis\customer_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\customer_shipping_address_api.py) | ForEach-Object { $_ -replace '''/tms/v2/customers/{customerTokenId}/shipping-addresses''', '''/tms/v2/customers/{customer_token_id}/shipping-addresses'''} | Set-Content ..\CyberSource\apis\customer_shipping_address_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\customer_shipping_address_api.py) | ForEach-Object { $_ -replace '''/tms/v2/customers/{customerTokenId}/shipping-addresses/{shippingAddressTokenId}''', '''/tms/v2/customers/{customer_token_id}/shipping-addresses/{shipping_address_token_id}'''} | Set-Content ..\CyberSource\apis\customer_shipping_address_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\customer_payment_instrument_api.py) | ForEach-Object { $_ -replace '''/tms/v2/customers/{customerTokenId}/payment-instruments''', '''/tms/v2/customers/{customer_token_id}/payment-instruments'''} | Set-Content ..\CyberSource\apis\customer_payment_instrument_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\customer_payment_instrument_api.py) | ForEach-Object { $_ -replace '''/tms/v2/customers/{customerTokenId}/payment-instruments/{paymentInstrumentTokenId}''', '''/tms/v2/customers/{customer_token_id}/payment-instruments/{payment_instrument_token_id}'''} | Set-Content ..\CyberSource\apis\customer_payment_instrument_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\symmetric_key_management_api.py) | ForEach-Object { $_ -replace '''/kms/v2/keys-sym/{keyId}''', '''/kms/v2/keys-sym/{key_id}'''} | Set-Content ..\CyberSource\apis\symmetric_key_management_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\asymmetric_key_management_api.py) | ForEach-Object { $_ -replace '''/kms/v2/keys-asym/{keyId}''', '''/kms/v2/keys-asym/{key_id}'''} | Set-Content ..\CyberSource\apis\asymmetric_key_management_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\secure_file_share_api.py) | ForEach-Object { $_ -replace 'select_header_content_type\(\[''application/json', 'select_header_content_type([''*/*'} | Set-Content ..\CyberSource\apis\secure_file_share_api.py"


REM powershell -Command "(Get-Content ..\CyberSource\apis\__init__.py) | ForEach-Object { $_ -replace 'from .download_dtd_api import DownloadDTDApi', ''} | ForEach-Object { $_ -replace 'from .download_xsd_api import DownloadXSDApi', ''} | Set-Content ..\CyberSource\apis\__init__.py"

REM powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .apis.download_dtd_api import DownloadDTDApi', ''} | ForEach-Object { $_ -replace 'from .apis.download_xsd_api import DownloadXSDApi', ''} | Set-Content ..\CyberSource\__init__.py"

REM To Change the Long file names
REM Change filenames in models\__init__.py
powershell -Command "(Get-Content ..\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .ptsv2payments_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\models\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .tmsv2customers__embedded_default_payment_instrument__embedded_instrument_identifier_processing_information_authorization_options_initiator_merchant_initiated_transaction import Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .tmsv2customers__embedded_merchant_initiated_transaction import Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\models\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .tmsv2customers__embedded_default_payment_instrument__embedded_instrument_identifier_processing_information_authorization_options_initiator import Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformationAuthorizationOptionsInitiator', 'from .tmsv2customers__embedded_authorization_options_initiator import Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformationAuthorizationOptionsInitiator'} | Set-Content ..\CyberSource\models\__init__.py"

REM powershell -Command "(Get-Content ..\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .risk_v1_authentication_exemptions_post201_response_consumer_authentication_information_strong_authentication import RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformationStrongAuthentication', 'from .risk_v1_authentication_exemptions_post201_response_strong_authentication import RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformationStrongAuthentication'} | Set-Content ..\CyberSource\models\__init__.py"

REM Change filenames in __init__.py
powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .models.ptsv2payments_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.tmsv2customers__embedded_default_payment_instrument__embedded_instrument_identifier_processing_information_authorization_options_initiator_merchant_initiated_transaction import Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .models.tmsv2customers__embedded_merchant_initiated_transaction import Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.tmsv2customers__embedded_default_payment_instrument__embedded_instrument_identifier_processing_information_authorization_options_initiator import Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformationAuthorizationOptionsInitiator', 'from .models.tmsv2customers__embedded_authorization_options_initiator import Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformationAuthorizationOptionsInitiator'} | Set-Content ..\CyberSource\__init__.py"

REM powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.risk_v1_authentication_exemptions_post201_response_consumer_authentication_information_strong_authentication import RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformationStrongAuthentication', 'from .models.risk_v1_authentication_exemptions_post201_response_strong_authentication import RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformationStrongAuthentication'} | Set-Content ..\CyberSource\__init__.py"

REM Change filenames in models
powershell -Command " rename-item -Path ..\CyberSource\models\ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py  -newname ptsv2payments_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path ..\CyberSource\models\tmsv2customers__embedded_default_payment_instrument__embedded_instrument_identifier_processing_information_authorization_options_initiator_merchant_initiated_transaction.py   -newname tmsv2customers__embedded_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path ..\CyberSource\models\tmsv2customers__embedded_default_payment_instrument__embedded_instrument_identifier_processing_information_authorization_options_initiator.py   -newname tmsv2customers__embedded_authorization_options_initiator.py"

REM powershell -Command " rename-item -Path ..\CyberSource\models\risk_v1_authentication_exemptions_post201_response_consumer_authentication_information_strong_authentication.py  -newname risk_v1_authentication_exemptions_post201_response_strong_authentication.py"

REM Change filenames in test
powershell -Command " rename-item -Path ..\test\test_ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py   -newname test_ptsv2payments_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path ..\test\test_tmsv2customers__embedded_default_payment_instrument__embedded_instrument_identifier_processing_information_authorization_options_initiator_merchant_initiated_transaction.py -newname test_tmsv2customers__embedded_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path ..\test\test_tmsv2customers__embedded_default_payment_instrument__embedded_instrument_identifier_processing_information_authorization_options_initiator.py -newname test_tmsv2customers__embedded_authorization_options_initiator.py"

REM powershell -Command " rename-item -Path ..\test\test_risk_v1_authentication_exemptions_post201_response_consumer_authentication_information_strong_authentication.py   -newname test_risk_v1_authentication_exemptions_post201_response_strong_authentication.py"

REM Change filenames in docs
powershell -Command " rename-item -Path ..\docs\Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.md   -newname Ptsv2paymentsMerchantInitiatedTransaction.md"

powershell -Command " rename-item -Path ..\docs\Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.md  -newname Tmsv2customersEmbeddedMerchantInitiatedTransaction.md"

powershell -Command " rename-item -Path ..\docs\Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformationAuthorizationOptionsInitiator.md  -newname Tmsv2customersEmbeddedAuthorizationOptionsInitiator.md"

REM powershell -Command " rename-item -Path ..\docs\RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformationStrongAuthentication.md   -newname RiskV1AuthenticationExemptionsPost201ResponseStrongAuthentication.md"

git checkout ..\README.md

git checkout ..\setup.py

pause
