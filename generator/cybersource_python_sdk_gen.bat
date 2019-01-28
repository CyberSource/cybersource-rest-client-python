mkdir %~dp0Python
cd %~dp0
java -jar swagger-codegen-cli-2.2.3.jar generate -t cybersource-python-template -i cybersource-rest-spec.json -l python -o Python -c %~dp0cybersource-python-config.json



powershell -Command "(Get-Content .\Python\CyberSource\apis\payment_instruments_api.py) | ForEach-Object { $_ -replace '/tms/v1/instrumentidentifiers/{tokenId}/paymentinstruments', '/tms/v1/instrumentidentifiers/''+token_id+''/paymentinstruments' } | Set-Content .\Python\CyberSource\apis\payment_instruments_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\payment_instruments_api.py) | ForEach-Object { $_ -replace '''/tms/v1/paymentinstruments/{tokenId}''', '''/tms/v1/paymentinstruments/''+token_id'} | Set-Content .\Python\CyberSource\apis\payment_instruments_api.py"


powershell -Command "(Get-Content .\Python\CyberSource\apis\capture_api.py) | ForEach-Object { $_ -replace '/pts/v2/payments/{id}/captures', '/pts/v2/payments/''+id+''/captures' } | Set-Content .\Python\CyberSource\apis\capture_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\instrument_identifier_api.py) | ForEach-Object { $_ -replace '''/tms/v1/instrumentidentifiers/{tokenId}''', '''/tms/v1/instrumentidentifiers/''+token_id'} | Set-Content .\Python\CyberSource\apis\instrument_identifier_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\refund_api.py) | ForEach-Object { $_ -replace '/pts/v2/captures/{id}/refunds', '/pts/v2/captures/''+id+''/refunds' } | Set-Content .\Python\CyberSource\apis\refund_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\refund_api.py) | ForEach-Object { $_ -replace '/pts/v2/payments/{id}/refunds', '/pts/v2/payments/''+id+''/refunds' } | Set-Content .\Python\CyberSource\apis\refund_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\report_definitions_api.py) | ForEach-Object { $_ -replace '''/reporting/v3/report-definitions/{reportDefinitionName}''', '''/reporting/v3/report-definitions/''+report_definition_name'} | Set-Content .\Python\CyberSource\apis\report_definitions_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\report_subscriptions_api.py) | ForEach-Object { $_ -replace '''/reporting/v3/report-subscriptions/{reportName}''', '''/reporting/v3/report-subscriptions/''+report_name'} | Set-Content .\Python\CyberSource\apis\report_subscriptions_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\reports_api.py) | ForEach-Object { $_ -replace '''/reporting/v3/reports/{reportId}''', '''/reporting/v3/reports/''+report_id'} | Set-Content .\Python\CyberSource\apis\reports_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\reversal_api.py) | ForEach-Object { $_ -replace '/pts/v2/payments/{id}/reversals', '/pts/v2/payments/''+id+''/reversals' } | Set-Content .\Python\CyberSource\apis\reversal_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\search_transactions_api.py) | ForEach-Object { $_ -replace '''/tss/v2/searches/{id}''', '''/tss/v2/searches/''+id'} | Set-Content .\Python\CyberSource\apis\search_transactions_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\secure_file_share_api.py) | ForEach-Object { $_ -replace '''/v1/files/{fileId}''', '''/v1/files/''+file_id'} | Set-Content .\Python\CyberSource\apis\secure_file_share_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\secure_file_share_api.py) | ForEach-Object { $_ -replace '/v1/file-details', '/v1/file-details'} | Set-Content .\Python\CyberSource\apis\secure_file_share_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\transaction_batch_api.py) | ForEach-Object { $_ -replace '''/pts/v1/transaction-batches/{id}''', '''/pts/v1/transaction-batches/''+id'} | Set-Content .\Python\CyberSource\apis\transaction_batch_api.py"


powershell -Command "(Get-Content .\Python\CyberSource\apis\transaction_details_api.py) | ForEach-Object { $_ -replace '''/tss/v2/transactions/{id}''', '''/tss/v2/transactions/''+id'} | Set-Content .\Python\CyberSource\apis\transaction_details_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\void_api.py) | ForEach-Object { $_ -replace '/pts/v2/captures/{id}/voids', '/pts/v2/captures/''+id+''/voids'} | Set-Content .\Python\CyberSource\apis\void_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\void_api.py) | ForEach-Object { $_ -replace '/pts/v2/credits/{id}/voids', '/pts/v2/credits/''+id+''/voids'} | Set-Content .\Python\CyberSource\apis\void_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\void_api.py) | ForEach-Object { $_ -replace '/pts/v2/payments/{id}/voids', '/pts/v2/payments/''+id+''/voids'} | Set-Content .\Python\CyberSource\apis\void_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\apis\void_api.py) | ForEach-Object { $_ -replace '/pts/v2/refunds/{id}/voids', '/pts/v2/refunds/''+id+''/voids'} | Set-Content .\Python\CyberSource\apis\void_api.py"

powershell -Command "(Get-Content .\Python\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.error__links import ErrorLinks', 'from .models.error_links import ErrorLinks'} | Set-Content .\Python\CyberSource\__init__.py"

powershell -Command "(Get-Content .\Python\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .error__links import ErrorLinks', 'from .error_links import ErrorLinks'} | Set-Content .\Python\CyberSource\models\__init__.py"

powershell -Command "(Get-Content .\Python\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .ptsv2payments_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content .\Python\CyberSource\models\__init__.py"

powershell -Command "(Get-Content .\Python\CyberSource\models\__init__.py) | ForEach-Object { $_ -replace 'from .tmsv1instrumentidentifiers_processing_information_authorization_options_initiator_merchant_initiated_transaction import Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .tmsv1instrumentidentifiers_merchant_initiated_transaction import Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content .\Python\CyberSource\models\__init__.py"

powershell -Command "(Get-Content .\Python\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .models.ptsv2payments_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content .\Python\CyberSource\__init__.py"

powershell -Command "(Get-Content .\Python\CyberSource\__init__.py) | ForEach-Object { $_ -replace 'from .models.tmsv1instrumentidentifiers_processing_information_authorization_options_initiator_merchant_initiated_transaction import Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction', 'from .models.tmsv1instrumentidentifiers_merchant_initiated_transaction import Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'} | Set-Content .\Python\CyberSource\__init__.py"

powershell -Command " rename-item -Path .\Python\CyberSource\models\ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py  -newname ptsv2payments_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path .\Python\CyberSource\models\tmsv1instrumentidentifiers_processing_information_authorization_options_initiator_merchant_initiated_transaction.py   -newname tmsv1instrumentidentifiers_merchant_initiated_transaction.py"


powershell -Command " rename-item -Path .\Python\test\test_ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py   -newname test_ptsv2payments_merchant_initiated_transaction.py"

powershell -Command " rename-item -Path .\Python\test\test_tmsv1instrumentidentifiers_processing_information_authorization_options_initiator_merchant_initiated_transaction.py   -newname test_tmsv1instrumentidentifiers_merchant_initiated_transaction.py"


pause



