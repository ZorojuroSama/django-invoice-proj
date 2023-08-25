from django.db import models
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import AuthenticationForm
    
# client model form

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=15)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self) -> str:
        return self.company_name
    

class Services(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    quantity = models.CharField(max_length=15)
    amount = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.company_name



class AddClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    comp_name = models.CharField(max_length=50)
    handle_by = models.CharField(max_length=100)
    email = models.CharField(max_length=15)
    phone = models.CharField(max_length=50)
    acc_no = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=50)
    bank = models.CharField(max_length=50)
    gst = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.company_name
    

    class Meta:
        db_table = 'providers'

