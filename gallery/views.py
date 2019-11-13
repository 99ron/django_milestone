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
    rev = Reviews()
    att = Attachment()
    
    if request.method=="GET":
        
        form = reviewForm()
        return render(request, "add_review.html", {'form' : form, 'order': order})
    
    else:
        
        form = reviewForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            try:
                
                formForm = form.save(commit=False)
                formForm.save()
                
                # rev.username = request.user
                # rev.rating = form.cleaned_data['rating']
                # rev.title = form.cleaned_data['title']
                # rev.comment = form.cleaned_data['comment']
                # rev.save()
                
                
                
                return redirect(view_gallery)
                
            except Exception as e:
                messages.error(request, "Error occured: " + str(e))
                print("Error occured: " + str(e))
                return render(request, "add_review.html", {'form' : form, 'order': order})
                

        else:
            print(form.errors)
            return render(request, "add_review.html", {'form' : form, 'order': order})
            
            
            