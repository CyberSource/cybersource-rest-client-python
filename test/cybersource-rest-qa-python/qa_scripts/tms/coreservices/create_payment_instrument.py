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


def create_payment_instrument():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "tms", "coreservices",
                           "create_payment_instrument.csv"),
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
                message=row[2]

                # Setting the json message body
                request = Body2()
                card_info = Tmsv1paymentinstrumentsCard()
                card_info.expiration_month = "09"
                card_info.expiration_year = "2022"
                card_info.type = "visa"
                request.card = card_info.__dict__

                bill_to_info = Tmsv1paymentinstrumentsBillTo()
                bill_to_info.first_name = "John"
                bill_to_info.last_name = "Deo"
                bill_to_info.company = "CyberSource"
                bill_to_info.address1 = "12 Main Street"
                bill_to_info.address2 = "20 My Street"
                bill_to_info.locality = "Foster City"
                bill_to_info.administrative_area = "CA"
                bill_to_info.postal_code = "90200"
                bill_to_info.country = "US"
                bill_to_info.email = "john.smith@example.com"
                bill_to_info.phone_number = "555123456"
                request.bill_to = bill_to_info.__dict__

                instument_identifier = Tmsv1paymentinstrumentsInstrumentIdentifier()
                card_info = Tmsv1instrumentidentifiersCard()
                card_info.number = "4111111111111111"
                instument_identifier.card = card_info.__dict__
                request.instrument_identifier = instument_identifier.__dict__

                message_body = json.dumps(request.__dict__)


                try:
                    api_response = api_instance.tms_v1_paymentinstruments_post(
                        profile_id, message_body)

                    if (api_response):
                        api_response_data = json.loads(api_response.data)
                        if api_response_data['state'] != utility.ConstantUtility.STATUS_ACTIVE:
                            writer.writerow([tcid, "CreatePaymentsInstrument",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_ACTIVE, datetime.datetime.now()])
                        elif not (api_response_data['id']):
                            writer.writerow([tcid, "CreatePaymentsInstrument",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.MESSAGE_NULL_ID,
                                             datetime.datetime.now()])
                        else:
                            writer.writerow([tcid, "CreatePaymentsInstrument",
                                             "Passed:" + str(api_response.status) + "-" + api_response_data[
                                                 'id'] ,message

                                                , datetime.datetime.now()])


                except ApiException as e:

                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):
                        writer.writerow(
                            [tcid, "CreatePaymentsInstrument",
                             "Failed:" + str(e.status) , json.loads(e.body)['errors'][0]['message'], datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "CreatePaymentsInstrument",
                             "Failed:" + str(e.status), json.loads(e.body)['errors'][0]['message'], datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "CreatePaymentsInstrument", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    create_payment_instrument()
