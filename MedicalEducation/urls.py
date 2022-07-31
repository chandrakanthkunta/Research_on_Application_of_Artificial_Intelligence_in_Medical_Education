"""MedicalEducation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from student.views import studentlogincheck,viewtrainerfilespage
from trainer.models import patientsdata
from trainer.views import trainerlogincheck, uploadfile, uploadtrainingdata,  upload_list
from .views import index, trainer, student, adminlogin, adminloginaction, logout, trainerregistration, \
    viewadmintrainerspage, studentregistration, viewadminstudentpage, activatestudents, studentbase, \
    activatetrainers, trainerpage, viewadminfilespage, studentsendquery, viewstudentqueries, \
    adminbase, storecsvdata, viewadmincsvpage, viewpatienpage
from django.conf.urls import url



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index, name="index"),
    url(r'^index/', index, name="index"),
    url(r'^adminlogin/', adminlogin, name="adminlogin"),
    url(r'^trainer/', trainer, name="trainer"),
    url(r'^student/', student, name="student"),
    url(r'^studentbase/',studentbase, name="studentbase"),
    url(r'^adminbase/',adminbase, name="adminbase"),
    url(r'^adminloginaction/', adminloginaction, name="adminloginaction"),
    url(r'^trainerregistration/', trainerregistration, name="trainerregistration"),
    url(r'^trainerlogincheck/', trainerlogincheck, name="trainerlogincheck"),
    url(r'^trainerpage/', trainerpage, name="trainerpage"),
    url(r'^viewadmintrainerspage/',viewadmintrainerspage,name="viewadmintrainerspage"),
    url(r'^activatetrainers/$', activatetrainers, name="activatetrainers"),
    url(r'^studentlogincheck/', studentlogincheck, name="studentlogincheck"),
    url(r'^studentregistration/', studentregistration, name="studentregistration"),
    url(r'^viewadminstudentpage/',viewadminstudentpage,name="viewadminstudentpage"),
    url(r'^activatestudents/$', activatestudents, name="activatestudents"),
    url(r'^uploadfile/',uploadfile,name="uploadfile"),
    url(r'^uploadtrainingdata/',uploadtrainingdata,name="uploadtrainingdata"),
    url(r'^viewadminfilespage/',viewadminfilespage,name="viewadminfilespage"),
    url(r'^viewtrainerfilespage/',viewtrainerfilespage,name="viewtrainerfilespage"),
    url(r'^storecsvdata/',storecsvdata,name="storecsvdata"),
    url(r'^viewadmincsvpage/',viewadmincsvpage,name="viewadmincsvpage"),
    url(r'^viewpatienpage/',viewpatienpage,name="viewpatienpage"),
    url(r'^upload_list/',upload_list,name="upload_list"),
    url(r'^studentsendquery',studentsendquery,name="studentsendquery"),
    url(r'^viewstudentqueries/',viewstudentqueries,name="viewstudentqueries"),
    url(r'^logout/', logout, name="logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
