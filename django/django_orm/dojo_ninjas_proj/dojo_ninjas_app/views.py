from django.shortcuts import render,redirect
from .models import dojo,ninja

def index(request):
   context={
      "all_the_dojo":dojo.objects.all(),
      "all_the_ninja":ninja.objects.all()
   }

   return render(request,'index.html',context)

def addDojo(request):
   name = request.POST['name']
   city = request.POST['city']
   state = request.POST['state']
   dojo.objects.create(name=name,city=city,state=state)
   return redirect('/')

def addNinja(request):
   first_name=request.POST['first_name']
   last_name=request.POST['last_name']
   dojo_id = request.POST['dojo']
   print(first_name,last_name,dojo_id)
   ninja.objects.create(first_name=first_name,last_name=last_name,dojo_id=dojo.objects.get(name=dojo_id))
   return redirect('/')

def delNinja(request):
   ninja_id=request.POST['ninja_id']
   print(ninja_id)
   ninja.objects.get(id=ninja_id).delete()
   return  redirect('/')