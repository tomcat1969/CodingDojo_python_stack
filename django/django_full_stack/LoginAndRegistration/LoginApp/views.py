from django.shortcuts import render,redirect
from .models import *
import bcrypt
from django.contrib import messages
from datetime import datetime

def LoginApp_index(request):


    if 'id' in request.session:
        print("session['id'] = ",request.session['id'])
    else:
        print("session id is not here")

    return render(request,"LoginApp_index.html")

def regist(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/register/")



    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    hashed_PW = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
    birthday_str = request.POST['birthday']
    birthday_obj = datetime.strptime(birthday_str,"%Y-%m-%d")     ##show how to use datetime
    print(birthday_obj.strftime("%d %B, %Y"))
    user =  Users.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = hashed_PW,
                birthday=birthday_obj
            )
    print("add a user in datebase")
    request.session['id'] = user.id
    print("session id = ",request.session['id'])
    return redirect('/register/success')

def success(request):
    if 'id' not in request.session:
        print("you have to login")
        return redirect('/register/')
    logged_user = Users.objects.get(id=request.session['id'])
    context={
        "logged_user":logged_user
    }
    return render(request,"success.html",context)

def logout(request):
    request.session.clear()
    return redirect('/register/')

def login(request):
    if 'id' not in request:
        request.session['id'] = None
    user = Users.objects.filter(email=request.POST['email'])

    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),logged_user.password.encode()):
            request.session['id'] = logged_user.id
            return redirect('/register/success')
    return redirect('register/')