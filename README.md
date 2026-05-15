
# Python Client SDK for the CyberSource REST API

## Description

The CyberSource Python client provides convenient access to the [CyberSource REST API](https://developer.cybersource.com/api/reference/api-reference.html) from your Python application.

## System Requirements

* **`Python 3.7`** or later

## Installation

* Install the CyberSource Python client using the below command

    ```bash
    pip install cybersource-rest-client-python
    ```

## Account Registration & Configuration

* Account Registration

Follow the first step mentioned in [Getting Started with CyberSource REST SDKs](https://developer.cybersource.com/hello-world/rest-api-sdks.html#gettingstarted) to create a sandbox account.

* Configuration

Follow the second step mentioned in [Getting Started with CyberSource REST SDKs](https://developer.cybersource.com/hello-world/rest-api-sdks.html#gettingstarted) to configure the SDK by inputting your credentials.

***Please note that this is for reference only. Ensure to store the credentials in a more secure manner.***

## Authentication

The CyberSource Python SDK supports multiple authentication methods. You can configure authentication by setting properties in your configuration dictionary.

> **⚠️ HTTP Signature Deprecation Notice:** HTTP Signature authentication is being deprecated. **JWT with Shared Secret** is the recommended migration path — it uses the same `merchant_keyid` and `merchant_secretkey` credentials, requires only two property changes, and enables MLE (Message Level Encryption) support that HTTP Signature does not provide.

### For HTTP Signature authentication (⚠️ Deprecated — migrate to JWT with Shared Secret)

```python
config = {
    'authentication_type': 'HTTP_Signature',
    'merchantid': 'your_merchant_id',
    'merchant_keyid': 'your_merchant_keyid',
    'merchant_secretkey': 'your_merchant_secretkey',
    'run_environment': 'apitest.cybersource.com'
}
```

### For JWT authentication (with P12 certificate)

```python
config = {
    'authentication_type': 'JWT',
    'merchantid': 'your_merchant_id',
    'run_environment': 'apitest.cybersource.com',
    'key_alias': 'your_key_alias',
    'key_password': 'your_key_password',
    'key_file_name': 'your_certificate_file_name',
    'keys_directory': 'path/to/keys/directory'
}
```

### For JWT authentication with Shared Secret (Recommended migration from HTTP Signature)

Uses the **same** `merchant_keyid` and `merchant_secretkey` credentials as HTTP Signature. Only two properties change:

```python
config = {
    'authentication_type': 'JWT',
    'jwt_key_type': 'SHARED_SECRET',
    'merchantid': 'your_merchant_id',
    'run_environment': 'apitest.cybersource.com',
    'merchant_keyid': 'your_merchant_keyid',
    'merchant_secretkey': 'your_merchant_secretkey'
}
```

### For using MetaKey

MetaKey can be used for HTTP Signature, JWT (P12), and JWT with Shared Secret authentication.

A Meta Key is a single key that can be used by one, some, or all merchants (or accounts, if created by a Portfolio user) in the portfolio. The Portfolio or Parent Account owns the key and is considered the transaction submitter when a Meta Key is used, while the merchant owns the transaction.

#### For HTTP Signature Authentication with MetaKey (⚠️ Deprecated)

```python
config = {
    'authentication_type': 'HTTP_Signature',
    'merchantid': 'your_transacting_merchant_id',
    'merchant_keyid': 'your_metakey_portfolio_keyid',
    'merchant_secretkey': 'your_metakey_portfolio_shared_secret',
    'run_environment': 'apitest.cybersource.com',
    'use_metakey': True,
    'portfolio_id': 'your_portfolio_id'
}
```

#### For JWT Authentication with MetaKey (P12)

```python
config = {
    'authentication_type': 'JWT',
    'merchantid': 'your_transacting_merchant_id',
    'run_environment': 'apitest.cybersource.com',
    'key_alias': 'your_portfolio_id',
    'key_password': 'your_metakey_portfolio_p12_password',
    'key_file_name': 'your_metakey_portfolio_p12_filename',
    'keys_directory': 'path/to/keys/directory',
    'use_metakey': True
}
```

#### For JWT Authentication with Shared Secret and MetaKey (Recommended)

```python
config = {
    'authentication_type': 'JWT',
    'jwt_key_type': 'SHARED_SECRET',
    'merchantid': 'your_transacting_merchant_id',
    'run_environment': 'apitest.cybersource.com',
    'merchant_keyid': 'your_metakey_portfolio_keyid',
    'merchant_secretkey': 'your_metakey_portfolio_shared_secret',
    'use_metakey': True,
    'portfolio_id': 'your_portfolio_id'
}
```

#### Response MLE with MetaKey

When Response MLE is enabled (`enableResponseMleGlobally=True`) and MetaKey is in use (`use_metakey=True`), the Response MLE configuration must use the **portfolio's** response MLE key — not the transacting merchant's. Specifically:

- `responseMlePrivateKeyFilePath` (or the `responseMlePrivateKey` object) must point to the **portfolio's** response MLE private key.
- `responseMleKID` — the KID value associated with the **portfolio's** response MLE certificate.
  - **Optional** when `responseMlePrivateKeyFilePath` points to a CyberSource-generated P12 file (SDK auto-fetches from P12).
  - **Required** when using PEM format files (`.pem`, `.key`, `.p8`) or when providing `responseMlePrivateKey` object directly.

```python
config = {
    # ... other MetaKey configuration ...
    'enableResponseMleGlobally': True,
    'responseMlePrivateKeyFilePath': '/path/to/portfolio/response/mle/private/key.p12',
    'responseMlePrivateKeyFilePassword': 'portfolio_private_key_password',
    # responseMleKID is optional when using a CyberSource-generated P12 file (auto-fetched from P12)
    # Required when using PEM files or responseMlePrivateKey object
    # 'responseMleKID': 'your_portfolio_response_mle_kid'
}
```

> **Important:** The response MLE private key (and KID, if applicable) must belong to the portfolio (parent account), since in MetaKey mode the portfolio is the transaction submitter and the response is encrypted using the portfolio's MLE certificate.

## How to Use

To get started using this SDK, it's highly recommended to download our sample code repository:

* [Cybersource Python Sample Code Repository (on GitHub)](https://github.com/CyberSource/cybersource-rest-samples-python)

In that repository, we have comprehensive sample code for all common uses of our API:

Additionally, you can find details and examples of how our API is structured in our API Reference Guide:

* [Developer Center API Reference](https://developer.cybersource.com/api/reference/api-reference.html)

The API Reference Guide provides examples of what information is needed for a particular request and how that information would be formatted. Using those examples, you can easily determine what methods would be necessary to include that information in a request using this SDK.

### Example using Sample Code Application

* Install the CyberSource Python SDK and add the SDK to your requirements.txt file.

* Configure your credentials in [Configuration Dictionary](https://github.com/CyberSource/cybersource-rest-samples-python/blob/master/data/Configuration.py#L5C5-L52C98).

* Create an instance of [ApiClient](https://github.com/CyberSource/cybersource-rest-samples-python/blob/c73bf7ae4a4826e4a6b652067cf38eb4affe765c/samples/Payments/Payments/simple-authorizationinternet.py#L94C50) and set the required properties in it.

* Use the created ApiClient instance to call CyberSource APIs. For example [SimpleAuthorizationInternet](https://github.com/CyberSource/cybersource-rest-samples-python/blob/c73bf7ae4a4826e4a6b652067cf38eb4affe765c/samples/Payments/Payments/simple-authorizationinternet.py#L95C9-L95C76).

For more detailed examples, refer to the [cybersource-rest-samples-python](https://github.com/CyberSource/cybersource-rest-samples-python) repository.

### Switching between the sandbox environment and the production environment

Cybersource maintains a complete sandbox environment for testing and development purposes. This sandbox environment is an exact duplicate of our production environment with the transaction authorization and settlement process simulated. By default, this SDK is configured to communicate with the sandbox environment. To switch to the production environment, set the `run_environment` property in the SDK Configuration.  See our sample at <https://github.com/CyberSource/cybersource-rest-samples-python/blob/master/data/Configuration.py>

```python
    # For TESTING use
    self.run_environment = "apitest.cybersource.com"
    # For PRODUCTION use
    # self.run_environment = "api.cybersource.com"
```

API credentials are different for each environment, so be sure to switch to the appropriate credentials when switching environments.

### Logging

[![Generic badge](https://img.shields.io/badge/LOGGING-NEW-GREEN.svg)](https://shields.io/)

Since v0.0.31, a new logging framework has been introduced in the SDK. This new logging framework makes use of Python's native logging, and standardizes the logging so that it can be integrated with the logging in the client application.

More information about this new logging framework can be found in this file : [Logging.md](Logging.md)

## Features

### Message Level Encryption (MLE) Feature
[![Generic badge](https://img.shields.io/badge/MLE-NEW-GREEN.svg)](https://shields.io/)

This feature provides an implementation of Message Level Encryption (MLE) for APIs provided by CyberSource, integrated within our SDK. This feature ensures secure communication by encrypting messages at the application level before they are sent over the network.

More information about this new MLE feature can be found in this file : [MLE.md](MLE.md)

## MetaKey Support

A Meta Key is a single key that can be used by one, some, or all merchants (or accounts, if created by a Portfolio user) in the portfolio.

The Portfolio or Parent Account owns the key and is considered the transaction submitter when a Meta Key is used, while the merchant owns the transaction.

MIDs continue to be able to create keys for themselves, even if a Meta Key is generated.

**For MetaKey configuration examples with all authentication types (HTTP Signature, JWT P12, and JWT Shared Secret), see the [Authentication](#authentication) section above.**

Further information on MetaKey can be found in [New Business Center User Guide](https://developer.cybersource.com/library/documentation/dev_guides/Business_Center/New_Business_Center_User_Guide.pdf).

## How to Contribute

* Fork the repo and create your branch from `master`.
* If you've added code that should be tested, add tests.
* Ensure the test suite passes.
* Submit your pull request! (Ensure you have [synced your fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) with the original repository before initiating the PR).

## Need Help?

For any help, you can reach out to us at our [Discussion Forum](https://community.developer.cybersource.com/t5/cybersource-APIs/bd-p/api).

## Disclaimer

CyberSource may allow Customer to access, use, and/or test a CyberSource product or service that may still be in development or has not been market-tested (“Beta Product”) solely for the purpose of evaluating the functionality or marketability of the Beta Product (a “Beta Evaluation”). Notwithstanding any language to the contrary, the following terms shall apply with respect to Customer’s participation in any Beta Evaluation (and the Beta Product(s)) accessed thereunder): The Parties will enter into a separate form agreement detailing the scope of the Beta Evaluation, requirements, pricing, the length of the beta evaluation period (“Beta Product Form”). Beta Products are not, and may not become, Transaction Services and have not yet been publicly released and are offered for the sole purpose of internal testing and non-commercial evaluation. Customer’s use of the Beta Product shall be solely for the purpose of conducting the Beta Evaluation. Customer accepts all risks arising out of the access and use of the Beta Products. CyberSource may, in its sole discretion, at any time, terminate or discontinue the Beta Evaluation. Customer acknowledges and agrees that any Beta Product may still be in development and that Beta Product is provided “AS IS” and may not perform at the level of a commercially available service, may not operate as expected and may be modified prior to release. CYBERSOURCE SHALL NOT BE RESPONSIBLE OR LIABLE UNDER ANY CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE RELATING TO A BETA PRODUCT OR THE BETA EVALUATION (A) FOR LOSS OR INACCURACY OF DATA OR COST OF PROCUREMENT OF SUBSTITUTE GOODS, SERVICES OR TECHNOLOGY, (B) ANY CLAIM, LOSSES, DAMAGES, OR CAUSE OF ACTION ARISING IN CONNECTION WITH THE BETA PRODUCT; OR (C) FOR ANY INDIRECT, INCIDENTAL OR CONSEQUENTIAL DAMAGES INCLUDING, BUT NOT LIMITED TO, LOSS OF REVENUES AND LOSS OF PROFITS.

## License

This repository is distributed under a proprietary license. See the provided [`LICENSE.txt`](/license.txt) file.
