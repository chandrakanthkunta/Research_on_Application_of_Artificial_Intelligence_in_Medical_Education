from django.contrib import messages
from django.shortcuts import render

from MedicalEducation.models import studentregistrationmodel
from trainer.models import upload


def studentlogincheck(request):
    if request.method == "POST":
        usid = request.POST.get('loginid')
        pswd = request.POST.get('password')
        try:
            check = studentregistrationmodel.objects.get(loginid=usid, password=pswd)
            request.session['stuid'] = check.loginid
            request.session['loggedstu'] = check.name
            status = check.status
            print("stu  id ",check.loginid)
            if status == "activated":
               #request.session['stuid'] = check.loginid
               request.session['email'] = check.email
               return render(request,'student/studentpage.html')
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request,'student.html')

            return render(request,'student/studentpage.html')
        except Exception as e:
            print('Exception is ',str(e))
    messages.success(request, 'Invalid Login Details')
    return render(request,'student.html')


def viewtrainerfilespage(request):
    filedata = upload.objects.all()
    return render(request,'student/viewtrainerfilesdata.html',{'object':filedata})