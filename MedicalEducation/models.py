from django.db import models

class trainerregistrationmodel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    qualification = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    authkey = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

def __str__(self):
    return self.email


class studentregistrationmodel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    college = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    authkey = models.CharField(max_length=100)
    status  = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class studentquerymodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    query = models.CharField(max_length=500)

    def __str__(self):
        return self.emailid

