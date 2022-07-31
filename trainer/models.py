import os
from uuid import uuid4

from django.db import models

# Create your models here.
from django.db import models
from django.forms import FileField, HiddenInput


class upload(models.Model):
    #uuid = models.CharField(max_length=30)
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args,**kwargs)


class patientsdata(models.Model):

    name = models.CharField(max_length=100)
    #description = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return  self.name

class patientdatamodel(models.Model):

    Name = models.CharField(max_length=500)
    Email = models.CharField(max_length=300)
    DOB = models.CharField(max_length=300)
    Address = models.CharField(max_length=300)
    PAN = models.CharField(max_length=255)
    City = models.CharField(max_length=300)
    Country = models.CharField(max_length=300)

    def __str__(self):
        return self.Name,self.Email,self.DOB,self.Address,self.PAN,self.City,self.Country
