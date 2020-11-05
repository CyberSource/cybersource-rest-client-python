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


def key_generation_no_enc():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "flex", "keygeneration_noenc.csv"),
              newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:
            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = KeyGenerationApi(details_dict1)

                tcid = row[0]
                encryption_type = row[1]
                message = row[2]

                # key_generation = KeyParameters()
                key_generation = GeneratePublicKeyRequest(encryption_type=encryption_type)
                message_body = json.dumps(key_generation.__dict__)

                # payment_request = AuthorizeNetRest.PaymentRequest("true", amount_detail, "", payment_instrument, baseaddress_bill_to, baseaddress_ship_to, ip, order, "", "", "", lineitem)
                try:
                    api_response = api_instance.generate_public_key(generate_public_key_request=message_body)

                    if (api_response):
                        api_response_data = json.loads(api_response.data)

                        if api_response_data['keyId']:

                            writer.writerow([tcid, "KeyGenerationNoEnc",
                                             "Passed:" + str(api_response.status) + "-" + api_response_data[
                                                 'keyId'] + " "

                                                , message, datetime.datetime.now()])
                        else:
                            writer.writerow([tcid, "KeyGenerationNoEnc",
                                             "Assertion Failed: " + str(api_response.status), message,
                                             datetime.datetime.now()])


                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):
                        writer.writerow(
                            [tcid, "KeyGenerationNoEnc", "Failed:" + str(e.status),
                             json.loads(e.body)['responseStatus']['reason'], datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "KeyGenerationNoEnc", "Failed:" + str(e.status),
                             json.loads(e.body)['responseStatus']['reason'], datetime.datetime.now()])

                except Exception as ex:

                    writer.writerow([tcid, "KeyGenerationNoEnc", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    key_generation_no_enc()
