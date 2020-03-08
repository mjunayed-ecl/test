# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Records
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    records = Records.objects.all()[:10]    #getting the first 10 records
    context = {
        'records': records
    }
    return render(request, 'records.html', context)

def details(request, id):
    #def record(self, id):
       # try:
            #return Records.objects.get(id=id)
        #except Records.DoesNotExist:
            #return False
    record = Records.objects.get(id=id)
    context = {
        'record': record
    }
    return render(request, 'details.html', context)
