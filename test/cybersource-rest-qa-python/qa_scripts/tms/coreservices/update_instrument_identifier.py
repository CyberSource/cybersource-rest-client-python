from __future__ import print_function
import os
import sys
import csv
from CyberSource import *
from CyberSource.rest import ApiException
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()
util_file = os.path.join(os.getcwd(), "qa_scripts", "utility", "constant_utility.py")
utility = SourceFileLoader("module.name", util_file).load_module()
import datetime


def update_instrument_identifier():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "tms", "coreservices",
                           "update_instrument_identifier.csv"),
              newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:
            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                # Reading Merchant details from Configuration file
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = InstrumentIdentifierApi(details_dict1)
                tcid = row[0]
                profileid = row[1]
                tokenid = row[2]
                message = row[3]
                # Setting the json message body
                request = Body1()
                processing_info = Tmsv1instrumentidentifiersProcessingInformation()
                authorize_options_info = Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptions()
                initiator = Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiator()
                merchant_initiated_info = Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction()

                merchant_initiated_info.previous_transaction_id = "123456789012345"
                initiator.merchant_initiated_transaction = merchant_initiated_info.__dict__
                authorize_options_info.initiator = initiator.__dict__
                processing_info.authorization_options = authorize_options_info.__dict__
                request.processing_information = processing_info.__dict__

                message_body = json.dumps(request.__dict__)

                try:
                    # Create A Customer Address
                    api_response = api_instance.tms_v1_instrumentidentifiers_token_id_patch(
                        profileid, tokenid, body=message_body)

                    if (api_response):
                        api_response_data = json.loads(api_response.data)
                        if api_response_data['state'] != utility.ConstantUtility.STATUS_ACTIVE:
                            writer.writerow([tcid, "UpdateInstrumentIdentifier",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_ACTIVE, datetime.datetime.now()])
                        elif not (row[2]) in api_response_data["_links"]["self"]["href"]:

                            writer.writerow([tcid, "UpdateInstrumentIdentifier",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.TOKEN_ID_MISMATCH,
                                             datetime.datetime.now()])
                        else:
                            writer.writerow([tcid, "UpdateInstrumentIdentifier",
                                             "Passed:" + str(api_response.status) + "-" + api_response_data['id'],
                                             message

                                                , datetime.datetime.now()])
                except ApiException as e:
                    size = len(row);
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):
                        writer.writerow(
                            [tcid, "UpdateInstrumentIdentifier", "Failed:" + str(e.status),
                             json.loads(e.body)['errors'][0]['message'], datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "UpdateInstrumentIdentifier", "Failed:" + str(e.status),
                             json.loads(e.body)['errors'][0]['message'], datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "UpdateInstrumentIdentifier", ex, datetime.datetime.now()]);


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    update_instrument_identifier()
