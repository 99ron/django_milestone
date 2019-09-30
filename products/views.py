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
            
        car_info = quotesForm()

        return render(request, 'quotes.html', { 'form' : car_info, 'serviceType' : serviceType,
        'optionalService' : optionalService, 'damage' : damage })