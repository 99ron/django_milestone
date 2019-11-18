from django.shortcuts import render

# Views for the home app.

def home(request):
    """A view that displays an index page"""
    return render(request, "home.html")
    
def about(request):
    """ A view to show the about us page"""
    return render(request, "about.html")
    
