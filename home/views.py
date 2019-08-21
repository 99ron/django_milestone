from django.shortcuts import render

# Create your views here.
def home(request):
    """A view that displays an index page"""
    return render(request, "home/home.html")