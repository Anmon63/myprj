from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest
from .models import *

def login(request):
    return render(request,'login.html')
def body(request):
    return render(request,'body.html')
def row(request):
    return render(request,'row.html')
def home(request):
    sdata=studadm.objects.all()
    context={'ses':request.session.get('fname_s'),
             'sdata':sdata}
    return render(request,'home.html',context)
def updadm(request):
    return render(request,'updadm.html')

def admdet(request):
    sdata=studadm.objects.all()
    return render(request,'admdet.html',{'sdata':sdata})

def addadm(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        standard=request.POST['standard']
        address=request.POST['address']
        phone=request.POST['phone']
        data=studadm(fname=fname,lname=lname,email=email,standard=standard,address=address,phone=phone)
        data.save()
        return redirect('admdet')
    return render(request,'home.html')

def updstu(request,id):
    stu=get_object_or_404(studadm,id=id)
    if request.method=='POST':
        stu.fname=request.POST.get('fname')
        stu.lname=request.POST.get('lname')
        stu.email=request.POST.get('email')
        stu.standard=request.POST.get('standard')
        stu.address=request.POST.get('address')
        stu.phone=request.POST.get('phone')
        stu.save()
        return redirect('admdet')
    return render(request,'updadm.html',{'stu':stu})

def delstu(request,id):
    ndata=studadm.objects.filter(id=id)
    ndata.delete()
    return redirect('admdet')

def studentsession(request):
    if request.method=='POST':
        fname=request.POST['fname']
        email=request.POST['email']
        if  studadm.objects.filter(fname=fname,email=email).exists():
            data=studadm.objects.filter(fname=fname,email=email).values('fname','email','id').first()
            request.session['fname_s']=data['fname']
            request.session['email_s']=data['email']
            request.session['s_id']=data['id']
            return redirect('home')
        else:
            return render(request,'home.html',{'msg':'Wrong Credentials or not verified'})
    else:
        return redirect('login')
    
def logout(request):
        request.session.flush()
        return redirect('login')

# Create your views here.
