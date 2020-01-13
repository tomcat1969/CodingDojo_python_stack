from django.shortcuts import render,redirect
import random
from time import strftime, gmtime
def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    if "logs" not in request.session:
        request.session['logs'] = []
    #request.session['gold'] += request.session['amount']
    context={
        "gold":request.session['gold'],
        "logs":request.session['logs']
    }

    return render(request,"index.html",context)
# def farm(request):
#     request.session['amount'] = random.randint(5, 10)
#     print("farm")
#     return redirect('/')
# def cave(request):
#     request.session['amount'] = 8
#     return redirect('/')
# def house(request):
#     request.session['amount'] = 10
#     return redirect('/')
# def casino(request):
#     request.session['amount'] = -5
#     return redirect('/')
def process_money(request):
    print(request.POST)
    locate = request.POST['location']
    print(locate)
    if locate == "farm":
        amount = random.randint(5,10)
    elif locate == "cave":
        amount = random.randint(5,10)
    elif locate == "house":
        amount = random.randint(5,10)
    else:
        amount = random.randint(-10,10)
    request.session['gold'] += amount
    time = strftime("%Y-%m-%d %H: %M %p", gmtime())
    request.session['logs'].append(f"earns {amount} from {locate} at {time}")

    return redirect("/")

