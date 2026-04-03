[![Generic badge](https://img.shields.io/badge/MLE-NEW-GREEN.svg)](https://shields.io/)

# Message Level Encryption (MLE) Feature

This feature provides an implementation of Message Level Encryption (MLE) for APIs provided by CyberSource, integrated within our SDK. This feature ensures secure communication by encrypting messages at the application level before they are sent over the network.

MLE supports both **Request Encryption** (encrypting outgoing request payloads) and **Response Decryption** (decrypting incoming response payloads).

## Authentication Requirements

- **Request MLE**: Only supported with `JWT (JSON Web Token)` authentication type
- **Response MLE**: Only supported with `JWT (JSON Web Token)` authentication type

<br/>

## Configuration

## 1. Request MLE Configuration

### 1.1 Global Request MLE Configuration

Configure global settings for request MLE using these properties in your `merchantConfig`:

#### (i) Primary Configuration

- **Variable**: `enableRequestMLEForOptionalApisGlobally`
- **Type**: `Boolean`
- **Default**: `False`
- **Description**: Enables request MLE globally for all APIs that have optional MLE support when set to `True`.

---

#### (ii) Deprecated Configuration (Backward Compatibility)

- **Variable**: `useMLEGlobally` ⚠️ **DEPRECATED**
- **Type**: `Boolean`
- **Default**: `False`
- **Description**: **DEPRECATED** - Use `enableRequestMLEForOptionalApisGlobally` instead. This field is maintained for backward compatibility and will be used as an alias for `enableRequestMLEForOptionalApisGlobally`.

---

#### (iii) Advanced Configuration

- **Variable**: `disableRequestMLEForMandatoryApisGlobally`
- **Type**: `Boolean`
- **Default**: `False`
- **Description**: Disables request MLE for APIs that have mandatory MLE requirement when set to `True`.

---

### 1.2 Request MLE Certificate Configuration [Optional Params]

#### (i) Certificate File Path (Optional)

- **Variable**: `mleForRequestPublicCertPath`
- **Type**: `str`
- **Optional**: `True`
- **Description**: Path to the public certificate file used for request encryption. Supported formats: `.pem`, `.crt`.
  - **Note**: This parameter is optional when using JWT authentication. If not provided, the request MLE certificate will be automatically fetched from the JWT authentication P12 file using the `requestMleKeyAlias`.

---

#### (ii) Key Alias Configuration (Optional)

- **Variable**: `requestMleKeyAlias`
- **Type**: `str`
- **Optional**: `True`
- **Default**: `CyberSource_SJC_US`
- **Description**: Key alias used to retrieve the MLE certificate from the certificate file. When `mleForRequestPublicCertPath` is not provided, this alias is used to fetch the certificate from the JWT authentication P12 file. If not specified, the SDK will automatically use the default value `CyberSource_SJC_US`.

---

#### (iii) Deprecated Key Alias (Backward Compatibility) (Optional)

- **Variable**: `mleKeyAlias` ⚠️ **DEPRECATED**
- **Type**: `str`
- **Optional**: `True`
- **Default**: `CyberSource_SJC_US`
- **Description**: **DEPRECATED** - Use `requestMleKeyAlias` instead. This field is maintained for backward compatibility and will be used as an alias for `requestMleKeyAlias`.

<br/>

## 2. Response MLE Configuration

### 2.1 Global Response MLE Configuration

- **Variable**: `enableResponseMleGlobally`
- **Type**: `Boolean`
- **Default**: `False`
- **Description**: Enables response MLE globally for all APIs that support MLE responses when set to `True`.

---

### 2.2 Response MLE Private Key Configuration

#### (i) Option 1: Provide Private Key Object

- **Variable**: `responseMlePrivateKey`
- **Type**: `PrivateKey` (Python cryptography library object)
- **Description**: Direct private key object for response decryption.

---

#### (ii) Option 2: Provide Private Key File Path

- **Variable**: `responseMlePrivateKeyFilePath`
- **Type**: `str`
- **Description**: Path to the private key file. Supported formats: `.p12`, `.pfx`, `.pem`, `.key`, `.p8`. Recommendation: use encrypted private key (password protection) for MLE response.

---

#### (iii) Private Key File Password

- **Variable**: `responseMlePrivateKeyFilePassword`
- **Type**: `str`
- **Description**: Password for the private key file (required for `.p12/.pfx` files or encrypted private keys).

---

### 2.3 Response MLE Additional Configuration

- **Variable**: `responseMleKID`
- **Type**: `str`
- **Optional**: `True` (when using CyberSource-generated P12 file)
- **Required**: `True` (when using PEM files or private key object)
- **Description**: Key ID value for the MLE response certificate (provided in merchant portal).
  - **Note**: This parameter is optional when `responseMlePrivateKeyFilePath` points to a CyberSource-generated P12 file. If not provided, the SDK will automatically fetch the Key ID from the P12 file. If provided, the SDK will use the user-provided value instead of the auto-fetched value.
  - **Required** when using PEM format files (`.pem`, `.key`, `.p8`) or when providing `responseMlePrivateKey` object directly.

<br/>

## 3. API-level MLE Control for Request and Response MLE

### Map Configuration

- **Variable**: `mapToControlMLEonAPI`
- **Type**: `Dict[str, str]` or `Dict[str, bool]`
- **Description**: Overrides global MLE settings for specific APIs. The key is the API function name, and the value controls both request and response MLE.
- **Example**: `{"api_function_name": "true::true"}`

#### Structure of Values in Map:

(i) **"requestMLE::responseMLE"** - Control both request and response MLE
   - `"true::true"` - Enable both request and response MLE
   - `"false::false"` - Disable both request and response MLE
   - `"true::false"` - Enable request MLE, disable response MLE
   - `"false::true"` - Disable request MLE, enable response MLE
   - `"::true"` - Use global setting for request, enable response MLE
   - `"true::"` - Enable request MLE, use global setting for response
   - `"::false"` - Use global setting for request, disable response MLE
   - `"false::"` - Disable request MLE, use global setting for response

(ii) **"requestMLE"** or **Boolean** - Control request MLE only (response uses global setting)
   - `"true"` or `True` - Enable request MLE
   - `"false"` or `False` - Disable request MLE

<br/>

## 4. Example Configurations

### (i) Minimal Request MLE Configuration

```python
# Dictionary-based configuration - Uses defaults (most common scenario)
configuration_dictionary = {
    "enableRequestMLEForOptionalApisGlobally": True
    # Both mleForRequestPublicCertPath and requestMleKeyAlias are optional
    # SDK will use JWT P12 file with default alias "CyberSource_SJC_US"
}

# OR

# Class-based configuration
class Configuration:
    def __init__(self):
        self.enableRequestMLEForOptionalApisGlobally = True
        # Both mleForRequestPublicCertPath and requestMleKeyAlias are optional
        # SDK will use JWT P12 file with default alias "CyberSource_SJC_US"
```

### (ii) Request MLE with Deprecated Parameters (Backward Compatibility)

```python
# Using deprecated parameters - still supported but not recommended
configuration_dictionary = {
    "useMLEGlobally": True,  # Deprecated - use enableRequestMLEForOptionalApisGlobally
    "mleKeyAlias": "Custom_Key_Alias"  # Deprecated - use requestMleKeyAlias
}

# OR

class Configuration:
    def __init__(self):
        self.useMLEGlobally = True  # Deprecated - use enableRequestMLEForOptionalApisGlobally
        self.mleKeyAlias = "Custom_Key_Alias"  # Deprecated - use requestMleKeyAlias
```

### (iii) Request MLE with Custom Key Alias

```python
# Dictionary-based configuration - With custom key alias only
configuration_dictionary = {
    "enableRequestMLEForOptionalApisGlobally": True,
    "requestMleKeyAlias": "Custom_Key_Alias"
    # Will fetch from JWT P12 file using custom alias
}

# OR

class Configuration:
    def __init__(self):
        self.enableRequestMLEForOptionalApisGlobally = True
        self.requestMleKeyAlias = "Custom_Key_Alias"
        # Will fetch from JWT P12 file using custom alias
```

### (iv) Request MLE with Separate Certificate File

```python
# Dictionary-based configuration - With separate MLE certificate file
configuration_dictionary = {
    "enableRequestMLEForOptionalApisGlobally": True,
    "mleForRequestPublicCertPath": "/path/to/public/cert.pem",
    "requestMleKeyAlias": "Custom_Key_Alias",
    # API-specific control
    "mapToControlMLEonAPI": {
        "create_payment": "true",      # Enable request MLE for this API
        "capture_payment": "false"     # Disable request MLE for this API
    }
}

# OR

class Configuration:
    def __init__(self):
        self.enableRequestMLEForOptionalApisGlobally = True
        self.mleForRequestPublicCertPath = "/path/to/public/cert.pem"
        self.requestMleKeyAlias = "Custom_Key_Alias"
        # API-specific control
        self.mapToControlMLEonAPI = {
            "create_payment": "true",      # Enable request MLE for this API
            "capture_payment": "false"     # Disable request MLE for this API
        }
```

### (v) Response MLE Configuration with Private Key File

```python
# Dictionary-based configuration with CyberSource-generated P12 file
configuration_dictionary = {
    "enableResponseMleGlobally": True,
    "responseMlePrivateKeyFilePath": "/path/to/private/key.p12",
    "responseMlePrivateKeyFilePassword": "password",
    # responseMleKID is optional for CyberSource-generated P12 files - SDK will auto-fetch if not provided
    # "responseMleKID": "your-key-id",  # Optional - overrides auto-fetched value
    # API-specific control
    "mapToControlMLEonAPI": {
        "create_payment": "::true"  # Enable response MLE only for this API
    }
}

# OR

class Configuration:
    def __init__(self):
        self.enableResponseMleGlobally = True
        self.responseMlePrivateKeyFilePath = "/path/to/private/key.p12"
        self.responseMlePrivateKeyFilePassword = "password"
        # responseMleKID is optional for CyberSource-generated P12 files - SDK will auto-fetch if not provided
        # self.responseMleKID = "your-key-id"  # Optional - overrides auto-fetched value
        # API-specific control
        self.mapToControlMLEonAPI = {
            "create_payment": "::true"  # Enable response MLE only for this API
        }
```

```python
# Dictionary-based configuration with PEM file (responseMleKID is required)
configuration_dictionary = {
    "enableResponseMleGlobally": True,
    "responseMlePrivateKeyFilePath": "/path/to/private/key.pem",
    "responseMleKID": "your-key-id",  # Required for PEM files
    # API-specific control
    "mapToControlMLEonAPI": {
        "create_payment": "::true"  # Enable response MLE only for this API
    }
}

# OR

class Configuration:
    def __init__(self):
        self.enableResponseMleGlobally = True
        self.responseMlePrivateKeyFilePath = "/path/to/private/key.pem"
        self.responseMleKID = "your-key-id"  # Required for PEM files
        # API-specific control
        self.mapToControlMLEonAPI = {
            "create_payment": "::true"  # Enable response MLE only for this API
        }
```

### (vi) Response MLE Configuration with Private Key Object

```python
# Load private key programmatically using Python cryptography library
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Load private key from file
with open("/path/to/private/key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,  # or b"password" if encrypted
        backend=default_backend()
    )

# Dictionary-based configuration (responseMleKID is required)
configuration_dictionary = {
    "enableResponseMleGlobally": True,
    "responseMlePrivateKey": private_key,
    "responseMleKID": "your-key-id"  # Required when using private key object
}

# Note: When using private key object, you cannot use dictionary-based configuration alone.
# You need to set the private key separately after creating the configuration object.
```

### (vii) Both Request and Response MLE Configuration

```python
# Dictionary-based configuration
configuration_dictionary = {
    # Request MLE settings (minimal - uses defaults)
    "enableRequestMLEForOptionalApisGlobally": True,
    
    # Response MLE settings (with CyberSource-generated P12 file)
    "enableResponseMleGlobally": True,
    "responseMlePrivateKeyFilePath": "/path/to/private/key.p12",
    "responseMlePrivateKeyFilePassword": "password",
    # responseMleKID is optional for CyberSource-generated P12 files
    # "responseMleKID": "your-key-id",  # Optional - overrides auto-fetched value
    
    # API-specific control for both request and response
    "mapToControlMLEonAPI": {
        "create_payment": "true::true",     # Enable both request and response MLE for this API
        "capture_payment": "false::true",   # Disable request, enable response MLE for this API
        "refund_payment": "true::false",    # Enable request, disable response MLE for this API
        "create_credit": "::true"           # Use global request setting, enable response MLE for this API
    }
}

# OR

class Configuration:
    def __init__(self):
        # Request MLE settings (minimal - uses defaults)
        self.enableRequestMLEForOptionalApisGlobally = True
        
        # Response MLE settings (with CyberSource-generated P12 file)
        self.enableResponseMleGlobally = True
        self.responseMlePrivateKeyFilePath = "/path/to/private/key.p12"
        self.responseMlePrivateKeyFilePassword = "password"
        # responseMleKID is optional for CyberSource-generated P12 files
        # self.responseMleKID = "your-key-id"  # Optional - overrides auto-fetched value
        
        # API-specific control for both request and response
        self.mapToControlMLEonAPI = {
            "create_payment": "true::true",     # Enable both request and response MLE for this API
            "capture_payment": "false::true",   # Disable request, enable response MLE for this API
            "refund_payment": "true::false",    # Enable request, disable response MLE for this API
            "create_credit": "::true"           # Use global request setting, enable response MLE for this API
        }
```

### (viii) Mixed Configuration (New and Deprecated Parameters)

```python
# Example showing both new and deprecated parameters (deprecated will be used as aliases)
configuration_dictionary = {
    # If both are set with same value, it works fine
    "enableRequestMLEForOptionalApisGlobally": True,
    "useMLEGlobally": True,  # Deprecated but same value
    
    # If both are set with different values, it will cause ValueError
    # "enableRequestMLEForOptionalApisGlobally": True,
    # "useMLEGlobally": False,  # This would cause an error
    
    # Key alias - new parameter takes precedence if both are provided
    "requestMleKeyAlias": "New_Alias",
    "mleKeyAlias": "Old_Alias"  # This will be ignored
}

# OR

class Configuration:
    def __init__(self):
        # If both are set with same value, it works fine
        self.enableRequestMLEForOptionalApisGlobally = True
        self.useMLEGlobally = True  # Deprecated but same value
        
        # Key alias - new parameter takes precedence if both are provided
        self.requestMleKeyAlias = "New_Alias"
        self.mleKeyAlias = "Old_Alias"  # This will be ignored
```

<br/>

## 5. JSON Configuration Examples

### (i) Minimal Request MLE

```json
{
  "merchantConfig": {
    "enableRequestMLEForOptionalApisGlobally": true
  }
}
```

### (ii) Request MLE with Deprecated Parameters

```json
{
  "merchantConfig": {
    "useMLEGlobally": true,
    "mleKeyAlias": "Custom_Key_Alias"
  }
}
```

### (iii) Request MLE with Custom Configuration

```json
{
  "merchantConfig": {
    "enableRequestMLEForOptionalApisGlobally": true,
    "mleForRequestPublicCertPath": "/path/to/public/cert.pem",
    "requestMleKeyAlias": "Custom_Key_Alias",
    "mapToControlMLEonAPI": {
      "create_payment": "true",
      "capture_payment": "false"
    }
  }
}
```

### (iv) Response MLE Only

```json
{
  "merchantConfig": {
    "enableResponseMleGlobally": true,
    "responseMlePrivateKeyFilePath": "/path/to/private/key.p12",
    "responseMlePrivateKeyFilePassword": "password",
    "_comment": "responseMleKID is optional for CyberSource-generated P12 files",
    "responseMleKID": "your-key-id",
    "mapToControlMLEonAPI": {
      "create_payment": "::true"
    }
  }
}
```

```json
{
  "merchantConfig": {
    "enableResponseMleGlobally": true,
    "responseMlePrivateKeyFilePath": "/path/to/private/key.pem",
    "_comment": "responseMleKID is required for PEM files",
    "responseMleKID": "your-key-id",
    "mapToControlMLEonAPI": {
      "create_payment": "::true"
    }
  }
}
```

### (v) Both Request and Response MLE

```json
{
  "merchantConfig": {
    "enableRequestMLEForOptionalApisGlobally": true,
    "enableResponseMleGlobally": true,
    "responseMlePrivateKeyFilePath": "/path/to/private/key.p12",
    "responseMlePrivateKeyFilePassword": "password",
    "_comment": "responseMleKID is optional for CyberSource-generated P12 files - SDK will auto-fetch if not provided",
    "responseMleKID": "your-key-id",
    "mapToControlMLEonAPI": {
      "create_payment": "true::true",
      "capture_payment": "false::true",
      "refund_payment": "true::false",
      "create_credit": "::true"
    }
  }
}
```

<br/>

## 6. Supported Private Key File Formats

For Response MLE private key files, the following formats are supported:

- **PKCS#12**: `.p12`, `.pfx` (requires password)
- **PEM**: `.pem`, `.key`, `.p8` (supports both encrypted and unencrypted)

<br/>

## 7. Important Notes

### (i) Request MLE

- Both `mleForRequestPublicCertPath` and `requestMleKeyAlias` are **optional** parameters
- If `mleForRequestPublicCertPath` is not provided, the SDK will automatically fetch the MLE certificate from the JWT authentication P12 file
- If `requestMleKeyAlias` is not provided, the SDK will use the default value `CyberSource_SJC_US`
- The SDK provides flexible configuration options: you can use defaults, customize the key alias only, or provide a separate certificate file
- If `enableRequestMLEForOptionalApisGlobally` is set to `True`, it enables request MLE for all APIs that have optional MLE support
- APIs with mandatory MLE requirements are enabled by default unless `disableRequestMLEForMandatoryApisGlobally` is set to `True`
- If `mapToControlMLEonAPI` doesn't contain a specific API, the global setting applies
- For HTTP Signature authentication, request MLE will fall back to non-encrypted requests with a warning

### (ii) Response MLE

- Response MLE requires either `responseMlePrivateKey` object OR `responseMlePrivateKeyFilePath` (not both)
- The `responseMleKID` parameter behavior:
  - **Optional** when `responseMlePrivateKeyFilePath` points to a CyberSource-generated P12 file (SDK auto-fetches from P12)
  - **Required** when using PEM format files (`.pem`, `.key`, `.p8`)
  - **Required** when using `responseMlePrivateKey` object directly
  - When both auto-fetched and user-provided values exist, the user-provided value takes precedence
- If an API expects a mandatory MLE response but the map specifies non-MLE response, the API might return an error
- Both the private key object and file path approaches are mutually exclusive

### (iii) Backward Compatibility

- `useMLEGlobally` is **deprecated** but still supported as an alias for `enableRequestMLEForOptionalApisGlobally`
- `mleKeyAlias` is **deprecated** but still supported as an alias for `requestMleKeyAlias`
- If both new and deprecated parameters are provided with the **same value**, it works fine
- If both new and deprecated parameters are provided with **different values**, it will cause a `ValueError`
- When both new and deprecated parameters are provided, the **new parameter takes precedence**

### (iv) API-level Control Validation

- The `mapToControlMLEonAPI` values are validated for proper format
- Invalid formats (empty values, multiple separators, non-boolean values) will cause configuration errors
- Empty string after `::` separator will use global defaults
- The map supports both `Dict[str, str]` format (new) and `Dict[str, bool]` format (backward compatible)
- Boolean values in the map only apply to request MLE; use string format with `::` separator to control both request and response

### (v) Configuration Validation

- The SDK performs comprehensive validation of MLE configuration parameters
- Conflicting values between new and deprecated parameters will result in `ValueError`
- File path validation is performed for certificate and private key files
- Invalid boolean values in `mapToControlMLEonAPI` will cause parsing errors

<br/>

## 8. Error Handling

The SDK provides specific error messages for common MLE issues:

- Invalid private key for response decryption
- Missing certificates for request encryption
- Invalid file formats or paths
- Authentication type mismatches (MLE requires JWT authentication)
- Configuration validation errors
- Conflicting parameter values between new and deprecated fields
- Invalid format in `mapToControlMLEonAPI` values
- Missing required `responseMleKID` for PEM files or private key objects

<br/>

## 9. Sample Code Repository

For comprehensive examples and sample implementations, please refer to:
[CyberSource Python Sample Code Repository (on GitHub)](https://github.com/CyberSource/cybersource-rest-samples-python)

Specifically, see the MLE feature samples at:
[MLE Feature Samples](https://github.com/CyberSource/cybersource-rest-samples-python/tree/master/samples/MLEFeature)

<br/>

## 10. Additional Information

### (i) API Support

- MLE is designed to support specific APIs that have been enabled for encryption
- Support can be extended to additional APIs based on requirements and updates
- Check the API documentation to see which APIs support MLE (optional or mandatory)

### (ii) Using the SDK

To use the MLE feature in the SDK, configure the `merchantConfig` object as shown above and pass it to the SDK initialization. The SDK will automatically handle encryption and decryption based on your configuration.

### (iii) Configuration Methods

The SDK supports multiple configuration approaches:

**Dictionary-based configuration:**
```python
config_dict = {
    "enableRequestMLEForOptionalApisGlobally": True,
    "enableResponseMleGlobally": True,
    # ... other parameters
}
merchant_config = MerchantConfiguration()
merchant_config.set_merchantconfig(config_dict)
```

**Class-based configuration:**
```python
class Configuration:
    def __init__(self):
        self.enableRequestMLEForOptionalApisGlobally = True
        self.enableResponseMleGlobally = True
        # ... other parameters
```

**JSON file configuration:**
```python
import json

with open('cybs.json', 'r') as config_file:
    config_dict = json.load(config_file)

merchant_config = MerchantConfiguration()
merchant_config.set_merchantconfig(config_dict)
```

### (iv) Migration from Deprecated Parameters

If you're currently using deprecated parameters, here's how to migrate:

```python
# OLD (Deprecated)
configuration_dictionary = {
    "useMLEGlobally": True,
    "mleKeyAlias": "Custom_Alias"
}

# NEW (Recommended)
configuration_dictionary = {
    "enableRequestMLEForOptionalApisGlobally": True,
    "requestMleKeyAlias": "Custom_Alias"
}
```

The deprecated parameters will continue to work but are not recommended for new implementations.

### (v) Private Key Object Usage

When using `responseMlePrivateKey` with a private key object, you need to load the key using Python's `cryptography` library:

```python
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# For PEM files
with open("/path/to/key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=b"password" if encrypted else None,
        backend=default_backend()
    )

# For PKCS12 files
from cryptography.hazmat.primitives.serialization import pkcs12

with open("/path/to/key.p12", "rb") as key_file:
    private_key, certificate, additional_certs = pkcs12.load_key_and_certificates(
        key_file.read(),
        b"password",
        backend=default_backend()
    )
```

<br/>

## 11. Contact

For any issues or further assistance, please open an issue on the GitHub repository or contact our support team.
