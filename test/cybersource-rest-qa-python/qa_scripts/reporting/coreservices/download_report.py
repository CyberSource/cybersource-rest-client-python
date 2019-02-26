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


def download_reports():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "reporting", "coreservices", "download_report.csv"),
              newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:

            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = ReportDownloadsApi(details_dict1)
                tcid = row[0]
                orgid = row[1]
                report_name = row[2]
                report_date = row[3]
                message = row[4]

                try:
                    api_response = api_instance.download_report(report_date, report_name, organization_id=orgid)

                    if (api_response):

                        if api_response.data:

                            writer.writerow(
                                [tcid, "DownloadReport", "Passed:" + str(api_response.status) + "-" + orgid + " ",
                                 message

                                    , datetime.datetime.now()])
                            # The Report obtained is being stored in a CSV file
                            f = open(os.path.join(os.getcwd(), "resources", "download_report.csv"), "a+")
                            f.write("\n********************** Start Of Report***********************\n")
                            f.write(api_response.data)
                            f.write("\n********************** End Of Report*************************\n")
                            f.close()
                            print("File Downloaded at the Location :  " + os.path.join(os.getcwd(), "resources",
                                                                                       "download_report.csv"))
                        else:
                            writer.writerow([tcid, "DownloadReport",
                                             "Assertion Failed: " + str(api_response.status),
                                             utility.ConstantUtility.EMPTY_CONTENT,
                                             datetime.datetime.now()])

                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):

                        writer.writerow(
                            [tcid, "DownloadReport", "Failed:" + str(e.status), message, datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "DownloadReport", "Failed:" + str(e.status), message, datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "DownloadReport", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    download_reports()
