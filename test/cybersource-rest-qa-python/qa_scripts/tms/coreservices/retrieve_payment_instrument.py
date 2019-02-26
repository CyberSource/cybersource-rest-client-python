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


def retrieve_payment_instrument():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "tms", "coreservices",
                           "retrieve_payment_instrument.csv"),
              newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:
            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = PaymentInstrumentsApi(details_dict1)
                tcid = row[0]
                profile_id = row[1]
                id = row[2]
                message = row[3]
                try:
                    # Create A Customer Address
                    api_response = api_instance.tms_v1_paymentinstruments_token_id_get(
                        profile_id, id)

                    if (api_response):
                        api_response_data = json.loads(api_response.data)
                        if api_response_data['state'] != utility.ConstantUtility.STATUS_ACTIVE:
                            writer.writerow([tcid, "RetrievePaymentInstrument",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_ACTIVE, datetime.datetime.now()])
                        elif not (row[2]) in api_response_data["_links"]["self"]["href"]:

                            writer.writerow([tcid, "RetrievePaymentInstrument",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.TOKEN_ID_MISMATCH,
                                             datetime.datetime.now()])
                        else:
                            writer.writerow([tcid, "RetrievePaymentInstrument",
                                             "Passed:" + str(api_response.status) + "-" + id, message

                                                , datetime.datetime.now()])
                except ApiException as e:
                    size = len(row);
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):
                        writer.writerow(
                            [tcid, "RetrievePaymentInstrument", "Failed:" + str(e.status),
                             json.loads(e.body)['errors'][0]['message'], datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "RetrievePaymentInstrument", "Failed:" + str(e.status),
                             json.loads(e.body)['errors'][0]['message'], datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "RetrievePaymentInstrument", ex, datetime.datetime.now()]);


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    retrieve_payment_instrument()
