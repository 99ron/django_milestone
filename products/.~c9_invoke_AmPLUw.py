from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
import requests, json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from orders.models import OrderList
from products.forms import quotesForm
from products.models import TypeOfService, OptionalService, Damage, Services, WrapColour


# This view deals with both POST and GET for the quotes page which then saves it into two tables, Services and Orders.
@login_required
def get_quote(request):

    # Gets required information from the required models/tables.
    car_info = quotesForm()
    serviceType = TypeOfService.objects.all()
    optionalService = OptionalService.objects.all()
    wrapColour = WrapColour.objects.all()
    user = User.objects.get(pk=request.user.id)
    damage = Damage.objects.all()    
    
    ''' This needs to be implemented, made in repl.it '''
    '''
    car_make = "toyota"

    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{0}?format=json'.format(car_make)
    
    #print(url)
    
    # Gets the modified string above to request data.
    response = requests.get(url)
    
    def jsonDump(response):
      json.dumps(response, sort_keys=True, indent=4)
      # text = json.dumps(response, sort_keys=True, indent=4)
      # print(text)
    
    # Filters by the Results key and then jsonDumps the results
    manuResults = response.json()['Results']
    jsonDump(manuResults)
    
    manuList = []
    
    for i in manuResults:
      # For each model in results append to list
      list = i["Model_Name"]
      manuList.append(list)
    
    # Print newly made list
    print(manuList)
    '''
    
    if request.method == 'GET':
        
        "Show the quotes page"
        
        return render(request, 'quotes.html', { 'form' : car_info, 'serviceType' : serviceType,
        'optionalService' : optionalService, 'damage' : damage, 'wrapColour' : wrapColour })
        
    else: 
        
        "Collects the data on the page to take over to the second page"
        
        sv = Services()
        ol = OrderList()
        
        form = quotesForm(request.POST)
        
        if form.is_valid():
            ''' If the form is valid it then collects the information on the form before saving it.'''
            
            # This gets the info from the 'type of service' select menu, converts it to an int 
            # and then compares it to the option in TypesOfService table.
            tosGet = request.POST.get('tos-option')
            ToSToInt = int(tosGet)
            tosModel = TypeOfService.objects.get(id=ToSToInt)
            
            # This gets the selected wrap colour which is a radio button, then compares it to 
            # the table to see what the match is.
            wcGet = request.POST.get('wc-option')
            wcModel = WrapColour.objects.get(id=wcGet)

            # This gets the option from the Optional Services list, compares the int to the 
            # OptionalServices table and then appends it to a list.
            osGet = request.POST.getlist('OS')
            
            osList = []
            
            for i in osGet:
                osModel = OptionalService.objects.get(id=i)
                osList.append(osModel)

               
            # This gathers the text inputted for the 'car make'.
            carmaGet = form.cleaned_data['car_make']
            
            # This gathers the text inputted for the 'car model'.            
            carmoGet = form.cleaned_data['car_model']

            # This gets the text from the 'Damage Details' text box.
            damageDetailsGet = request.POST.get('ddInput')
            
            # This gets the selected (if any) options to then compare to the Damage table
            # and then adds it to list.
            vdGet = request.POST.getlist('TD')
            
            vdList = []
            
            for i in vdGet:
                vdModel = Damage.objects.get(id=i)
                vdList.append(vdModel)
            
            # This gets the total price from the read-only text box which is updated by JS depending
            # on what options are selected by the user.
            tpGet = request.POST.get('tp-name')
            

            # Once the data has been collected above it then attempts to add it to the neccessary fields in the 
            # Services table.
            try:
                sv.save()
                sv.type_of_service = tosModel
                sv.optional_service.set(osList)
                sv.wrap_colour = wcModel
                sv.car_make = carmaGet
                sv.car_model = carmoGet
                sv.damage.set(vdList)
                sv.damage_details = damageDetailsGet
                sv.total_price = tpGet
                sv.user = str(user)
                sv.save()
                
                
                ''' Once the original form is submitted and has created an invoice number, this now gets the latest 
                    invoice number and compares the username to confirm it's the same and saves the invoice number
                    to the orders table with the time when this was added. 
                '''
                
                latestInvoice = Services.objects.latest('invoice_no')
                
                
                if latestInvoice.user == str(user):
                    try:
                        ol.service_id = latestInvoice
                        ol.order_date = datetime.now()
                        ol.order_status = "Waiting On Employee"
                        ol.username = str(user)
                        ol.save()

                    except Exception as e:
                        print(e)
                        messages.error(request, "Couldn't save your order, please try again shortly.")
                        return redirect(get_quote)
                else:
                    messages.error(request, "Couldn't match the user to the invoice, please try again.")
                    return redirect(get_quote)
            
            except Exception as e:
                # If it fails on one of the options above it'll ask the user to try again.
                print(e)
                messages.error(request, "Something went wrong: " + e + " , please try again.")
                return redirect(get_quote)
            
            # All being well it ends here!
            messages.success(request, "Success! Your order has been sent for review.")
            return redirect(get_quote)


@login_required
def edit_quote(request, order_id):

    orderList = OrderList.objects.get(pk=order_id)
    origOrder = orderList.service_id
    
    os = origOrder.optional_service.all()
    for i in os:
        print("origOrder: " + str(i))
        i.is_needed

    #print(origOrder.wrap_colour)
    
    car_info = quotesForm()
    serviceType = TypeOfService.objects.all()
    optionalService = OptionalService.objects.all()

    for i in origOrder.optional_service.all():
        print(i)
        print(i.is_needed)
        
        
    # USE DICTIONARY    
    # { : , : }
        
    wrapColour = WrapColour.objects.all()
    damage = Damage.objects.all() 
    return render(request, 'edit.html', { 'form' : car_info, 'serviceType' : serviceType,
    'optionalService' : optionalService, 'damage' : damage, 'wrapColour' : wrapColour, 'origOrder' : origOrder })
    