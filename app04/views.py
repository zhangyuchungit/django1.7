#coding:utf-8
from django.shortcuts import render,render_to_response
#coding:utf-8
from django.http.response import HttpResponse
from app04.models import UserInfo,UserList
# Create your views here.

def Ajax(request):
    if request.method == 'POST':
        print request.POST
        return HttpResponse('ok')
    else:
        print HttpResponse('not ok')
        return render_to_response('./app04/ajax.html')

def Add(request):
        UserInfo.objects.create(username='zzz',age=10 )
        return HttpResponse('create OK')
def Update(request):
    return HttpResponse('update OK')

def Userlist(request):
    result = UserInfo.objects.all()
    return render_to_response('./app04/userlist.html',{'result':result})
def Register(request):
    if request.method == "POST":
        username = request.POST.get("username",None)        
        password = request.POST.get("password",None)
        print username,password
        UserList.objects.create(username=username,password=password)
        result = UserList.objects.filter(username=username,password=password).count()
        print result
        if result <= 1:
           return render_to_response('./app04/registerok.html',{'status':'注册成功'})
        else:
            return render_to_response('./app04/register.html',{'status':'用户已被注册'})
    else:
        return render_to_response('./app04/register.html')

def Index(request):
    return render_to_response('./app04/index.html')
def ChouTi(request):
    return render_to_response('./app04/chouti.html')
def Login(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        result = UserList.objects.filter(username=username,password=password).count()
        if result == 1:
            return render_to_response('./app04/index.html')
        else:
            return render_to_response('./app04/login.html',{'status':'用户或者密码错误'})
    else:
        return render_to_response('./app04/login.html')
def UpLoad(request):
    if request.method == "POST":
        rev_num1 = request.POST.get("rev_num",None)
        up_url1 = request.POST.get("up_url",None)
        print rev_num1,up_url1
        res = [rev_num1,up_url1]
        reu=all(res)
        print reu
        if reu:
            return HttpResponse('正在组合成脚本') 
        else:
            return HttpResponse('你有其中一个的参数是错误的')
    else:
        return render_to_response('./app04/upload.html')