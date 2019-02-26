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


def download_file_with_file_identifier():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "secure_file_share", "coreservices",
                           "download_file_with_file_identifier.csv"),
              newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:

            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = SecureFileShareApi(details_dict1)
                tcid = row[0]
                org_id = row[1]
                field_id = row[2]
                message = row[3]
                try:
                    api_response = api_instance.get_file(field_id, organization_id=org_id)

                    if (api_response):
                        if api_response.data:

                            writer.writerow([tcid, "DownloadFileWithFileIdentifier",
                                             "Passed:" + str(api_response.status) + "-" + field_id + " "

                                                , message, datetime.datetime.now()])
                            # The Report obtained is being stored in a CSV file
                            f = open(os.path.join(os.getcwd(), "resources", "fileshare_report.csv"), "a+")
                            f.write("\n********************** Start Of Report***********************\n")
                            f.write(api_response.data)
                            f.write("\n********************** End Of Report*************************\n")
                            f.close()
                            print("File Downloaded at the Location :  " + os.path.join(os.getcwd(), "resources",
                                                                                       "fileshare_report.csv"))
                        else:
                            writer.writerow([tcid, "DownloadFileWithFileIdentifier",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.EMPTY_CONTENT,
                                             datetime.datetime.now()])
                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):

                        writer.writerow(
                            [tcid, "DownloadFileWithFileIdentifier", "Failed:" + str(e.status), message,
                             datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "DownloadFileWithFileIdentifier", "Failed:" + str(e.status)
                                , message, datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "DownloadFileWithFileIdentifier", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    download_file_with_file_identifier()
