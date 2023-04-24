from django.shortcuts import render

# Create your views here.
from app.models import *
from django import forms
from app.forms import *
from django.http import HttpResponse
def insert_Student(request):
    SDO=Studentforms()
    d={'SDO':SDO}
    
    if request.method=='POST':
        SFDO=Studentforms(request.POST)
        if SFDO.is_valid():
            SFDO.save()

            return HttpResponse('sucessfully inserted student data')






    
    return render(request,'insert_Student.html',d)