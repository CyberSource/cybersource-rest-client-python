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


def delete_subscriptions_report():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "reporting", "coreservices",
                           "delete_subscription_of_report_name_by_organization.csv"),
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
                report_name = row[1]
                message = row[2]

                try:
                    api_response = api_instance.delete_subscription(report_name)

                    if (api_response):
                        writer.writerow(
                            [tcid, "DeleteSubscriptionOfReportNameByOrganization", "Passed:" + str(api_response.status),
                             message

                                , datetime.datetime.now()])

                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):

                        writer.writerow(
                            [tcid, "DeleteSubscriptionOfReportNameByOrganization", "Failed:" + str(e.status),
                             json.loads(e.body)['message'] + ":" + message, datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "DeleteSubscriptionOfReportNameByOrganization", "Failed:" + str(e.status),
                             json.loads(e.body)['message'] + ":" + message, datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "DeleteSubscriptionOfReportNameByOrganization", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    delete_subscriptions_report()
