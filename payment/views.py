from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from orders.models import OrderList
from payment.forms import orderForm, makePaymentForm
from profiles.models import UserProfile
from django.conf import settings
from django.utils import timezone
import stripe




# Payment View below.


stripe_api_key = settings.STRIPE_SECRET_KEY

@login_required
def payment(request, order_id):
    if request.method == "POST":
        order_form = orderForm(request.POST)
        payment_form = makePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            try:
                customer = stripe.Charge.create(
                    amount = int('total' * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            
            if customer.paid:
                messages.success(request, "You've paid successfully")
                return redirect(reverse('orders'))
       
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")

    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_SECRET_KEY, })


@login_required
def checkout(request, order_id):
    if request.method == "GET":
        user = UserProfile.objects.get(pk=request.user.id)
        
        print(str(order_id))
        serviceOrder = OrderList.objects.get(pk=order_id)
        print(str(serviceOrder))
        
        payment_form = makePaymentForm()
        order_form = orderForm(instance=user)
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'order' : serviceOrder })
        
 