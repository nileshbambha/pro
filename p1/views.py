from django.shortcuts import render,redirect
from .models import data
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    datas = data.objects.all()
    return render(request,'index.html',{'datas':datas})
def details(request,data_id):
    dataa = data.objects.get(pk=data_id)
    return render(request,'details.html',{'dataa':dataa})
def register(request):
    if request.method=="POST":
        name = request.POST['name']
        passwd = request.POST['password']
        user = User.objects.create_user(username=name,password=passwd)
        user.save()
        return redirect(index)
    else:
        return render(request,'register.html')
def login(request):
    if request.method =="POST":
        name = request.POST['username']
        passwd = request.POST['password']
        user = auth.authenticate(username=name,password=passwd)
        if user is not None:
            auth.login(request,user)
            return redirect(index)
    else :
        return render(request,'login.html')
def input(request):
    if request.method=="POST":
        name = request.POST['name']
        city = request.POST['city']
        inputs = data.objects.create(name=name,city=city)
        return redirect(index)
    else:
        return render(request,'input.html')
def deletes(request,datas_id):
    obj= data.objects.get(pk=datas_id)
    obj.delete()
    return redirect(index)
def logout(request):
    auth.logout(request)
    return redirect(index)