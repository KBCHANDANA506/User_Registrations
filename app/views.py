from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from app.models import *


def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)

        if ufd.is_valid and pfd.is_valid():
            NSUFO=ufd.save(commit=False)
            NSUFO.set_password(ufd.cleaned_data['password'])
            NSUFO.save()
            NSPFO=pfo.save(commit=False)
            NSPFO.username=NSUFO
            NSPFO.save()
            return  HttpResponse('Registration done successfully..!')
        else:
            return HttpResponse("Data is invalid")



    return render(request,'registration.html',d)
