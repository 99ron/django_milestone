import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from orders.models import OrderList
from orders.views import view_order
from profiles.models import UserProfile
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
            
            if wcGet == None:
                wcGet = 1
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
            carmoGet = request.POST.get('car_model')
            
            # Checks to see if model has been chosen.
            if carmoGet is None:
                carmoGet = "Unknown"
                
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
                        ol.username = str(user)
                        ol.save()
    
                    except Exception as e:
                        messages.error(request, "Couldn't save your order: " + str(e))
                        return redirect(get_quote)
                else:
                    messages.error(request, "Couldn't match the user to the invoice, please try again.")
                    return redirect(get_quote)
            
            except Exception as e:
                # If it fails on one of the options above it'll ask the user to try again.
                messages.error(request, "Something went wrong: " + str(e) + " , please try again.")
                return redirect(get_quote)
            
            # All being well it ends here!
            messages.success(request, "Success! Your order has been sent for review.")
            return redirect(view_order)
            
        else: 
            # If form isn't valid!
            messages.error(request, "Form didn't validate: " + str(form.errors))
            return redirect(get_quote)


@login_required
def edit_quote(request, order_id):
    
    current_user = request.user.username
    orderList = OrderList.objects.get(pk=order_id)
    user = UserProfile.objects.get(user=request.user) 
    
    # This checks to confirm that the order was created by the user trying to edit it or an employee of the company
    if current_user == orderList.username or user.employee == True:
        
        try:
            # This retrieves the options selected from the original order created.
            origOrder = orderList.service_id
            service = Services.objects.get(invoice_no=origOrder)
            car_info = quotesForm(instance=service)
            
            # This retrieves all options from the models, these are dynamic in respect that the employer can add more as they need to.
            serviceType = TypeOfService.objects.all()
            optionalService = OptionalService.objects.all()
            wrapColour = WrapColour.objects.all()
            damage = Damage.objects.all() 
            
            # This sets the multi choice options as a flat list. Reason for this is when the options from that model
            # are rendered it will compare it to this list and if the option exists it'll add a checked option to it.
            origOSlist = origOrder.optional_service.all().values_list('id', flat=True)
            origDamageList = origOrder.damage.all().values_list('name', flat=True)
        
            context = { 'form' : car_info, 'serviceType' : serviceType, 'optionalService' : optionalService, 'damage' : damage, 'wrapColour' : wrapColour,
                        'origOrder' : origOrder, 'origOSlist' : origOSlist, 'origDamageList' : origDamageList}
                        
            return render(request, 'edit.html', context)
       
        except Exception as e:
            messages.error(request, "Sorry, something went wrong while trying to get your order. " + str(e))
            
    else:
        messages.error(request, "You are not an employee or the creator for this order.")
        return render(request, 'orders.html')





@login_required
def update_quote(request, order_id):
    """ This will collect the new (if updated) data from the quotes page """

    current_user = request.user.username
    user = UserProfile.objects.get(user=request.user) 
    
    # Gets the Current Service by matching the invoice numbers.
    cs = Services.objects.get(invoice_no=order_id)
    form = quotesForm(request.POST)
    
    # This confirms the user trying to update the order is the owner or an employee.
    if current_user == cs.user or user.employee == True:
    
        # Taken from the get_quote function.
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

            
            # This checks to see if an input has been chosen and if not gets the original colour choice from the database.
            if wcGet == None:
                wcRetreive = cs.wrap_colour.id
                wcModel = WrapColour.objects.get(id=wcRetreive)
            else:
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
            carmoGet = request.POST.get('car_model')
            
            # This checks if an input was selected, if not then gets the previous selection from the database.
            if carmoGet == None:
                carmoGet = cs.car_model
            
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

        
            # Once the data has been collected above, it then attempts to add it to the neccessary fields in the 
            # matched Services table.
            try:

                cs.save()
                cs.type_of_service = tosModel
                cs.optional_service.set(osList)
                cs.wrap_colour = wcModel
                cs.car_make = carmaGet
                cs.car_model = carmoGet
                cs.damage.set(vdList)
                cs.damage_details = damageDetailsGet
                cs.total_price = tpGet
                cs.user = str(user)
                cs.save()
                
                messages.success(request, "This order was updated successfully!")
                return redirect(view_order)
                
            except Exception as e:
                messages.error(request, "Error occured updating this order: " + str(e))
                return redirect(view_order)
        
        else:
            messages.error(request, "Sorry, there was an error with the form, please try again.")
            return redirect(view_order)
    else:
        messages.error(request, "You don't have permission to update this quote!")
        return redirect(view_order)