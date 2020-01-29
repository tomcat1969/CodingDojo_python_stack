from django.shortcuts import render,redirect
from .models import *

def index(request):
    context = {
        "all_the_messages": Messages.objects.all()
    }
    return render(request,"index.html",context)


def addPost(request):
    Messages.objects.create(message=request.POST['message'])
    print('add a message in date base')
    return redirect('/')