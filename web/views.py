#coding:utf-8
from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse
from web.models import Asset,UserInfo
from pip._vendor.distlib._backport.tarfile import pwd
# Create your views here.

def AssetList(request):
    asset_list = Asset.objects.all()
    print asset_list
    result =  render_to_response('assetlist.html',{'data':asset_list,'user':'alex'})
    return result
def Login(request):
    if request.method == 'POST':
       user = request.POST.get('username',None)
       pwd = request.POST.get('password',None)
       print user,pwd
       result = UserInfo.objects.filter(username=user,password=pwd).count()
       if result == 1:
           return HttpResponse('登陆成功')
       else:
           print user,pwd 
           return render_to_response('login.html',{'status':'用户名或密码错误'})
    else:
       return render_to_response('login.html')

    
    