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


def create_search_request():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "transaction_search", "coreservices",
                           "create_search_request.csv"), newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:

            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = SearchTransactionsApi(details_dict1)
                tcid = row[0]
                request_name = row[1]
                request_query = row[2]
                message = row[3]

                # Setting the json message body
                create_search_request = TssV2TransactionsPostResponse()
                create_search_request.save = "false"
                create_search_request.name = request_name
                create_search_request.timezone = "America/Chicago"
                create_search_request.query = request_query
                create_search_request.offset = 0
                create_search_request.limit = 100
                create_search_request.sort = "id:asc, submitTimeUtc:asc"
                message_body = json.dumps(create_search_request.__dict__)

                try:
                    api_response = api_instance.create_search(message_body)

                    if (api_response):
                        api_response_data = json.loads(api_response.data)
                        # Assertion statements for Status,name#which id

                        if api_response_data['name'] == request_name:

                            writer.writerow([tcid, "CreateSearchRequest",
                                             "Passed:" + str(api_response.status)

                                                , message, datetime.datetime.now()])
                        else:
                            writer.writerow([tcid, "CreateSearchRequest",
                                             "Assertion Failed: " + str(api_response.status), message,
                                             datetime.datetime.now()])
                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):

                        writer.writerow(
                            [tcid, "CreateSearchRequest", "Failed:" + str(e.status), json.loads(e.body)['message'],
                             datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "CreateSearchRequest", "Failed:" + str(e.status)
                                , json.loads(e.body)['message'], datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "CreateSearchRequest", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    create_search_request()
