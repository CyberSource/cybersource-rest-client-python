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


def void_a_credit():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "payments", "coreservices", "void_credit.csv"),
              newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:
            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = VoidApi(details_dict1)
                tcid = row[0]
                creditid = row[1]
                response_body_status = row[2]
                message = row[3]
                credit_id = creditid

                # Setting the json message body
                request = VoidCreditRequest()
                client_reference = Ptsv2paymentsClientReferenceInformation()
                client_reference._code = "test_credit_void"
                request.client_reference_information = client_reference.__dict__
                message_body = json.dumps(request.__dict__)

                # payment_request = AuthorizeNetRest.PaymentRequest("true", amount_detail, "", payment_instrument, baseaddress_bill_to, baseaddress_ship_to, ip, order, "", "", "", lineitem)
                try:
                    api_response = api_instance.void_credit(message_body, credit_id)

                    if (api_response):
                        api_response_data = json.loads(api_response.data)
                        # Assertion statements for Status,id
                        if api_response_data['status'] != utility.ConstantUtility.STATUS_VOIDED:
                            writer.writerow([tcid, "VoidCredit",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_AUTHORIZE, datetime.datetime.now()])
                        elif not (api_response_data['id']):
                            writer.writerow([tcid, "VoidCredit",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_NULL_ID,
                                             datetime.datetime.now()])
                        else:
                            writer.writerow([tcid, "VoidCredit",
                                             "Passed:" + str(api_response.status) + "-" + api_response_data[
                                                 'id'] + " "

                                                , message, datetime.datetime.now()])


                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):
                        writer.writerow(
                            [tcid, "VoidCredit", "Failed:" + str(e.status), json.loads(e.body)['message'],
                             datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "VoidCredit", "Failed:" + str(e.status), json.loads(e.body)['message'],
                             datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "VoidCredit", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    void_a_credit()
