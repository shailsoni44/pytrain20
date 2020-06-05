from django import forms
from django.forms import ModelForm
from .models import register


class registerform(forms.ModelForm):
    class Meta:
        model=register
        fields="__all__"
        # include=['name','email','Repeat_email','password','re_password']
        # exclude=[]
        labels = {
            'name':'Enter your first and last name',
            'email':'Enter your email address',
            'Repeat_email':'Please re-enter email',
            'password':'Enter your password',
            're_password':'Enter your password again',
        }