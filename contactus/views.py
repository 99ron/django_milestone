from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from django.http import HttpResponse, HttpResponseRedirect 
from django.conf import settings
from .forms import contactForm

# Create your views here.

def contact(request):
    if request.method == 'GET':
        form = contactForm()
    else:
        form = contactForm(request.POST)
        
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            from_name = form.cleaned_data['from_name']
            subject = form.cleaned_data['subject']
            
            try:
                send_to = settings.DEFAULT_FROM_EMAIL
                message = "{0} has sent a query: \n\n{1}".format(from_name, form.cleaned_data['message'])
                send_mail(subject, message, from_email, send_to, from_name)
                return redirect (successView)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect (successView)
        else:
            form = contactForm()
            return render(request, 'contact.html', {'form' : form})
    return render(request, "contact.html", {'form' : form})

def successView(request):
    form = contactForm()
    messages.success(request, "Your email has been sent, thank you.")
    return render(request, 'contact.html', {'form' : form})

