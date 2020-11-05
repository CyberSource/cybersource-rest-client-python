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


def create_report_subscription():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "reporting", "coreservices",
                           "create_report_subscription_for_report_name_by_organization.csv"),
              newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:

            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = ReportSubscriptionsApi(details_dict1)
                tcid = row[0]
                definition_name = row[1]
                reportname = row[2]
                message = row[4]
                # Setting the json message body
                request = RequestBody(report_definition_name=definition_name,
                                      report_fields=["Request.RequestID", "Request.TransactionDate",
                                                     "Request.MerchantID"], report_name=reportname)

                request.report_fields = ["Request.RequestID", "Request.TransactionDate", "Request.MerchantID"]
                request.report_mime_type = "application/xml"
                request.report_frequency = "WEEKLY"
                request.timezone = "GMT"
                request.start_time = "0825"
                request.start_day = 1
                message_body = json.dumps(request.__dict__)

                try:
                    api_response = api_instance.create_subscription(message_body, report_name=request.report_name)

                    if (api_response):
                        writer.writerow([tcid, "CreateReportSubscriptionForReportNameByOrganization",
                                         "Passed:" + str(api_response.status), message

                                            , datetime.datetime.now()])

                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):

                        writer.writerow(
                            [tcid, "CreateReportSubscriptionForReportNameByOrganization", "Failed:" + str(e.status),
                             json.loads(e.body)['message'] + ":" + message, datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "CreateReportSubscriptionForReportNameByOrganization", "Failed:" + str(e.status),
                             json.loads(e.body)['message'] + ":" + message, datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow(
                        [tcid, "CreateReportSubscriptionForReportNameByOrganization", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    create_report_subscription()
