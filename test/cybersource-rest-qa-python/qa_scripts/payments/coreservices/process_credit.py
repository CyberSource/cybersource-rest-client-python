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


def process_a_credit():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "payments", "coreservices", "process_credit.csv"),
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
                api_instance = CreditApi(details_dict1)
                tcid = row[0]
                amount = row[1]
                message = row[2]

                request = CreateCreditRequest()
                client_reference = Ptsv2paymentsClientReferenceInformation()
                client_reference.code = "test_credits"
                request.client_reference_information = client_reference.__dict__

                order_information = Ptsv2paymentsOrderInformation()
                amount_details = Ptsv2paymentsOrderInformationAmountDetails()
                amount_details.total_amount = amount
                amount_details.currency = "usd"
                bill_to = Ptsv2paymentsOrderInformationBillTo()
                bill_to.country = "US"
                bill_to.first_name = "John"
                bill_to.last_name = "Doe"
                bill_to.address1 = "1 Market St"
                bill_to.phone_number = "9999999999"
                bill_to.postal_code = "48104-2201"
                bill_to.locality = "Ann Arbor"
                bill_to.administrative_area = "MI"
                bill_to.email = "test@cybs.com"
                order_information.amount_details = amount_details.__dict__
                order_information.bill_to = bill_to.__dict__

                payment_information = Ptsv2paymentsPaymentInformation()
                card_information = Ptsv2paymentsPaymentInformationCard()
                card_information.expiration_month = "03"
                card_information.expiration_year = "2031"
                card_information.type = "001"
                card_information.number = "4111111111111111"
                payment_information.card = card_information.__dict__
                request.order_information = order_information.__dict__
                request.payment_information = payment_information.__dict__
                message_body = json.dumps(request.__dict__)

                try:
                    api_response = api_instance.create_credit(message_body)
                    if (api_response):
                        api_response_data = json.loads(api_response.data)
                        # Assertion statements for Status,id,amountDetails
                        if api_response_data['status'] != utility.ConstantUtility.STATUS_PENDING:
                            writer.writerow([tcid, "ProcessCredit",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_AUTHORIZE, datetime.datetime.now()])
                        elif not (api_response_data['id']):
                            writer.writerow([tcid, "ProcessCredit",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_NULL_ID,
                                             datetime.datetime.now()])
                        else:
                            if api_response_data['creditAmountDetails']['creditAmount'] == amount:

                                writer.writerow([tcid, "ProcessCredit",
                                                 "Passed:" + str(api_response.status) + "-" + api_response_data[
                                                     'id'] + " "

                                                    , message, datetime.datetime.now()])
                            else:
                                writer.writerow([tcid, "ProcessCredit",
                                                 "Assertion Failed: " + str(api_response.status), message,
                                                 datetime.datetime.now()])

                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):
                        writer.writerow(
                            [tcid, "ProcessCredit", "Failed:" + str(e.status), json.loads(e.body)['message'],
                             datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "ProcessCredit", "Failed:" + str(e.status), json.loads(e.body)['message'],
                             datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "ProcessCredit", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    process_a_credit()
