from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import OrderList
from products.models import Services
from profiles.models import UserProfile

# Create your views here.
@login_required
def view_order(request):
    """ A view that renders the orders contents """
    ol = OrderList.objects.all()
    os = ol.filter(service_id__optional_service__isnull=False)
    olf = ol.filter(username=request.user)
    user = UserProfile.objects.get(user=request.user)
    page = request.GET.get('page', 1)
    
    
    # Checks to see if the logged in user is an employee or not.
    if user.employee == True:
        employee = True
        paginator = Paginator(ol, 5)
        #print("null = False: " + str(test))
        try:
            olpage = paginator.page(page)
        except PageNotAnInteger:
            olpage = paginator.page(1)
        except EmptyPage:
            olpage = paginator.page(paginator.num_pages)
            
        return render(request, "orders.html", {'orders' : olpage, 'employee' : employee})
    else:
        paginator = Paginator(olf, 5)
        try:
            olpage = paginator.page(page)
        except PageNotAnInteger:
            olpage = paginator.page(1)
        except EmptyPage:
            olpage = paginator.page(paginator.num_pages)
        
        employee = False
        return render(request, "orders.html", {'orders' : olf, 'employee' : employee})


