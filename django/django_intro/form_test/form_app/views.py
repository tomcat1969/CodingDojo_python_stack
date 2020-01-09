from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html')
def create_user(request):
    print("Got Post Info....................")
    print(request.POST)
    # <QueryDict: {'csrfmiddlewaretoken': ['xc6TP798YapnHno47dj92v8qNH1A1eHvY6Q74erzDr7rO1ujDAOzZGwrHKvuSqX5'], 'name': ['tomcat'], 'email': ['tomcat1969@gmail.com']}>
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    print(name_from_form)
    print(email_from_form)
    #return render(request, "index.html")
    #return redirect("/success")
    email = request.POST['email']
    return redirect(f"/success/{email} ")
def success(request,email):
    # this is the success route
    context = {
        "email":email
    }
    return render(request,"success.html",context)