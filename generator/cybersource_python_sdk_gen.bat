cd %~dp0

@echo off

REM Delete the previously generated SDK code

rd /s /q ..\docs
rd /s /q ..\CyberSource\api
rd /s /q ..\CyberSource\apis
rd /s /q ..\CyberSource\models
rd /s /q ..\test

REM Command to generate SDK

java -jar swagger-codegen-cli-2.4.38.jar generate -t cybersource-python-template -i cybersource-rest-spec-python.json -l python -o ../ -c cybersource-python-config.json

REM Fixing file names
powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.error__links import ErrorLinks', 'from .models.error_links import ErrorLinks'} | Set-Content ..\CyberSource\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .error__links import ErrorLinks', 'from .error_links import ErrorLinks'} | Set-Content ..\CyberSource\models\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\api\secure_file_share_api.py) | ForEach-Object { $_ -replace 'select_header_content_type\(\[''\*_\/_\*;charset=utf-8', 'select_header_content_type([''*/*;charset=utf-8'} | Set-Content ..\CyberSource\api\secure_file_share_api.py"

powershell -Command "(Get-Content ..\docs\SecureFileShareApi.md) | ForEach-Object { $_ -replace '\*\*Content-Type\*\*: \*_\/_\*;charset=utf-8', '**Content-Type**: */*;charset=utf-8'} | Set-Content ..\docs\SecureFileShareApi.md"

REM powershell -Command "(Get-Content ..\CyberSource\api\__init__.py) | ForEach-Object { $_ -replace 'from .download_dtd_api import DownloadDTDApi', ''} | ForEach-Object { $_ -replace 'from .download_xsd_api import DownloadXSDApi', ''} | Set-Content ..\CyberSource\api\__init__.py"

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

git checkout ..\CyberSource\api\o_auth_api.py
git checkout ..\CyberSource\models\access_token_response.py
git checkout ..\CyberSource\models\bad_request_error.py
git checkout ..\CyberSource\models\create_access_token_request.py
git checkout ..\CyberSource\models\resource_not_found_error.py
git checkout ..\CyberSource\models\unauthorized_client_error.py

git checkout ..\docs\OAuthApi.md
git checkout ..\docs\AccessTokenResponse.md
git checkout ..\docs\BadRequestError.md
git checkout ..\docs\CreateAccessTokenRequest.md
git checkout ..\docs\ResourceNotFoundError.md
git checkout ..\docs\UnauthorizedClientError.md

git checkout ..\test\test_o_auth_api.py
git checkout ..\test\test_access_token_response.py
git checkout ..\test\test_bad_request_error.py
git checkout ..\test\test_create_access_token_request.py
git checkout ..\test\test_resource_not_found_error.py
git checkout ..\test\test_unauthorized_client_error.py

pause
