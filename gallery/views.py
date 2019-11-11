from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Views for the Gallery app.

def view_gallery(request):
    """ This gets the gallery page to display """
    return render(request, "gallery.html")
        
