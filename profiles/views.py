from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required
from home.views import home
from .forms import userProfileForm

# User Profile Function
@login_required
def user_profile(request):
    
    '''
    This gets the profile page for the logged in User
    '''
    
    user = UserProfile.objects.get(pk=request.user.id)
    
    if request.method == 'GET':
        
        """The user's profile"""
        
        form = userProfileForm(instance=user)
        
    else:
        # Requests the form and files data.
        form = userProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            # Sets the unique user profile instance up. 
            up = user
            
            try:
                up.full_name = form.cleaned_data['full_name']
                up.phone_number = form.cleaned_data['phone_number']
                up.town_city = form.cleaned_data['town_city']
                up.street_address1 = form.cleaned_data['street_address1']
                up.street_address2 = form.cleaned_data['street_address2']
                up.postcode = form.cleaned_data['postcode']
                up.country = form.cleaned_data['country']
                image = form.cleaned_data['image']
                
                # This checks if any data was collected during validation.
                if image:
                    up.image = image
                else:
                    # If no data was collected it sets the image before form was submitted.
                    form.image = user.image
                    
                up.save()
                messages.success(request, "Updated successfully!")
                return render(request, 'home.html')
                
            except Exception as e:
                # If an error occurs it throws up a message and asks to retry.
                print("Error: " + str(e))
                messages.error(request, "Failed to update, try again.")
                return render(request, 'profile.html', {'form' : form, 'profile' : user})
                
    return render(request, 'profile.html', {'form' : form, 'profile' : user})