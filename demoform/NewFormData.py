from typing import Type
from django.shortcuts import render
from django import forms
# Create your views here.

org_choices=(("1","TCS"),("2","Infosys"),("3","Wipro"))

class NewFormData(forms.Form):
    first = forms.CharField(label="First Name")
    last = forms.CharField(label="Last Name")
    dob = forms.DateField(label="Date of Birth")
    organization = forms.ChoiceField(choices=org_choices)

    email=forms.EmailField(label="Email")