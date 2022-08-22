from django.shortcuts import render,redirect
from .models import Employee,otp_handler
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
import random
from django.conf import settings


def register(req):
    name=req.POST.get('name')
    dob=req.POST.get('dob')
    email=req.POST.get('email')
    pno=req.POST.get('pno')
    pin=req.POST.get('pin')
    pwd=req.POST.get('pwd')
    street,city,state,country=req.POST.get('location').split('-')
    employee=Employee.objects.filter(Email=email)
    userr=User.objects.filter(username=email)
    if employee.exists() and userr.exists():

        messages.success(req,'USER ALREADY EXIST')
    else:
        newEmp = Employee.objects.create(EmployeeName=name, Email=email, DOB=dob, Phone=pno, Street=street, City=city,
                                         State=state, Country=country, PINCODE=pin)
        newUser = User.objects.create_user(username=email, email=email, password=pwd)
        newEmp.save()
        newUser.save()
        messages.success(req, "USER CREATED")
    redirect('/')

def login(req):
    if req.method == 'POST':
        action = req.POST.get('action')
        if action == 'register':
            register(req)
    return render(req, 'login.html')

def validate(req):
    user=None
    if req.method=='POST':
        email = req.POST.get('email')
        pwd = req.POST.get('pwd')
        work = req.POST.get('action')
        if work == 'log_in':
            user = auth.authenticate(username=email, password=pwd)
    elif req.method=='GET':
        user=1
    return user

def home(req):
    user=validate(req)
    if user is not None and user!=1:
        auth.login(req, user)

        d={
            'name':Employee.objects.filter(Email=user).get().EmployeeName
        }
        return render(req, 'home.html', d)
    elif user is None:
        messages.success(req, 'Invalid Credintials')
    return redirect('/')
def forgot(req):

    return render(req,'forgot.html')

def email_send(email):
    subject = 'Your account verification email'
    one_time_p = random.randint(100000, 999999)
    user=otp_handler.objects.filter(email=email)
    if user.exists():
        user.update(last_otp=one_time_p)
    else:
        otp_handler.objects.create(email=email,last_otp=one_time_p).save()
    message = f'Hello User !!!!!\n Your one time password is {one_time_p}'
    email_from=settings.EMAIL_HOST
    send_mail(subject, message, email_from,[email])
def otp(req):
    email=req.POST.get('email')
    user=User.objects.filter(username=email)
    if user.exists():
        email_send(email)
        return render(req,'otp.html',{'email':email})
    else:
        messages.success(req,'EMAIL Does Not Exist')
        return redirect('/')

def change(req,email):
    otp_local=req.POST.get('otp')
    pwd=req.POST.get('pwd')
    user=otp_handler.objects.filter(email=email)
    if str(user[0].last_otp)==otp_local:
        u = User.objects.get(username=email)
        u.set_password(pwd)
        u.save()
        messages.success(req,'Password Changed')
    else:
        messages.success(req,'Invalid Otp')
    return redirect('/')

def logout(req):
    # req.session.flush()
    # auth.logout(req)
    return redirect('/')
