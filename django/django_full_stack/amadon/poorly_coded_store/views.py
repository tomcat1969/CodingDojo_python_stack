from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    id_from_form = int(request.POST["id"])
    total_charge = quantity_from_form * Product.objects.get(id=id_from_form).price
    print("Charging credit card...")
    myOrder = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    print('myorder id is ',myOrder.id)
    return redirect(f'/showResult/{myOrder.id}')

def showResult(request,myOrder_id):
    myOrder = Order.objects.get(id=myOrder_id)
    context={
        "the_order":myOrder
    }
    return render(request,"store/checkout.html",context)