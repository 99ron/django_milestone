from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from profiles.models import UserProfile
from .forms import userProfileForm

# User Profile Function

def user_profile(request):
    
    '''
    This gets the profile page for the logged in User
    '''
    user = UserProfile.objects.get(pk=request.user.id)
    
    if request.method == 'GET':
        
        """The user's profile"""
        
        form = userProfileForm(instance=user)
        
    else:
        
        form = userProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            up = user
            
            try:
                up.first_name = form.cleaned_data['first_name']
                up.last_name = form.cleaned_data['last_name']
                up.phone_number = form.cleaned_data['phone_number']
                up.address = form.cleaned_data['address']
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
                return render(request, 'profile.html', {'form' : form, 'profile' : user})
                
            except:
                # If an error occurs it throws up a message and asks to retry.
                messages.error(request, "Failed to update, try again.")
                return render(request, 'profile.html', {'form' : form, 'profile' : user})
                
    return render(request, 'profile.html', {'form' : form, 'profile' : user})