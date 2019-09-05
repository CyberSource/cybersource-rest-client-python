cd %~dp0

@echo off

REM Delete the previously generated SDK code

rd /s /q ..\docs
rd /s /q ..\CyberSource
rd /s /q ..\test

REM Command to generate SDK

java -jar swagger-codegen-cli-2.2.3.jar generate -t cybersource-python-template -i cybersource-rest-spec.json -l python -o ../ -c cybersource-python-config.json

REM Fixing file names
powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.error__links import ErrorLinks', 'from .models.error_links import ErrorLinks'} | Set-Content ..\CyberSource\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .error__links import ErrorLinks', 'from .error_links import ErrorLinks'} | Set-Content ..\CyberSource\models\__init__.py"

REM powershell -Command "(Get-Content ..\CyberSource\apis\__init__.py) | ForEach-Object { $_ -replace 'from .download_dtd_api import DownloadDTDApi', ''} | ForEach-Object { $_ -replace 'from .download_xsd_api import DownloadXSDApi', ''} | Set-Content ..\CyberSource\apis\__init__.py"

REM powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .apis.download_dtd_api import DownloadDTDApi', ''} | ForEach-Object { $_ -replace 'from .apis.download_xsd_api import DownloadXSDApi', ''} | Set-Content ..\CyberSource\__init__.py"

 REM To Change the Long file names
powershell -Command "(Get-Content ..\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .ptsv2payments_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\models\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .tms_v1_instrument_identifiers_post200_response_processing_information_authorization_options_initiator_merchant_initiated_transaction import TmsV1InstrumentIdentifiersPost200ResponseProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .tmsv1instrumentidentifiers_post200_response_merchant_initiated_transaction import TmsV1InstrumentIdentifiersPost200ResponseProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\models\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .models.ptsv2payments_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.tms_v1_instrument_identifiers_post200_response_processing_information_authorization_options_initiator_merchant_initiated_transaction import TmsV1InstrumentIdentifiersPost200ResponseProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .models.tmsv1instrumentidentifiers_post200_response_merchant_initiated_transaction import TmsV1InstrumentIdentifiersPost200ResponseProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\__init__.py"

powershell -Command " rename-item -Path ..\CyberSource\models\ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py  -newname ptsv2payments_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path ..\CyberSource\models\tms_v1_instrument_identifiers_post200_response_processing_information_authorization_options_initiator_merchant_initiated_transaction.py   -newname tmsv1instrumentidentifiers_post200_response_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path ..\test\test_ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py   -newname test_ptsv2payments_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path ..\test\test_tms_v1_instrument_identifiers_post200_response_processing_information_authorization_options_initiator_merchant_initiated_transaction.py   -newname test_tmsv1instrumentidentifiers_post200_response_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path ..\docs\Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.md   -newname Ptsv2paymentsMerchantInitiatedTransaction.md"

powershell -Command " rename-item -Path ..\docs\TmsV1InstrumentIdentifiersPost200ResponseProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.md  -newname Tmsv1instrumentidentifiersPost200ResponseMerchantInitiatedTransaction.md"

REM To change the Accept type and Content type
powershell -Command "(Get-Content ..\CyberSource\apis\search_transactions_api.py) | ForEach-Object { $_ -replace 'select_header_accept\(\[''application/json', 'select_header_accept([''*/*'} | Set-Content ..\CyberSource\apis\search_transactions_api.py"

git checkout ..\README.md

git checkout ..\setup.py

pause