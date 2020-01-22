from django.shortcuts import render,redirect
from .models import Show
from django.contrib import messages
def AllShows(request):
    print("code start here", "*" *40)
    # str = "hello"
    # str2 = "elloh"
    # if str == str2:
    #     print(True)
    # else:
    #     print(False)







    print("code end here", "*" *40)
    context={
        "all_the_shows":Show.objects.all()
    }
    return render(request, "AllShows.html",context)
def AddShow(request):
    print("AddShow is running",request.POST)
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)

        return redirect("/shows/new")

    ###


    title=request.POST['title']
    network=request.POST['network']
    release_date=request.POST['release_date']
    desc=request.POST['desc']
    Show.objects.create(title=title,network=network,release_date=release_date,desc=desc)
    return redirect('/')
def new(request):
    return render(request,"add.html")
def editShow(request,show_id):
    myShow = Show.objects.get(id=show_id)
    context={
        "myShow":myShow,
        "release_date":str(myShow.release_date)
    }
    print(myShow.release_date)
    return render(request,"edit.html",context)
def update(request):
    show_id=request.POST['show_id']
    myShow=Show.objects.get(id=show_id)
    myShow.title=request.POST['title']
    myShow.network=request.POST['network']
    myShow.release_date=request.POST['release_date']
    myShow.desc=request.POST['desc']
    myShow.save()
    return redirect('/')
def detail(request,show_id):
    myShow = Show.objects.get(id=show_id)
    context={
        "myShow":myShow
    }
    return render(request,"detail.html",context)
def delete(request,show_id):
    myShow = Show.objects.get(id=show_id)
    myShow.delete()
    return redirect('/')