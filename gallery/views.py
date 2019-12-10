from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from gallery.models import Reviews, Attachment
from gallery.forms import reviewForm
from orders.models import OrderList
from orders.views import view_order
from profiles.models import UserProfile


# Views for the Gallery app.

""" This gets the gallery page to display """
def view_gallery(request):
    
    # This checks if any filters have been applied
    if request.GET.get('orderSortBy'):
        sort_by = request.GET.get('orderSortBy')
        
        if sort_by == "HighRated":
            # If sort_by contains HighRated it'll display the results highest ratings first.
            reviews_list = Reviews.objects.all().order_by('-rating')
        
        elif sort_by == "Newest":
            # If sort_by contains Newest it'll display the results Newest first.
            reviews_list = Reviews.objects.all().order_by('-review_submitted')
        
        elif sort_by == "LowRated":
            # If sort_by contains LowRated it'll display the results lowest ratings first.
            reviews_list = Reviews.objects.all().order_by('rating')
            
        elif sort_by == "Oldest":
            # If sort_by contains Oldest it'll display the results oldest posts first.
            reviews_list = Reviews.objects.all().order_by('review_submitted')

    else:
        # This is the default when the page is loaded.
        reviews_list = Reviews.objects.all()
    
    """ This sets the pagination up for the reviews list with a maximum of 3 shown per page."""
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
    
    current_user = request.user.username
    order = OrderList.objects.get(pk=order_id)
    userID = UserProfile.objects.get(pk=request.user.id)
    rev = Reviews()
    
    if request.method=="GET":
        # This sets up the form ready for the user to enter information.
        # Checks that the user leaving the review is the one who created it.
        if order.username == current_user:
            form = reviewForm()
            return render(request, "add_review.html", {'form' : form, 'order': order})
        else:
            messages.error(request, "You didn't pay for the order, can't access this.")
            return redirect(view_order)
     
    
    else:
        
        # This checks if the logged in user is the owner of the order trying to be reviewed.
        if order.username == current_user:
            
            # This is processed when the user submits the form.
            form = reviewForm(request.POST, request.FILES, instance=rev)
            
            # Confirms the form is valid.
            if form.is_valid():
                
                # Attempts to save the form into the tables.
                try:
                    rev.order_number = order
                    rev.user_int = userID
                    rev.review_left = True
                    rev.save()
                    form.save()
    
                    return redirect(view_gallery)
                    
                except Exception as e:
                    messages.error(request, "Error occured: " + str(e))
                    return render(request, "add_review.html", {'form' : form, 'order': order})
                    
            else:
                messages.error(request, "Form wasn't valid, please check everthing is filled out.")
                return render(request, "add_review.html", {'form' : form, 'order': order})
        else:
            messages.error(request, "Sorry but you're not the owner of that listing.")
            return reverse(view_order)

            
def review_more(request, review_id):
    """ This view is used for more info on the review """
    
    reviewID = Reviews.objects.get(pk=review_id)
    uPro = UserProfile.objects.get(pk=reviewID.user_int)
    
    return render(request, "review_more.html", { 'review' : reviewID, 'profile' : uPro })