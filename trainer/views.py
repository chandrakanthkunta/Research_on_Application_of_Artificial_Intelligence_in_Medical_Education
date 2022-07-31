import csv,os
import io
from msilib.schema import File, ListView
from pathlib import Path
from uuid import uuid4

from django.contrib import messages, auth
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

import trainer
from MedicalEducation import settings
from MedicalEducation.forms import UploadfileForm
from MedicalEducation.models import trainerregistrationmodel
from trainer.functions.functions import handle_uploaded_file


def trainerlogincheck(request):
    if request.method == 'POST':
        usid = request.POST.get('loginid')
        #print(usid)
        pswd = request.POST.get('password')
        #print(pswd)
        try:
            check = trainerregistrationmodel.objects.get(loginid=usid, password=pswd)
           # print('usid',usid,'pswd',pswd)
            request.session['traid'] = check.loginid
            request.session['loggeduser'] = check.name
            status = check.status
            #print("stu  id ", check.id)
            #if usid=='loginid' and pswd=='loggeduser':
            #if usid is not None:
            if status == "activated":
                request.session['email'] = check.email
                #auth.login(request, usid)
                return render(request,'trainer/trainerpage.html')
            else:
                messages.success(request, 'trainer is not activated')
                return render(request,'trainer.html')

            return render(request,'trainer/trainerpage.html')
        except Exception as e:
            print('Exception is ', str(e))
            messages.success(request,'Invalid user id and password')
        return render(request,'trainer.html')


"""def uploadfile(request):
    #print("Am Arumalla")
    if request.method == 'POST':
        #print("Was Up")
        upload = UploadfileForm(request.POST, request.FILES)
        if upload.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            upload.save()
            return HttpResponse("File Upload Sucessfully")
        else:
            upload = UploadfileForm()
            return render(request, 'uploadfile.html', {'form': upload})
    else:
        upload = UploadfileForm()
        return render(request,'uploadfile.html',{'form':upload})

    #return render(request, 'uploadfile.html', {})
    #return HttpResponseRedirect("uploadtrainingdata")"""

def uploadfile(request):
    if request.method == 'POST':
        form = UploadfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_list.html')
    else:
        form = UploadfileForm()
    return render(request, 'uploadfile.html', {'form': form})

def upload_list(request):
    files = File.objects.all()
    return render(request, 'upload_list.html', {'files': files})

"""def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
    return redirect('upload_list')"""

def uploadtrainingdata(request):
    return render(request,"uploadfile.html",{})



"""@permission_required('admin.can_add_log_entry')
def address_upload(request):
    template = "address_upload.html"
    
    prompt = {
        'order': 'Order of the csv should be name, email, address, healthcondition'
    }

    if request.method == "GET":
        return  render(request,template,prompt)
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string,delimiter=',',quotechar='|'):
        _, created = trainer.objects.update_or_create(
            name=column[0],
            email=column[1],
            address=column[2],
            healthcondition=column[3]
        )
    context = {}
    return render(request, template, context)"""
