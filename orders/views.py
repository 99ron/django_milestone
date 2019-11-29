from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import OrderList
from products.models import Services
from profiles.models import UserProfile
from gallery.models import Reviews

# Orders page views.

@login_required
def view_order(request):
    """ A view that renders the orders contents """
    
    # This collects all the objects in the Reviews table by order number and puts into a flat list.
    review_true = Reviews.objects.all().values_list('order_number', flat=True)
    
    # This then collects the objects from the OrderList table and excludes any results from the Reviews table.
    ol = OrderList.objects.exclude(pk__in=review_true)
    
    # This is used for a user who isn't an employee so they can only see their own orders, expanding on the above exclude filter.
    olf = ol.filter(username=request.user)
    
    # Gets the current logged in user.
    user = UserProfile.objects.get(user=request.user)
    page = request.GET.get('page', 1)

    # Checks to see if the logged in user is an employee.
    if user.employee == True:
        
        paginator = Paginator(ol, 10)
        employee = True
        try:
            olpage = paginator.page(page)
        except PageNotAnInteger:
            olpage = paginator.page(1)
        except EmptyPage:
            olpage = paginator.page(paginator.num_pages)
        
        return render(request, "orders.html", {'orders' : olpage, 'employee' : employee})
    
    # If they aren't then they're only allowed to see their own orders.
    else:
        paginator = Paginator(olf, 5)
        employee = False
        try:
            olpage = paginator.page(page)
        except PageNotAnInteger:
            olpage = paginator.page(1)
        except EmptyPage:
            olpage = paginator.page(paginator.num_pages)
        
        return render(request, "orders.html", {'orders' : olf, 'employee' : employee})



@login_required
def delete_order(request, order, user_id):
    """ Deletes a selected order """
    current_user = request.user.username
    user = UserProfile.objects.get(user=request.user)
    order = OrderList.objects.filter(pk=order)
    
    # This checks if the logged in user is the owner of the order trying to be deleted
    # or if the user is an employee who then has the right to remove the order.
    
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
            
    # If they're not the owner then it returns to the orders page with a message redirecting 
    # them back to the orders page. 
    else:
        messages.error(request, "Couldn't delete the order, you aren't the owner.")
        return redirect(view_order)
        
