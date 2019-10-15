from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import OrderList
from profiles.models import UserProfile

# Create your views here.
@login_required
def view_order(request):
    """ A view that renders the orders contents """
    ol = OrderList.objects.all()
    olf = ol.filter(username=request.user)
    user = UserProfile.objects.get(user=request.user)
    
    # Checks to see if the logged in user is an employee or not.
    if user.employee == True:
        employee = True
        return render(request, "orders.html", {'orders' : ol, 'employee' : employee})
    else:
        employee = False
        return render(request, "orders.html", {'orders' : olf, 'employee' : employee})


