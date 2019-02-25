cd %~dp0
java -jar swagger-codegen-cli-2.2.3.jar generate -t cybersource-python-template -i cybersource-rest-spec.json -l python -o ../ -c cybersource-python-config.json


 REM To change the URL
powershell -Command "(Get-Content ..\CyberSource\apis\payment_instruments_api.py) | ForEach-Object { $_ -replace '/tms/v1/instrumentidentifiers/{tokenId}/paymentinstruments', '/tms/v1/instrumentidentifiers/''+token_id+''/paymentinstruments' } | Set-Content ..\CyberSource\apis\payment_instruments_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\payment_instruments_api.py) | ForEach-Object { $_ -replace '''/tms/v1/paymentinstruments/{tokenId}''', '''/tms/v1/paymentinstruments/''+token_id'} | Set-Content ..\CyberSource\apis\payment_instruments_api.py"


powershell -Command "(Get-Content ..\CyberSource\apis\capture_api.py) | ForEach-Object { $_ -replace '/pts/v2/payments/{id}/captures', '/pts/v2/payments/''+id+''/captures' } | Set-Content ..\CyberSource\apis\capture_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\instrument_identifier_api.py) | ForEach-Object { $_ -replace '''/tms/v1/instrumentidentifiers/{tokenId}''', '''/tms/v1/instrumentidentifiers/''+token_id'} | Set-Content ..\CyberSource\apis\instrument_identifier_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\refund_api.py) | ForEach-Object { $_ -replace '/pts/v2/captures/{id}/refunds', '/pts/v2/captures/''+id+''/refunds' } | Set-Content ..\CyberSource\apis\refund_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\refund_api.py) | ForEach-Object { $_ -replace '/pts/v2/payments/{id}/refunds', '/pts/v2/payments/''+id+''/refunds' } | Set-Content ..\CyberSource\apis\refund_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\report_definitions_api.py) | ForEach-Object { $_ -replace '''/reporting/v3/report-definitions/{reportDefinitionName}''', '''/reporting/v3/report-definitions/''+report_definition_name'} | Set-Content ..\CyberSource\apis\report_definitions_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\report_subscriptions_api.py) | ForEach-Object { $_ -replace '''/reporting/v3/report-subscriptions/{reportName}''', '''/reporting/v3/report-subscriptions/''+report_name'} | Set-Content ..\CyberSource\apis\report_subscriptions_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\reports_api.py) | ForEach-Object { $_ -replace '''/reporting/v3/reports/{reportId}''', '''/reporting/v3/reports/''+report_id'} | Set-Content ..\CyberSource\apis\reports_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\reversal_api.py) | ForEach-Object { $_ -replace '/pts/v2/payments/{id}/reversals', '/pts/v2/payments/''+id+''/reversals' } | Set-Content ..\CyberSource\apis\reversal_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\search_transactions_api.py) | ForEach-Object { $_ -replace '''/tss/v2/searches/{id}''', '''/tss/v2/searches/''+id'} | Set-Content ..\CyberSource\apis\search_transactions_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\secure_file_share_api.py) | ForEach-Object { $_ -replace '''/sfs/v1/files/{fileId}''', '''/sfs/v1/files/''+file_id'} | Set-Content ..\CyberSource\apis\secure_file_share_api.py"



powershell -Command "(Get-Content ..\CyberSource\apis\transaction_batch_api.py) | ForEach-Object { $_ -replace '''/pts/v1/transaction-batches/{id}''', '''/pts/v1/transaction-batches/''+id'} | Set-Content ..\CyberSource\apis\transaction_batch_api.py"


powershell -Command "(Get-Content ..\CyberSource\apis\transaction_details_api.py) | ForEach-Object { $_ -replace '''/tss/v2/transactions/{id}''', '''/tss/v2/transactions/''+id'} | Set-Content ..\CyberSource\apis\transaction_details_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\void_api.py) | ForEach-Object { $_ -replace '/pts/v2/captures/{id}/voids', '/pts/v2/captures/''+id+''/voids'} | Set-Content ..\CyberSource\apis\void_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\void_api.py) | ForEach-Object { $_ -replace '/pts/v2/credits/{id}/voids', '/pts/v2/credits/''+id+''/voids'} | Set-Content ..\CyberSource\apis\void_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\void_api.py) | ForEach-Object { $_ -replace '/pts/v2/payments/{id}/voids', '/pts/v2/payments/''+id+''/voids'} | Set-Content ..\CyberSource\apis\void_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\void_api.py) | ForEach-Object { $_ -replace '/pts/v2/refunds/{id}/voids', '/pts/v2/refunds/''+id+''/voids'} | Set-Content ..\CyberSource\apis\void_api.py"


powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.error__links import ErrorLinks', 'from .models.error_links import ErrorLinks'} | Set-Content ..\CyberSource\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .error__links import ErrorLinks', 'from .error_links import ErrorLinks'} | Set-Content ..\CyberSource\models\__init__.py"

 REM To Change the Long file names
powershell -Command "(Get-Content ..\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .ptsv2payments_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\models\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .tmsv1instrumentidentifiers_processing_information_authorization_options_initiator_merchant_initiated_transaction import Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .tmsv1instrumentidentifiers_merchant_initiated_transaction import Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\models\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .models.ptsv2payments_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\__init__.py"

powershell -Command "(Get-Content ..\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.tmsv1instrumentidentifiers_processing_information_authorization_options_initiator_merchant_initiated_transaction import Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .models.tmsv1instrumentidentifiers_merchant_initiated_transaction import Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content ..\CyberSource\__init__.py"

del ..\CyberSource\models\ptsv2payments_merchant_initiated_transaction.py
del ..\CyberSource\models\tmsv1instrumentidentifiers_merchant_initiated_transaction.py
del ..\test\test_ptsv2payments_merchant_initiated_transaction.py
del ..\test\test_tmsv1instrumentidentifiers_merchant_initiated_transaction.py
del ..\docs\Ptsv2paymentsMerchantInitiatedTransaction.md
del ..\docs\Tmsv1instrumentidentifiersMerchantInitiatedTransaction.md

powershell -Command " rename-item -Path ..\CyberSource\models\ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py  -newname ptsv2payments_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path ..\CyberSource\models\tmsv1instrumentidentifiers_processing_information_authorization_options_initiator_merchant_initiated_transaction.py   -newname tmsv1instrumentidentifiers_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path ..\test\test_ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py   -newname test_ptsv2payments_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path ..\test\test_tmsv1instrumentidentifiers_processing_information_authorization_options_initiator_merchant_initiated_transaction.py   -newname test_tmsv1instrumentidentifiers_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path ..\docs\Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.md   -newname Ptsv2paymentsMerchantInitiatedTransaction.md"

powershell -Command " rename-item -Path ..\docs\Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.md  -newname Tmsv1instrumentidentifiersMerchantInitiatedTransaction.md"



 REM To change the Accept type and Content type
powershell -Command "(Get-Content ..\CyberSource\apis\capture_api.py) | ForEach-Object { $_ -replace 'select_header_accept\(\[''application/json', 'select_header_accept([''application/hal+json'} | Set-Content ..\CyberSource\apis\capture_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\credit_api.py) | ForEach-Object { $_ -replace 'select_header_accept\(\[''application/json', 'select_header_accept([''application/hal+json'} | Set-Content ..\CyberSource\apis\credit_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\payments_api.py) | ForEach-Object { $_ -replace 'select_header_accept\(\[''application/json', 'select_header_accept([''application/hal+json'} | Set-Content ..\CyberSource\apis\payments_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\process_a_payout_api.py) | ForEach-Object { $_ -replace 'select_header_accept\(\[''application/json', 'select_header_accept([''application/hal+json'} | Set-Content ..\CyberSource\apis\process_a_payout_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\refund_api.py) | ForEach-Object { $_ -replace 'select_header_accept\(\[''application/json', 'select_header_accept([''application/hal+json'} | Set-Content ..\CyberSource\apis\refund_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\reversal_api.py) | ForEach-Object { $_ -replace 'select_header_accept\(\[''application/json', 'select_header_accept([''application/hal+json'} | Set-Content ..\CyberSource\apis\reversal_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\transaction_details_api.py) | ForEach-Object { $_ -replace 'select_header_accept\(\[''application/json', 'select_header_accept([''application/hal+json'} | Set-Content ..\CyberSource\apis\transaction_details_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\user_management_api.py) | ForEach-Object { $_ -replace 'select_header_accept\(\[''application/json', 'select_header_accept([''application/hal+json'} | Set-Content ..\CyberSource\apis\user_management_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\void_api.py) | ForEach-Object { $_ -replace 'select_header_accept\(\[''application/json', 'select_header_accept([''application/hal+json'} | Set-Content ..\CyberSource\apis\void_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\search_transactions_api.py) | ForEach-Object { $_ -replace 'select_header_accept\(\[''application/json', 'select_header_accept([''*/*'} | Set-Content ..\CyberSource\apis\search_transactions_api.py"

powershell -Command "(Get-Content ..\CyberSource\apis\secure_file_share_api.py) | ForEach-Object { $_ -replace 'select_header_content_type\(\[''application/json', 'select_header_content_type([''*/*'} | Set-Content ..\CyberSource\apis\secure_file_share_api.py"

git checkout ..\README.md

git checkout ..\setup.py

pause