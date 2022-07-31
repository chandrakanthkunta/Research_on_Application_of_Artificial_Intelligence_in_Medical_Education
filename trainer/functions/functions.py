"""def handle_uploaded_file(f):
    with open('trainer/static/upload/'+f.name,'wb+')as destination:
        for chunk in f.chunks():
            destination.write(chunk)
import os

def handle_uploaded_file(f):
    path = "trainer/static/upload/+f.name"
    format = f.file + f.transaction_uuid + f.file_extension
    return os.path.join(path,format)"""

import csv


def handle_uploaded_file(f):
    with open('C:/Users/DELL/Desktop/patientdata.csv') as f:
        q = csv.reader(f)
        row1 = next(q)
        print(row1)