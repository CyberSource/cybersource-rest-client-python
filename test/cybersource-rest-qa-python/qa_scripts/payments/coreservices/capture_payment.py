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


def capture_a_payment():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "payments", "coreservices", "capture_payment.csv"),
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
                api_instance = CaptureApi(details_dict1)
                tcid = row[0]
                paymentid = row[1]
                amount = row[2]
                message = row[3]

                payment_id = paymentid
                # Setting the json message body
                request = CapturePaymentRequest()
                client_reference = Ptsv2paymentsClientReferenceInformation()
                client_reference.code = "test_capture"
                request.client_reference_information = client_reference.__dict__

                amount_details = Ptsv2paymentsOrderInformationAmountDetails()
                amount_details.total_amount = amount
                amount_details.currency = "USD"
                order_information = Ptsv2paymentsOrderInformation()
                order_information.amount_details = amount_details.__dict__
                request.order_information = order_information.__dict__

                message_body = (json.dumps(request.__dict__))

                try:

                    api_response = api_instance.capture_payment(message_body, payment_id)

                    if (api_response):
                        api_response_data = json.loads(api_response.data)
                        # Assertion statements for Status,id,amountDetails
                        if api_response_data['status'] != utility.ConstantUtility.STATUS_PENDING:
                            writer.writerow([tcid, "CapturePayment",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_AUTHORIZE, datetime.datetime.now()])
                        elif not (api_response_data['id']):
                            writer.writerow([tcid, "CapturePayment",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_NULL_ID,
                                             datetime.datetime.now()])
                        else:
                            if api_response_data['orderInformation']['amountDetails']['totalAmount'] == amount:

                                writer.writerow([tcid, "CapturePayment",
                                                 "Passed:" + str(api_response.status) + "-" + api_response_data[
                                                     'id'] + " "

                                                    , message, datetime.datetime.now()])
                            else:
                                writer.writerow([tcid, "CapturePayment",
                                                 "Assertion Failed: " + str(api_response.status), message,
                                                 datetime.datetime.now()])


                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):
                        writer.writerow(
                            [tcid, "CapturePayment", "Failed:" + str(e.status), json.loads(e.body)['message'],
                             datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "CapturePayment", "Failed:" + str(e.status), json.loads(e.body)['message'],
                             datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "CapturePayment", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    capture_a_payment()
