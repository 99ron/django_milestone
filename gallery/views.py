from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from gallery.models import Reviews, Attachment
from gallery.forms import reviewForm
from orders.models import OrderList


# Views for the Gallery app.

def view_gallery(request):
    """ This gets the gallery page to display """
    
    reviews_list = Reviews.objects.all()
    
    # This sets the pagination up for the reviews list.
    page = request.GET.get('page', 1)
    paginator = Paginator(reviews_list, 3)
    
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)
    

    return render(request, "gallery.html", {'reviews' : reviews})
        

@login_required
def add_review(request, order_id):
    """ This will either fetch the page for the review or post a review """
    
    order = OrderList.objects.get(pk=order_id)
    rev = Reviews()
    
    if request.method=="GET":
        
        form = reviewForm()
        return render(request, "add_review.html", {'form' : form, 'order': order})
    
    else:
        
        form = reviewForm(request.POST, request.FILES, instance=rev)
        
        if form.is_valid():
            
            try:
                rev.save()
                current_review = form.save(commit=False)
                current_review.username = request.user.username
                current_review.save()

                return redirect(view_gallery)
                
            except Exception as e:
                messages.error(request, "Error occured: " + str(e))
                print("Error occured: " + str(e))
                return render(request, "add_review.html", {'form' : form, 'order': order})
                
        else:
            print(form.errors)
            return render(request, "add_review.html", {'form' : form, 'order': order})
            
            
def review_more(request, review_id):
    """ This view is used for more info on the review """
    
    reviewID = Reviews.objects.get(pk=review_id)
    
    return render(request, "review_more.html", { 'review' : reviewID })