import csv
from collections import defaultdict
from io import TextIOWrapper
from os import name
from tokenize import Name

from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from random import randint

from django.template.context_processors import request

from MedicalEducation.forms import trainerregistrationform, studentregistrationform, studentqueryform
from MedicalEducation.models import trainerregistrationmodel, studentregistrationmodel, studentquerymodel
from trainer.models import upload, patientdatamodel


def index(request):
    context = {}
    return render(request, "index.html", context)

def adminbase(request):
    return render(request,'adminbase.html')

def studentbase(request):
    return render(request,'studentbase.html')

def trainerpage(request):
    context = {}
    return  render(request,"trainer/trainerpage.html",context)

def adminlogin(request):
    return render(request,'adminlogin.html')

def adminloginaction(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return render(request,'admins/adminhome.html')
            else:
                messages.success(request, 'Invalid user id and password')
    #messages.success(request, 'Invalid user id and password')
    return render(request,'adminlogin.html')

def logout(request):
    return render(request,'index.html')

def trainer(request):
    context = {}
    return render(request, "trainer.html", context)

def trainerregistration(request):
    if request.method == 'POST':
        form = trainerregistrationform(request.POST)
        if form.is_valid():
            #print("Hai Meghana")
            form.save()
            messages.success(request, 'you are successfully registred')
            return HttpResponseRedirect('trainer')
        else:
            print('Invalid')
    else:
        form = trainerregistrationform()
    return render(request,"trainerregistration.html",{'form':form})

def studentregistration(request):
    if request.method == 'POST':
        form = studentregistrationform(request.POST)
        if form.is_valid():
            #print("Hai Meghana")
            form.save()
            messages.success(request, 'you are successfully registred')
            return HttpResponseRedirect('student')
        else:
            print('Invalid')
    else:
        form = studentregistrationform()
    return render(request,"studentregistration.html",{'form':form})

def studentsendquery(request):
    if request.method == 'POST':
        form = studentqueryform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'you are successfully send message')
            return HttpResponseRedirect('studentsendquery')
        else:
            print('Invalid')
    else:
        form = studentqueryform()
    return render(request,"studentsendquery.html",{'form':form})

def viewadmintrainerspage(request):
    trainerdata = trainerregistrationmodel.objects.all()
    return render(request,'admins/viewtrainersdata.html',{'object':trainerdata})

def viewadminstudentpage(request):

    studentdata = studentregistrationmodel.objects.all()
    return render(request,'admins/viewstudentsdata.html',{'object':studentdata})

def viewadminfilespage(request):
    filedata = upload.objects.all()
    return render(request,'admins/viewfilesdata.html',{'object':filedata})

def viewadmincsvpage(request):
    csvdata = patientdatamodel.objects.all()
    return render(request,'admins/viewcsvdata.html',{'object':csvdata})

def viewpatienpage(request):
    patientdata = patientdatamodel.objects.all()
    return render(request,'student/viewpatientdata.html',{'object':patientdata})



def viewstudentqueries(request):
    sendquery = studentquerymodel.objects.all()
    return render(request,'trainer/viewsendquery.html',{'object':sendquery})


def activatetrainers(request):
    if request.method=='GET':
        usid = request.GET.get('usid')
        authkey = random_with_N_digits(8)
        status = 'activated'
        print("USID = ",usid,authkey,status)
        trainerregistrationmodel.objects.filter(id=usid).update(authkey=authkey , status=status)
        trainerdata = trainerregistrationmodel.objects.all()
        return render(request,'admins/viewtrainersdata.html',{'object':trainerdata})

def activatestudents(request):
    if request.method=='GET':
        pid = request.GET.get('pid')
        authkey = random_with_N_digits(8)
        status = 'activated'
        print("PID = ",pid,authkey,status)
        studentregistrationmodel.objects.filter(id=pid).update(authkey=authkey , status=status)
        studentdata = studentregistrationmodel.objects.all()
        return render(request,'admins/viewstudentsdata.html',{'object':studentdata})


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def student(request):
    context = {}
    return render(request, "student.html", context)



def storecsvdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        csvfile =TextIOWrapper( request.FILES['file'])
        columns = defaultdict(list)
        #with open('trainer/static/upload/patientdata.csv') as csvfile:
            #storecsvdata = csv.reader(csvfile)
            #row1 = next(storecsvdata)
            #row2 = next(storecsvdata)
            #print(row1)
            #print(row2)
        storecsvdata = csv.DictReader(csvfile)
            #row1 = next(storecsvdata)
        for row1 in storecsvdata:
                name = row1["Name"]
                email = row1["Email"]
                dob = row1["DOB"]
                address = row1["Address"]
                pan = row1["PAN"]
                city = row1["City"]
                country = row1["Country"]
                patientdatamodel.objects.create(Name=name, Email=email, DOB=dob,
                                                Address=address, PAN=pan, City=city,
                                                Country=country)
                #for (k, v) in row1.items():
                    #var = columns[k].append(v)
                    #print("Values ",var," k  value ",k," V value ",v)

                    #patientdatamodel.objects.create(Name=columns['Name'], Email=columns['Email'], DOB=columns['DOB'], Address=columns['Address'], PAN=columns['PAN'], City=columns['City'], Country=columns['Country'], )

        #patientdatamodel.objects.create(Name=columns['Name'],Email=columns['Email'],DOB=columns['DOB'],Address=columns['Address'],PAN=columns['PAN'],City=columns['City'],Country=columns['Country'],)
        #print(columns['Name'])
        #print(columns['Email'])
        #print(columns['DOB'])

        print("Name is ",csvfile)
        return HttpResponse('CSV file successful uploaded')
    else:

        return render(request, 'patientsdata.html', {})