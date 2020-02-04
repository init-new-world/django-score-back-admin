# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import student
import json

def index(request):
    return render(request,'index.html')

def add(request):
    return render(request,'add.html')

def search(request):
    return render(request,'search.html')

def apiadd(request):
    if request.method == 'POST':
        student.objects.create(name=request.POST['name'],num=int(request.POST['num']),chi=int(request.POST['chi']),che=int(request.POST['che']),phy=int(request.POST['phy']),mat=int(request.POST['mat']),eng=int(request.POST['eng']),allscore=int(request.POST['chi'])+int(request.POST['che'])+int(request.POST['phy'])+int(request.POST['mat'])+int(request.POST['eng']))
    return HttpResponse("Dream will soon be a wasteland.")

def apisearch(request):
    if request.method == 'POST':
        ret = {'status':True,'data':None}
        try:
            userlist = student.objects.all()
            ret['data']=serializers.serialize('json',userlist)
        except Exception:
            ret['status'] = False
        return HttpResponse(json.dumps(ret))
    return HttpResponse("My glory belongs to me.")

def apicng(request):
    if request.method == 'POST':
        student.objects.filter(id=request.POST['pk']).update(name=request.POST['name'],num=int(request.POST['num']),chi=int(request.POST['chi']),che=int(request.POST['che']),phy=int(request.POST['phy']),mat=int(request.POST['mat']),eng=int(request.POST['eng']),allscore=int(request.POST['chi'])+int(request.POST['che'])+int(request.POST['phy'])+int(request.POST['mat'])+int(request.POST['eng']))
    return HttpResponse("What hurts you could make you better.")

def apidel(request):
    if request.method == 'POST':
        print student.objects.get(id=request.POST['pk']).delete()
    return HttpResponse("My dream will everlasting.")

def analysis(request):
    return render(request,'analysis.html')

def searchif(request):
    return render(request,'search-if.html')

# Create your views here.
