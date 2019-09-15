from django.shortcuts import render
from django.contrib.auth.models import User
from profiles.models import UserProfile

# Create your views here.
def user_profile(request):
    """The user's profile"""
    user = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile' : user})