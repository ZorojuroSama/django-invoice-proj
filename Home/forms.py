from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Services, AddClient
# from .forms import *


class UserLogin(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        labels = {
            'username':'userId',
            'password':'password'
        }



def __init__(self,*args,**kwargs):
    super(UserLogin, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['password'].widget.attrs['class'] = 'form-control'





class ClientForm(forms.ModelForm):
    class Meta:
        model = AddClient
        fields = ['client', 'comp_name', 'handle_by','email', 'gst', 'phone','acc_no','ifsc','bank']

def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['client'].widget.attrs['class'] = 'form-control'
        self.fields['comp_name'].widget.attrs['class'] = 'form-control'
        self.fields['handle_by'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['acc_no'].widget.attrs['class'] = 'form-control'
        self.fields['ifsc'].widget.attrs['class'] = 'form-control'  
        self.fields['bank'].widget.attrs['class'] = 'form-control'
        self.fields['gst'].widget.attrs['class'] = 'form-control'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['client', 'description', 'quantity', 'amount']

    def __ini__(self, *args, **qwargs):
        super(Services, self).__init__(*args, **qwargs)

        self.fields['client'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['class'] = 'form-control'