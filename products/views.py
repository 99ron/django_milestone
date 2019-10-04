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
            
            tosGet = request.POST.get('tos-option')
            ToSToInt = int(tosGet)
            tosModel = TypeOfService.objects.get(id=ToSToInt)
            
            print("Service Type: " + str(tosModel) )
            
            
            osGet = request.POST.getlist('OS')
            
            osList = []
            
            for i in osGet:
                osModel = OptionalService.objects.get(id=str(i))
                osList.append(osModel)
            print("Optional: " + str(osList))
            
            
            carmaGet = form.cleaned_data['car_make']
            print("Car Make: " + carmaGet)
            
            
            carmoGet = form.cleaned_data['car_model']
            print("Car Model: " + carmoGet) 
            
            
            vdGet = request.POST.getlist('TD')
            
            vdList = []
            
            for i in vdGet:
                vdModel = Damage.objects.get(id=str(i))
                vdList.append(vdModel)
            print("Vehicle Damage: " + str(vdList))
            
    
            tpGet = request.POST.get('tp-name')
            print("Total Price: " + str(tpGet))
            
            userGet = request.user.id
            print("Submitted User: " + str(userGet))

            
            
            messages.success(request, "Test Succesful!")
            return render(request, 'quotes.html', { 'form' : car_info, 'serviceType' : serviceType,
            'optionalService' : optionalService, 'damage' : damage })
            
           