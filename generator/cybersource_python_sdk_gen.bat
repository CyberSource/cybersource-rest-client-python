mkdir %~dp0Python
cd %~dp0
java -jar swagger-codegen-cli-2.2.3.jar generate -t C:\swagger\swagger-codegen-2.2.3\swagger-codegen-2.2.3\modules\swagger-codegen\src\main\resources\cybersource-python-template -i cybersource-rest-spec.json -l python -o Python -c %~dp0cybersource-python-config.json

pause



