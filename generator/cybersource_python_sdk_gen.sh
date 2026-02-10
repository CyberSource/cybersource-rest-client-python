#!/bin/bash

# Navigate to the script's directory
cd "$(dirname "$0")"

# Delete the previously generated SDK code
rm -rf ../docs
rm -rf ../CyberSource/api
rm -rf ../CyberSource/apis
rm -rf ../CyberSource/models
rm -rf ../test

# Run Python field name replacement
python3 replaceFieldNamesForPaths.py -i cybersource-rest-spec.json -o cybersource-rest-spec-python.json > replaceFieldLogs.log
rm -f replaceFieldLogs.log

# Generate SDK using Swagger Codegen
$JAVA_17_BIN -jar swagger-codegen-cli-2.4.38.jar generate -t cybersource-python-template -i cybersource-rest-spec-python.json -l python -o ../ -c cybersource-python-config.json

# Change long filenames to shorter ones
# Change filenames in models/__init__.py
sed -i 's/from \.ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction/from .ptsv2payments_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction/g' ../CyberSource/models/__init__.py

# Change filenames in __init__.py
sed -i 's/from \.models\.ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction/from .models.ptsv2payments_merchant_initiated_transaction import Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction/g' ../CyberSource/__init__.py

# Rename files in models
if [ -f ../CyberSource/models/ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py ]; then
    mv ../CyberSource/models/ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py ../CyberSource/models/ptsv2payments_merchant_initiated_transaction.py
fi

# Rename files in test
if [ -f ../test/test_ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py ]; then
    mv ../test/test_ptsv2payments_processing_information_authorization_options_initiator_merchant_initiated_transaction.py ../test/test_ptsv2payments_merchant_initiated_transaction.py
fi

# Rename files in docs
if [ -f ../docs/Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.md ]; then
    mv ../docs/Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.md ../docs/Ptsv2paymentsMerchantInitiatedTransaction.md
fi

# Replace sdkLinks fieldName to links for supporting links field name in request/response body
echo "Starting replacement of links keyword in pbl_payment_links_all_get200_response.py model"
sed -i "s/'sdk_links': 'sdkLinks'/'sdk_links': 'links'/g" ../CyberSource/models/pbl_payment_links_all_get200_response.py
echo "Completed replacement of links keyword in pbl_payment_links_all_get200_response.py model"

# Checkout specific files to restore original versions
git checkout ../README.md
git checkout ../setup.py

git checkout ../CyberSource/api/o_auth_api.py
git checkout ../CyberSource/api/batch_upload_with_mtls_api.py
git checkout ../CyberSource/models/access_token_response.py
git checkout ../CyberSource/models/bad_request_error.py
git checkout ../CyberSource/models/create_access_token_request.py
git checkout ../CyberSource/models/resource_not_found_error.py
git checkout ../CyberSource/models/unauthorized_client_error.py

git checkout ../docs/OAuthApi.md
git checkout ../docs/AccessTokenResponse.md
git checkout ../docs/BadRequestError.md
git checkout ../docs/CreateAccessTokenRequest.md
git checkout ../docs/ResourceNotFoundError.md
git checkout ../docs/UnauthorizedClientError.md

git checkout ../test/test_o_auth_api.py
git checkout ../test/test_access_token_response.py
git checkout ../test/test_bad_request_error.py
git checkout ../test/test_create_access_token_request.py
git checkout ../test/test_resource_not_found_error.py
git checkout ../test/test_unauthorized_client_error.py

rm -f ../git_push.sh
rm -f ../.travis.yml
rm -f ../.swagger-codegen-ignore

echo "SDK generation completed successfully"
