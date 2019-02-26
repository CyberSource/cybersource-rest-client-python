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


def process_a_payout():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "payouts", "coreservices", "process_payout.csv"),
              newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:
            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = ProcessAPayoutApi(details_dict1)
                tcid = row[0]

                client_ref_infocode = row[1]
                business_appid = row[2]
                amount = row[3]
                message = row[4]
                # Setting the json message body
                request = PtsV2PayoutsPostResponse()
                client_reference = Ptsv2paymentsClientReferenceInformation()
                client_reference._code = client_ref_infocode
                request.client_reference_information = client_reference.__dict__

                sender_info = Ptsv2payoutsSenderInformation()
                account_info = Ptsv2payoutsSenderInformationAccount()
                sender_info.reference_number = "1234567890"
                sender_info.address1 = "900 Metro Center Blvd.900"
                sender_info.country_code = "US"
                sender_info.locality = "Foster City"
                sender_info.name = "Thomas Jefferson"
                sender_info.administrative_area = "CA"
                account_info.funds_source = "05"
                account_info.number = "1234567890123456789012345678901234"
                sender_info.account = account_info.__dict__
                request.sender_information = sender_info.__dict__

                processing_info = Ptsv2payoutsProcessingInformation()
                processing_info.commerce_indicator = "internet"
                processing_info.business_application_id = business_appid
                processing_info.network_routing_order = "ECG"

                payouts_details = Ptsv2payoutsProcessingInformationPayoutsOptions()
                payouts_details.retrieval_reference_number = "123456789012"
                payouts_details.acquirer_bin = "567890124"
                processing_info.reconciliation_id = "1087488702VIAQNSPQ"
                processing_info.payouts_options = payouts_details.__dict__
                request.processing_information = processing_info.__dict__

                order_information = Ptsv2payoutsOrderInformation()
                amount_details = Ptsv2payoutsOrderInformationAmountDetails()
                amount_details.total_amount = amount
                amount_details.currency = "USD"
                order_information.amount_details = amount_details.__dict__
                request.order_information = order_information.__dict__

                merchant_details = Ptsv2payoutsMerchantInformation()
                merchant_details.category_code = 123
                merchant_description = Ptsv2payoutsMerchantInformationMerchantDescriptor()
                merchant_description.country = "US"
                merchant_description.postal_code = "94440"
                merchant_description.locality = "FC"
                merchant_description.name = "Thomas"
                merchant_description.administrative_area = "CA"
                merchant_details.merchant_descriptor = merchant_description.__dict__
                request.merchant_information = merchant_details.__dict__

                payment_info = Ptsv2payoutsPaymentInformation()
                card_details = Ptsv2payoutsPaymentInformationCard()
                card_details.expiration_year = "2025"
                card_details.number = "4111111111111111"
                card_details.expiration_month = "12"
                card_details.type = "001"
                card_details.source_account_type = "CH"
                payment_info.card = card_details.__dict__
                request.payment_information = payment_info.__dict__

                recepient_info = Ptsv2payoutsRecipientInformation()
                recepient_info.first_name = "John"
                recepient_info.last_name = "Doe"
                recepient_info.address1 = "Paseo Padre Boulevard"
                recepient_info.locality = "Foster City"
                recepient_info.administrative_area = "CA"
                recepient_info.postal_code = "94400"
                recepient_info.phone_number = "6504320556"
                recepient_info.country = "US"
                recepient_info.date_of_birth = "19801009"
                request.recipient_information = recepient_info.__dict__
                message_body = json.dumps(request.__dict__)

                try:
                    api_response = api_instance.oct_create_payment(message_body)

                    if (api_response):
                        api_response_data = json.loads(api_response.data)
                        # Assertion statements for Status,id,amountDetails
                        if api_response_data['status'] != utility.ConstantUtility.STATUS_ACCEPTED:
                            writer.writerow([tcid, "ProcessPayout",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_AUTHORIZE, datetime.datetime.now()])
                        elif not (api_response_data['id']):
                            writer.writerow([tcid, "ProcessPayout",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_NULL_ID,
                                             datetime.datetime.now()])

                        else:
                            if api_response_data['orderInformation']['amountDetails']['totalAmount'] == amount:

                                writer.writerow([tcid, "ProcessPayout",
                                                 "Passed:" + str(api_response.status) + "-" + api_response_data[
                                                     'id'] + " "

                                                    , message, datetime.datetime.now()])
                            else:
                                writer.writerow([tcid, "ProcessPayout",
                                                 "Assertion Failed: " + str(api_response.status), message,
                                                 datetime.datetime.now()])



                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):
                        writer.writerow(
                            [tcid, "ProcessPayout", "Failed:" + str(e.status), json.loads(e.body)['message'],
                             datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "ProcessPayout", "Failed:" + str(e.status), json.loads(e.body)['message'],
                             datetime.datetime.now()])
                except Exception as ex:
                    print(ex)
                    writer.writerow([tcid, "ProcessPayout", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    process_a_payout()
