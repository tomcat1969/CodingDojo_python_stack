from django.shortcuts import render,HttpResponse,redirect
def index(request):
    return HttpResponse("<h1>Placeholder to display a list of all blogs<h1>/")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def show(request,number):
    html = "Placeholder to display blog number:  {%s}" %number
    return HttpResponse(html)
def edit(request,number):
    return HttpResponse("placeholder to edit blog {%s}" %number)
def delete(request,number):
    return redirect("/")