from django.shortcuts import render
from .blackJackGame import Tools

def index(request):

    return render(request,"index.html")
