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


def tokenize_card():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "flex", "coreservices", "tokenize_card.csv"),
              newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:
            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = FlexTokenApi(details_dict1)

                tcid = row[0]
                keyid = row[1]
                message = row[2]

                tokenize_card = TokenizeRequest()
                card_info = Flexv1tokensCardInfo()
                tokenize_card.key_id = keyid

                card_info.card_expiration_year = "2031"
                card_info.card_number = "5555555555554444"
                card_info.card_type = "002"
                card_info.card_expiration_month = "03"
                tokenize_card.card_info = card_info.__dict__

                message_body = json.dumps(tokenize_card.__dict__)

                try:
                    api_response = api_instance.tokenize(tokenize_request=message_body)

                    if (api_response):
                        api_response_data = json.loads(api_response.data)
                        # Assertion statements for Status,Id

                        if not api_response_data['_embedded']['icsReply']['requestId']:
                            writer.writerow([tcid, "TokenizedCard",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.REQUEST_ID_NULL,
                                             datetime.datetime.now()])

                        else:
                            if api_response_data['keyId'] == keyid:

                                writer.writerow([tcid, "TokenizedCard",
                                                 "Passed:" + str(api_response.status) + "-" + api_response_data[
                                                     'keyId'] + " "

                                                    , message, datetime.datetime.now()])
                            else:
                                writer.writerow([tcid, "TokenizedCard",
                                                 "Assertion Failed: " + str(api_response.status), message,
                                                 datetime.datetime.now()])


                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):
                        writer.writerow(
                            [tcid, "TokenizedCard", "Failed:" + str(e.status),
                             json.loads(e.body)['responseStatus']['reason'], datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "TokenizedCard", "Failed:" + str(e.status),
                             json.loads(e.body)['responseStatus']['reason'], datetime.datetime.now()])

                except Exception as ex:

                    writer.writerow([tcid, "TokenizedCard", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    tokenize_card()
