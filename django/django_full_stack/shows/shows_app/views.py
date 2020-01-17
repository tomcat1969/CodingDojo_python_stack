from django.shortcuts import render,redirect
from .models import Show
def AllShows(request):
    context={
        "all_the_shows":Show.objects.all()
    }
    return render(request, "AllShows.html",context)
def AddShow(request):
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
        "myShow":myShow
    }
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