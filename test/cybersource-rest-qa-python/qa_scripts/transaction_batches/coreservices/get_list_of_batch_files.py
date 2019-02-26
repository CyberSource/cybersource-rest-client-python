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


def get_list_of_batch_files():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "transaction_batches", "coreservices",
                           "get_list_of_batch_files.csv"), newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:

            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = TransactionBatchesApi(details_dict1)
                tcid = row[0]
                start_time = row[1]
                end_time = row[2]
                message = row[3]

                try:
                    api_response = api_instance.pts_v1_transaction_batches_get(start_time, end_time)

                    if (api_response):
                        writer.writerow([tcid, "GetListOfBatchFile",
                                         "Passed:" + str(api_response.status)

                                            , message, datetime.datetime.now()])


                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):

                        writer.writerow(
                            [tcid, "GetListOfBatchFile", "Failed:" + str(e.status),
                             json.loads(e.body)['message'] + "-" + message, datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "GetListOfBatchFile", "Failed:" + str(e.status)
                                , json.loads(e.body)['message'] + "-" + message, datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "GetListOfBatchFile", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_list_of_batch_files()
