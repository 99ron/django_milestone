from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from django.http import HttpResponse, HttpResponseRedirect 
from django.conf import settings
from contactus.forms import contactForm
from home.views import home

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

                send_to = settings.DEFAULT_SEND_TO
                message = "Name: {0} \nEmail: {1} \n\nMessage: {2}".format(from_name, from_email, form.cleaned_data['message'])
                send_mail(subject, message, from_email, [send_to], from_name)
                
                messages.success(request, "Your email has been sent, We'll get back to you soon as possible.")
                return redirect (home)
                
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect (successView)
        else:
            form = contactForm()
            return render(request, 'contact.html', {'form' : form})
    return render(request, "contact.html", {'form' : form})
