cd %~dp0

@echo off

REM Delete the previously generated SDK code

rd /s /q ..\docs
rd /s /q ..\CyberSource\api
rd /s /q ..\CyberSource\apis
rd /s /q ..\CyberSource\models
rd /s /q ..\test

setlocal enabledelayedexpansion
python replaceFieldNamesForPaths.py -i cybersource-rest-spec.json -o cybersource-rest-spec-python.json > replaceFieldLogs.log
del replaceFieldLogs.log
endlocal

REM Command to generate SDK

java -jar swagger-codegen-cli-2.4.38.jar generate -t cybersource-python-template -i cybersource-rest-spec-python.json -l python -o ../ -c cybersource-python-config.json

REM To Change the Long file names
REM Change filenames in models\__init__.py
powershell -Command "(Get-Content ..\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .ptsv2payments_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\models\__init__.py"
REM Change filenames in __init__.py
powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .models.ptsv2payments_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\__init__.py"
REM Change filenames in models
powershell -Command " rename-item -Path ..\CyberSource\models\ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py  -newname ptsv2payments_merchant_initiated_transaction.py"
REM Change filenames in test
powershell -Command " rename-item -Path ..\test\test_ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py   -newname test_ptsv2payments_merchant_initiated_transaction.py"
REM Change filenames in docs
powershell -Command " rename-item -Path ..\docs\Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.md   -newname Ptsv2paymentsMerchantInitiatedTransaction.md"


@REM replace sdkLinks fieldName to links for supporting links field name in request/response body
echo "starting of replacing the links keyword in pbl_payment_links_all_get200_response.py model"
powershell -Command "Set-Content ..\CyberSource\models\pbl_payment_links_all_get200_response.py ((Get-Content ..\CyberSource\models\pbl_payment_links_all_get200_response.py -Raw) -replace '''sdk_links'': ''sdkLinks''', '''sdk_links'': ''links''')"
echo "completed the task of replacing the links keyword in pbl_payment_links_all_get200_response.py model"

git checkout ..\README.md

git checkout ..\setup.py

git checkout ..\CyberSource\api\o_auth_api.py
git checkout ..\CyberSource\api\batch_upload_with_mtls_api.py
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
