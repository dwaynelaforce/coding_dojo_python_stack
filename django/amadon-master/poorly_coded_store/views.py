from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if 'total_products_ordered' not in request.session:
        request.session['total_products_ordered'] = 0
    if 'total_spent' not in request.session:
        request.session['total_spent'] = 0
    
    prod_id = request.POST['id']
    my_prod = Product.objects.get(id=prod_id)

    quantity_from_form = int(request.POST["quantity"])
    request.session['total_products_ordered'] += quantity_from_form
    
    price_from_form = float(my_prod.price)
    total_charge = quantity_from_form * price_from_form
    request.session['total_spent'] += total_charge
    print("Charging credit card...")
    Order.objects.create(
        quantity_ordered=quantity_from_form,
        total_price=total_charge
    )
    return redirect('/receipt')

def receipt(request):
    context = {
        'order': Order.objects.last()
    }
    return render(request, 'store/checkout.html', context)
