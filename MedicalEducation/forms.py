import os
from uuid import uuid4

from django import forms
from django.forms import HiddenInput

from MedicalEducation.models import trainerregistrationmodel, studentregistrationmodel, studentquerymodel
from trainer.models import upload, patientsdata


class trainerregistrationform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    loginid = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    email = forms.EmailField(widget=forms.TextInput(),required=True)
    qualification = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    mobile = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    address = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    state = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    authkey = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    class Meta:
        model = trainerregistrationmodel
        fields = ['name','loginid','password','email','qualification','mobile','address','state','authkey','status' ]

class studentregistrationform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    loginid = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    email = forms.CharField(widget=forms.TextInput(), required=True)
    college = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    mobile = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    address = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    state = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    authkey = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    class Meta:
        model = studentregistrationmodel
        fields = ['name','loginid','password','email','college','mobile','address', 'state', 'authkey','status']



class studentqueryform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    email = forms.CharField(widget=forms.TextInput(), required=True)
    query = forms.CharField(widget=forms.TextInput(), required=True, max_length=500)

    class Meta:
        model = studentquerymodel
        fields = ['name', 'email', 'query']



class UploadfileForm(forms.ModelForm):
    #filename = forms.CharField(widget=forms.TextInput(),required=True, max_length=100)
    #description = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    #file = forms.FileField()
    class Meta:
        model = upload
        fields = ('filename','description','file')

"""class patientsdataForm(forms.ModelForm):

    class Meta:
        model = patientsdata
        fields = ('filename','description','file')"""