from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from products.forms import quotesForm
from products.models import TypeOfService, OptionalService, Damage


# Create your views here.
def get_quote(request):

    if request.method == 'GET':
        
        "Show the quotes page"
        
        serviceType = TypeOfService.objects.all()
        optionalService = OptionalService.objects.all()
        damage = Damage.objects.all()
            
        quotes_form = quotesForm()

        return render(request, 'quotes.html', { 'form' : quotes_form, 'serviceType' : serviceType,
        'optionalService' : optionalService, 'damage' : damage })