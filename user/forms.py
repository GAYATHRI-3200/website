from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    
    #phone=forms.IntegerField(required=True)
    #city=forms.CharField(required=True)

    class Meta:
        model=User
        fields=(
            'username',    
            'email',
            #'phone',
            'password1',
            'password2',
            
        )
    def save(self,commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.username=self.cleaned_data['username']
        #user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        user.password1=self.cleaned_data['password1']
        user.password2=self.cleaned_data['password2']
        #user.phone=self.cleaned_data['phone']
        #user.city=self.cleaned_data['city']
        if commit:
            user.save()
        return user

 

