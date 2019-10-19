from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import OrderList
from products.models import Services
from profiles.models import UserProfile

ol = OrderList.objects.all()
#os = ol.filter(service_id__optional_service__isnull=False)

# Orders page views.

@login_required
def view_order(request):
    """ A view that renders the orders contents """
    olf = ol.filter(username=request.user)
    user = UserProfile.objects.get(user=request.user)
    page = request.GET.get('page', 1)
    
    
    # Checks to see if the logged in user is an employee or not.
    if user.employee == True:
        employee = True
        paginator = Paginator(ol, 5)

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



@login_required
def delete_order(request, order, user_id):
    """ Deletes a selected order """
    current_user = request.user.username
    user = UserProfile.objects.get(user=request.user)
    order = OrderList.objects.filter(pk=order)
    
    # This checks if the logged in user is the owner of the order trying to be deleted
    # or if the user is an employee who then has the write to remove the order.
    
    if user_id == current_user or user.employee == True:
        try:
            order = OrderList.objects.filter(pk=order)
            order.delete()
            messages.success(request, "Order has been removed.")
            return redirect(view_order) 
        except Exception as e:
            print(e)
            messages.error(request, "Couldn't delete object.")
            return redirect(view_order)
            
    # If they're not the owner then it returns to the orders page with a message. 
    else:
        messages.error(request, "Couldn't delete the order, you aren't the owner.")
        return redirect(view_order)