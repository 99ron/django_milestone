from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from products.forms import quotesForm
from products.models import Services

# Create your views here.
def get_quote(request):
    
    user = User.objects.get(pk=request.user.id)
    
    if request.method == 'GET':
        
        "Show the quotes page"
        
        quotes_form = quotesForm()
        
        context = { 'form' : quotes_form,
                    'user' : user }
        
        return render(request, 'quotes.html', context)