from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def view_order(request):
    """ A view that renders the orders contents """
    return render(request, "orders.html")
    
def add_to_order(request, id):
    """ Add a quantity to a specified product to the cart """
    
    quantity = int(request.POST.get('quantity'))
    
    order = request.session.get('order', {})
    order[id] = order.get(id, quantity)
    
    request.session['order'] = order
    return redirect(reverse('index'))
    
def adjust_order(request, id):
    """ Adjust the quantity of the specified product. """
    
    quantity = int(request.POST.get('quantity'))
    order = request.session.get('order', {})
    
    if quantity > 0:
        order[id] = quantity
    else:
        order.pop(id)
    
    request.session['order'] = order
    return redirect(reverse('view_order'))