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


def get_reporting_resource_information():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "reporting", "coreservices",
                           "get_reporting_resource_information.csv"),
              newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:

            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = ReportDefinitionsApi(details_dict1)
                tcid = row[0]
                orgid = row[1]
                message = row[2]
                try:
                    api_response = api_instance.get_resource_v2_info(organization_id=orgid)

                    if (api_response):
                        writer.writerow(
                            [tcid, "GetReportingResourceInformation", "Passed:" + str(api_response.status), message

                                , datetime.datetime.now()])

                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):

                        writer.writerow(
                            [tcid, "GetReportingResourceInformation", "Failed:" + str(e.status), e.body,
                             datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "GetReportingResourceInformation", "Failed:" + str(e.status)
                                , (e.body), datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "GetReportingResourceInformation", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_reporting_resource_information()
