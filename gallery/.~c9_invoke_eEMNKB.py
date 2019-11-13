from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from gallery.models import Reviews, Attachment
from gallery.forms import reviewForm
from orders.models import OrderList


# Views for the Gallery app.

def view_gallery(request):
    """ This gets the gallery page to display """
    
    reviews = Attachment.objects.all()
    return render(request, "gallery.html", {'reviews' : reviews})
        

@login_required
def add_review(request, order_id):
    """ This will either fetch the page for the review or post a review """
    
    order = OrderList.objects.get(pk=order_id)
    reviews = Reviews.objects.all()
    rev = Attachment()
    
    if request.method=="GET":
        
        form = reviewForm(instance=order)
        return render(request, "add_review.html", {'form' : form, 'order': order})
    
    else:
        
        form = reviewForm(request.POST, request.FILES)
        
        
        if form.is_valid():

            try:
                
                rev.message.username = request.user
                rev.message.rating = form.cleaned_data['rating']
                rev.message.title = form.cleaned_data['title']
                rev.message.comment = form.cleaned_data['comment']
                rev.save()
                
                def form_valid(self, form):
                    for each in form.cleaned_data['attachments']:
                        Attachment.objects.create(file=each)
                    return super(UploadView, self).form_valid(form)

            except Exception as e:
                messages.error(request, "Error occured: " + str(e))
                return render(request, "add_review.html", {'form' : form, 'order': order})
                
            return redirect(view_gallery)
        
        else:
            print(form.errors)
            return render(request, "add_review.html", {'form' : form, 'order': order})
            
            
            