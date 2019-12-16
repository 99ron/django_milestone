from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from orders.models import OrderList
from orders.views import view_order
from payment.forms import orderForm, makePaymentForm
from profiles.models import UserProfile
from django.conf import settings
from django.utils import timezone
import stripe

# Payment View below.

# Sets the stripe api key which is set in the environment file. 
stripe.api_key = settings.STRIPE_SECRET_KEY

# Confirms user is logged in.
@login_required
def checkout(request, order_id):
    if request.method == "GET":
        
        # Fetches user profile details by currently logged in user.
        current_user = request.user.username
        user = UserProfile.objects.get(pk=request.user.id)
        # Collects the correct order from the imported order_id.
        serviceOrder = OrderList.objects.get(pk=order_id)
        
        if serviceOrder.paid == False and current_user == serviceOrder.username:
        
            # Sets the payment form up as new and the order form with the user's data.
            payment_form = makePaymentForm()
            order_form = orderForm(instance=user)
            
            return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'order' : serviceOrder, 'publishable': settings.STRIPE_PUBLIC_KEY })
        
        else:
            # If user has already paid then takes them back to the orders page.
            messages.error(request, "You've already paid or didn't make the order.")
            return redirect(view_order)
 

@login_required
def payment(request, order_id):
    if request.method == "POST":
        
        # This sets up the required information needed to process who and what order.
        order = OrderList.objects.get(pk=order_id)
        user = UserProfile.objects.get(user=request.user)
        order_form = orderForm(request.POST)
        payment_form = makePaymentForm(request.POST)
        
        # Confirms form is valid and if so sets the data needed into the database.
        if order_form.is_valid() and payment_form.is_valid():
            orderF = order_form.save(commit=False)
            orderF.user = user
            orderF.order = order
            orderF.date = timezone.now()
            orderF.save()
            
            # Gets the price from the database via FK's.
            total = order.service_id.total_price
            
            # Now attempts to charge the card details that were supplied by the user.
            try:
                customer = stripe.Charge.create(
                    amount = int(total),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
                
                if customer.paid:
                # This sets the paid checkbox to true.
                    order.paid = True
                    order.save()
                    
                    messages.success(request, "You've paid Successfully")
                    return redirect(reverse('orders'))
            
                else:
                    messages.error(request, "Unable to take payment")
                
            # Any issues it prompts a message and a chance for the user to try again.
            except stripe.error.CardError:
                messages.error(request, "Your card was declined, please check your details below.")
            
            # Confirms once user has paid it will set a checkbox to true so it changes to 'leave review'
            # instead of 'pay' as it did previously on the orders page. 
            
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")

    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLIC_KEY, 'order' : order})

