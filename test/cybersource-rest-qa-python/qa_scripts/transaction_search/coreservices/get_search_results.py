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


def get_search_results():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "transaction_search", "coreservices",
                           "get_search_results.csv"), newline='') as csvfile:  # current folder is MainTestPackage
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
                input_id = row[1]
                message = row[2]
                id_input = input_id
                try:
                    api_response = api_instance.get_search(id_input)

                    if (api_response):
                        api_response_data = json.loads(api_response.data)

                        if api_response_data['searchId'] == input_id:

                            writer.writerow([tcid, "GetSearchResults",
                                             "Passed:" + str(api_response.status) + "-" + input_id + " "

                                                , message, datetime.datetime.now()])
                        else:
                            writer.writerow([tcid, "GetSearchResults",
                                             "Assertion Failed: " + str(api_response.status), message,
                                             datetime.datetime.now()])
                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):

                        writer.writerow(
                            [tcid, "GetSearchResults", "Failed:" + str(e.status), json.loads(e.body)['message'],
                             datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "GetSearchResults", "Failed:" + str(e.status)
                                , json.loads(e.body)['message'], datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "GetSearchResults", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_search_results()
