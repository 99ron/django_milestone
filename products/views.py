from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from products.forms import quotesForm
from products.models import TypeOfService, OptionalService, Damage, Services


# Create your views here.
def get_quote(request):
    
    car_info = quotesForm()
    serviceType = TypeOfService.objects.all()
    optionalService = OptionalService.objects.all()
    damage = Damage.objects.all()    

    if request.method == 'GET':
        
        "Show the quotes page"

        return render(request, 'quotes.html', { 'form' : car_info, 'serviceType' : serviceType,
        'optionalService' : optionalService, 'damage' : damage })
        
    else: 
        
        "Collects the data on the page to take over to the second page"
        
        sv = Services()
        
        form = quotesForm(request.POST)
        
        if form.is_valid():
            
            print("Try to get tos options")
            sv.type_of_service = request.POST.getlist('tos-option')
            
            print("Try to get OS options")
            sv.optional_service = request.POST.getlist('OS')
            
            print("Try to get car make")
            sv.car_make = form.cleaned_data['car_make']
            
            print("Try to get car model")
            sv.car_model = form.cleaned_data['car_model']
            
            print("Try to get TD options")
            sv.damage = request.POST.getlist('TD')
            
            print("Try to get TP options")
            sv.total_price = request.POST.get('total-price')
            
            print("Try to get tos options")
            sv.user = request.user.id
        
            print(sv)
            #sv.save()
            
            messages.success(request, "Test Succesful!")
            return render(request, 'quotes.html', { 'form' : car_info, 'serviceType' : serviceType,
            'optionalService' : optionalService, 'damage' : damage })
            
           