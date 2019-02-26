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


def process_a_payment(flag):
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "payments", "coreservices", "process_payment.csv"),
              newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)

        for row in reader:

            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = PaymentsApi(details_dict1)
                tcid = row[0]
                amount = row[1]
                message = row[2]

                request = CreatePaymentRequest()
                client_reference = Ptsv2paymentsClientReferenceInformation()
                client_reference.code = "test_payment"
                request.client_reference_information = client_reference.__dict__

                processing_info = Ptsv2paymentsProcessingInformation()

                if flag:
                    processing_info.capture = "true"

                request.processing_information = processing_info.__dict__

                aggregator_info = Ptsv2paymentsAggregatorInformation()
                sub_merchant = Ptsv2paymentsAggregatorInformationSubMerchant()
                sub_merchant.card_acceptor_id = "1234567890"
                sub_merchant.country = "US"
                sub_merchant.phone_number = "650-432-0000"
                sub_merchant.address1 = "900 Metro Center"
                sub_merchant.postal_code = "94404-2775"
                sub_merchant.locality = "Foster City"
                sub_merchant.name = "Visa Inc"
                sub_merchant.administrative_area = "CA"
                sub_merchant.region = "PEN"
                sub_merchant.email = "test@cybs.com"
                aggregator_info.sub_merchant = sub_merchant.__dict__
                aggregator_info.name = "V-Internatio"
                aggregator_info.aggregator_id = "123456789"
                request.aggregator_information = aggregator_info.__dict__

                order_information = Ptsv2paymentsOrderInformation()
                bill_to = Ptsv2paymentsOrderInformationBillTo()
                bill_to.country = "US"
                bill_to.last_name = "Doe"
                bill_to.address2 = "1 Market St"
                bill_to.address1 = "201 S. Division St."
                bill_to.postal_code = "48104-2201"
                bill_to.locality = "Ann Arbor"
                bill_to.administrative_area = "MI"
                bill_to.first_name = "John"
                bill_to.phone_number = "999999999"
                bill_to.district = "MI"
                bill_to.building_number = "123"
                bill_to.company = "Visa"
                bill_to.email = "test@cybs.com"

                amount_details = Ptsv2paymentsOrderInformationAmountDetails()
                amount_details.total_amount = amount
                amount_details.currency = "USD"

                order_information.bill_to = bill_to.__dict__
                order_information.amount_details = amount_details.__dict__

                payment_info = Ptsv2paymentsPaymentInformation()
                card = Ptsv2paymentsPaymentInformationCard()
                card.expiration_year = "2031"
                card.number = "5555555555554444"
                card.security_code = "123"
                card.expiration_month = "12"
                card.type = "002"
                payment_info.card = card.__dict__
                request.payment_information = payment_info.__dict__

                request.order_information = order_information.__dict__

                message_body = json.dumps(request.__dict__)
                try:
                    api_response = api_instance.create_payment(message_body)
                    api_response_data = json.loads(api_response.data)
                    if (api_response):
                        # Assertion statements for Status,id,amountDetails
                        if api_response_data['status'] != utility.ConstantUtility.STATUS_AUTHORIZED:
                            writer.writerow([tcid, "ProcessPayment",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_AUTHORIZE, datetime.datetime.now()])
                        elif not (api_response_data['id']):
                            writer.writerow([tcid, "ProcessPayment",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_NULL_ID,
                                             datetime.datetime.now()])
                        else:
                            if api_response_data['orderInformation']['amountDetails']['authorizedAmount'] == amount:

                                writer.writerow([tcid, "ProcessPayment",
                                                 "Passed:" + str(api_response.status) + "-" + api_response_data[
                                                     'id'] + " "

                                                    , message, datetime.datetime.now()])
                            else:
                                writer.writerow([tcid, "ProcessPayment",
                                                 "Assertion Failed: " + str(api_response.status), message,
                                                 datetime.datetime.now()])
                except ApiException as e:
                    size = len(row)

                    if (row[size - 1] == "Negative" and str(e.status) == '400'):
                        writer.writerow(
                            [tcid, "ProcessPayment", "Failed:" + str(e.status), json.loads(e.body)['message'],
                             datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "ProcessPayment", "Failed:" + str(e.status), json.loads(e.body)['message'],
                             datetime.datetime.now()])
                except Exception as ex:
                    writer.writerow([tcid, "ProcessPayment", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    process_a_payment(False)
