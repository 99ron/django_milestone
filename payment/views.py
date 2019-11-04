from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from payment.forms import orderForm, makePaymentForm
from django.conf import settings
from django.utils import timezone
import stripe



# Payment View below.


stripe_api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
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
    
    
    else:
        payment_form = makePaymentForm()
        order_form = orderForm()

    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_SECRET_KEY, })