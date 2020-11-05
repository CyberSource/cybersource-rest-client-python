import csv
import os

path=os.getcwd()
with open(os.path.join(os.getcwd(), "qa_scripts","csv_files", "test_report", "testresults.csv"), 'a', newline='') as csvfile:     #a in place of w for append
    writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)


with open(os.path.join(os.getcwd(), "qa_scripts","csv_files", "driver", "driver.csv"), newline='') as csvfile:  #current folder is MainTestPackage
    reader=csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)
    for row in reader:
            if(row[2]=="1"):
                fileName=row[1]
                print("opening the file: ",path+"/"+row[0]+"/"+fileName+".py")
                exec(open(path+"/"+row[0]+"/"+fileName+".py").read())


