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


def create_instrument_identifier():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "tms", "coreservices",
                           "create_instrument_identifier.csv"),
              newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:
            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = InstrumentIdentifiersApi(details_dict1)

                tcid = row[0]
                prev_transaction_id = row[1]
                profile_id = row[2]
                message = row[3]

                # Setting the json message body
                request = Body()
                card_info = Tmsv1instrumentidentifiersCard()
                card_info.number = "123456789098765"
                request.card = card_info.__dict__

                processing_info = Tmsv1instrumentidentifiersProcessingInformation()
                authorize_options_info = Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptions()
                initiator = Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiator()
                merchant_initiated_info = Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction()
                merchant_initiated_info.previous_transaction_id = prev_transaction_id
                initiator.merchant_initiated_transaction = merchant_initiated_info.__dict__
                authorize_options_info.initiator = initiator.__dict__
                processing_info.authorization_options = authorize_options_info.__dict__
                request.processing_information = processing_info.__dict__

                message_body = json.dumps(request.__dict__)

                # payment_request = AuthorizeNetRest.PaymentRequest("true", amount_detail, "", payment_instrument, baseaddress_bill_to, baseaddress_ship_to, ip, order, "", "", "", lineitem)
                try:
                    api_response = api_instance.tms_v1_instrumentidentifiers_post(
                        profile_id, body=message_body)

                    if (api_response):
                        api_response_data = json.loads(api_response.data)
                        # Assertion statements for Status,id
                        if api_response_data['state'] != utility.ConstantUtility.STATUS_ACTIVE:
                            writer.writerow([tcid, "CreateInstrumentIdentifier",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_ACTIVE, datetime.datetime.now()])
                        elif not (api_response_data['id']):
                            writer.writerow([tcid, "CreateInstrumentIdentifier",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_NULL_ID,
                                             datetime.datetime.now()])
                        else:
                            if api_response_data['processingInformation']['authorizationOptions'][
                                'initiator']['merchantInitiatedTransaction'][
                                'previousTransactionId'] == prev_transaction_id:
                                # QA modification
                                writer.writerow([tcid, "CreateInstrumentIdentifier",
                                                 "Passed:" + str(api_response.status) + "-" + api_response_data[
                                                     'id'], message

                                                    , datetime.datetime.now()])

                            else:
                                writer.writerow(
                                    [tcid,
                                     "CreateInstrumentIdentifier", "Assertion Failed: " + str(api_response.status),
                                     message,

                                     datetime.datetime.now()])


                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):
                        writer.writerow(
                            [tcid, "CreateInstrumentIdentifier", "Failed:" + str(e.status),
                             json.loads(e.body)['errors'][0]['message'], datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "CreateInstrumentIdentifier", "Failed:" + str(e.status),
                             json.loads(e.body)['errors'][0]['message'], datetime.datetime.now()])

                except Exception as ex:

                    writer.writerow([tcid, "CreateInstrumentIdentifier", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    create_instrument_identifier()
