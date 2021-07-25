from typing import Type
from django.shortcuts import render
from django import forms
# Create your views here.
from .NewFormData import NewFormData




def index(request):
    context={}
    context['form']=NewFormData()
    return render(request,"demoform/newform.html",context)

    

