from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect 
from .forms import contactForm

# Create your views here.

def emailView(request):
    if request.method == 'GET':
        form = contactForm()
    else:
        form = contactForm(request.POST)
        
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            from_name = form.cleaned_data['from_name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            try:
                send_mail = EmailMessage(subject, message, from_email, from_name, ['test@gmail.com'], reply_to=[from_email],)
                send_mail.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('./successView/')
        else:
            form = contactForm()
            return render(request, 'home/contact.html', {'form' : form})
        
def successView(request):
    messages.success(request, "Your email has been sent, thank you.")
    return render(request, 'home/home.html')
        