[![Build Status](https://travis-ci.org/99ron/django_milestone.svg?branch=master)](https://travis-ci.org/99ron/django_milestone)

# Django Milestone

This project is based on a car wrapping service. Being cars are a passion of mine, I wanted to implement this in my project and came up with the idea of a website that users can purchase a service and once completed have the option to leave a review with pictures. When looking at the list of reviews you can click on the 'more info' button to see the slideshow of images and a description of what was done plus a rating the user left the company. If you are the user that ordered a service you can edit or delete it from the database before paying so you can remove or amend the quote if you change your mind. Prices are updated on the go when an option is de/selected and users have a profile so people know who uploaded what review. 

# UX

My UX process was to analyze the customer’s requirements and try and think of different ways to implement this in an easy manner for the user. 

## The client’s requirements are:

    To be able to register and sign into an account
    To be able to create, edit, delete and view services on their account
    To be able to leave a review once they've purchased a service.
    To be able to contact the company for any queries via a contact form.
    To be able to sort through previous reviews to make judgement on work done

## User stories:

    As a user I want to be able to create an account
    As a user I want to be able to setup a personal profile.
    As a user I want to be able to create, edit and delete my own services/orders.
    As a user I want to be able to send the company an email with any queries I have.
    As a user I want to be able to sort through reviews by different criteria's
    As a user I want to view other user’s reviews.
    As a user I want be able to see a users review in detail. 
    As a user I want to be able to log out of my account

## Front End Design

Login/Register Pages - These pages use the same design. If the user has an issue with either login or registration then a information message should appear on the screen.

Reset Password Pages - These pages utilise the same background image and similar container structure so the user can easily navigate through and reset their password. One stage they will enter thier email address which will send an email with a link inside via a gmail account. 

Home Page - The home page appears to all users who have just visited the website. This page explains how the site works and has some infromation about the company.

About Page - This page has a little more personal information about the company and a link to the contact page at the bottom.

User Profile - This page is where a user who's just created an account is redirected to so they can upload a picture and add some personal information which will then be used in the payments app later on.

Contact Us - This is a page with a simple form used to send the company any query a user may have. It's setup using a free gmail account == vehicleautowraps@gmail.com.

Quotes Page - This is the page the user heads to get a quote for a service. There's multiple options to choose from and uses jQuery to hide or show certain containers as well as ajax using an api for the car models.

Edit Order Page - This page is used when the user wants to amend a service or remove an option that they've previously selected. This uses the same forms and models as the quotes page.

Orders Page - This shows the logged in user their orders, from here they can edit or delete the order if they're not happy with it. If they're wanting to proceed they can choose to pay. Once they've gone through the payment process they then have the option to leave a review. If the logged in user is an employee they will then see everyones orders and edit/delete as they need to.

Check Out Page - This shows a small container with some over order details and total cost, below this is two forms, one is the user details which is pulled from the User Profile model and the other is using stripe for payment method. 

Add Review - This page is simple in design which I wanted as it would seem more appealing for the user to fill out oppose to if there were tons of questions. It asks the user to rate the service out of five from a dropdown list, give the review a title and a description of the service and what they think. Finally leading to adding some images.

Review More - This page is got to by the user clicking the 'More Info' button on a review. Design of this page is simple as the top half of the container has who wrote the review, what they rated it, title and description and the bottom half has a courosel for the images they've uploaded. 

Gallery/Review Page - This page is where anyone can access to view the reviews left by users who've purchased a service from the company. These appear in small tidy panels with some basic overview of their experince. Takes one image (if more have been uploaded) and displays it to the left on a big screen or above on a smaller screen. Text for rating, title and description sit to the right on a big screen and below the image on a smaller screen.  

## Backend

My backend consists of a relatively simple MySQL database. For testing and Development I use the local AWS Cloud 9 Database and then for the live version I use the Postgres heroku add on.

My Database consists of many tables:

    User (django default auth model)
    Groups (didn't use but would on a larger project with many users)
    Reviews
        -Attachment (links to Reviews table)
    Order Lists
    Payment Details
    Services (Mostly made up of smaller models)
        -Damages
        -Optional Services
        -Type Of Services
        -Wrap Colour
    User Profile
    

The ER Diagram for my database:

.:: Attached as a pdf in repositry ::.

# Features

The features of this application are as follows:

    Ability to Register, Sign into and Logout of an Account
    Ability to Create, Edit and Delete Orders
    Ability to Add new Services, Optional Extras and Colours to the quotes 
    Ability to Create Reviews
    Ability to Create and Edit a personal User Profile
    Ability to Purchase a Service
    Ability to View other Reviews left by Users
    Ability to Upload images for my Profile and/or Reviews
    Ability to Contact the company for any queries
    Ability to Sort the Review results to what suits me


## Features Left to Implement

For the project I made the quote request fairly quick in regards that the user creates a quote and they can then pay and leave a review. Quick and easy. I'd like to change this so when they make a quote, they can't pay until an employee has checked it over and added any additional costs for damage as an example, then when they've checked it, would then let the user recheck the modified quote and proceed to pay.

Likewise I'd like to make the user hold off for leaving a review until the job is finishes. As it stands for the project everything can be done and tested quickly so I made it as soon as payment is succesfull it shows the button to leave a review.

I would like to add a way for users to communicate or comment on a review left by another user as I feel this would benefit the company if other users can answer any questions to someone who's had the work done previously.

Ability to be search would be a nice benefit feature on both Services and Profiles as I feel when the database grows it would be a useful feature to use.

Possibly change the layout for the wrap colour choice as it works well now, but I feel like when more colours of different textures appear in the database I would need to reorganise and also display a higher detailed image which can be expanded to give the user a better idea.

# Technologies Used

Python, Django, S3, AJAX, Pillow, Stripe, BlockUI

Django is the Python Framework I’m using for this application. 

Pillow - I've used this for securing image uploads to make sure no one uploads any old document and also to stop users intercepting it. 

AJAX - I've used this to update the car models on the quotes and edit quotes pages depending on what car make is chosen. 

Dj-Database-url - Used to connect to an external SQL database. 

Jinja2 - Used for rendering and adding logic to my templates.

Boto3 / S3 - Used for uploading images to my Bucket hosted on AWS. 

Stripe - This was used for making a purchase of a service, controls all the card details and transmits them securly. 

BlockUI - This is used for the message when the user presses a button. It times out after 2 seconds incase they press a submit button and the form doesn't validate.

## CSS

I'm using SCSS to build my css style sheet which has SASS doing the conversion for me.

Animated CSS by Daniel Eden. I love this package and use it with all my projects, if needed it can be amended with javascript to make it run a function when it's finished animating and much more (link below).

## jQuery

I've used jQuery to do a simple 'back to top' function but also for hiding/showing containers for the quotes page. Changing text for the show more buttons in the quotes page as well as the orders page. Confirm prompt box for when the user chooses to delete an order. At the last moment I've added the ability 

## Testing

For testing I have tried the following browsers; Firefox, Chrome, Edge and Internet Explorer.

I've used my PC at home which uses the screen size 2560 x 1080 and at work which is dual screen setup, used the built in "reponsive browser" feature mainly in firefox to test for different resolutions/devices.
As an addition I've used Django's built in TestCase to check urls, forms and some models, confirmed they pass but will need to be done on a local environment. To check your self type: python3 manage.py test

Check HTML and CSS code using W3C Markup, HTML had complaints regarding missing header tags as it can't read into the {% extend %} as well as any python logic it doesn't like.

## Testing Scenarios

    Try registering a user that already exists on the system
    Register a new user
    Login with incorrect details
    Login in with correct details
    Access user profile if they weren't created within the app, will fail
    Update user profile
    Create a new Order
    Edit a Order
    Delete a Order
    Edit a Order using the URL and vehicle id for a vehicle that has matching upload_by and current user
    Edit a Order using the URL and vehicle id for a vehicle that is another user’s upload
    Delete a Order using the URL and vehicle id for a vehicle that has the matching upload_by and current user
    Delete a Order using the URL and vehicle id for a vehicle that is another user’s order
    Sort the results on the Reviews/Gallery page
    Logout

## Bugs

I've installed django-cors-headers and set it up to whitelist the website needed to get car models, it still sometimes doesn't load the list due to
an error; "Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at
https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/?format=json. (Reason: CORS request did not succeed)."

Yet again, it does pull the list through most of the times so I'm not too sure on this, I've set up the package as the manual shows.

# Deployment

I've been using AWS Cloud 9 While developing this app. Throughout the development I used GitHub to keep track of changes.

The development version of my application is on GitHub and I push this code using git push origin master.

I've done all my testing on a local database which doesn't get uploaded to GitHub.

## Local Deployment

If you'd like to run this app locally you'll need to clone/pull from my git hub link: https://github.com/99ron/django_milestone.git

Once it's finished downloading, open a terminal and copy this command: pip3 install -r requirements.txt
this will install the required modules.

You want to open a console terminal and type: python3 manage.py makemigrations
Then: python3 manage.py migrate

This creates all the models and fk/relations between them.

Once this is succesfully done you'll want to create a 'superuser' which can be done with: python3 manage.py createsuperuser

To run the app you'll need to type into the console: python3 manage.py runserver $IP:$PORT'

From here you can create a new user and explore the site.

-- Admin Panel --

To add services and/or to test tables open the app so it's on the homepage and add /admin at the end of the url.
Must've created a superuser beforehand.

-- Quotes Services --

Only issue with creating a local database is the Services requires having the type of service, optional services and damages all added in manually via the django admin panel. Reason it's setup like this is so the employer can add additional services as they need to. I've preprogrammed in the quotes.js file that the first 4 options are set as Full Wrap, Mid Wrap, Small Wrap and Bonnet Wrap with the images set as an absolute path, change this as you need.  


## Heroku Deployment Steps

    Go to the Heroku Website and create new app
    Create requirements.txt and Procfile to tell heroku what is required to run the app
    Login into Heroku Account via command line and add the newly created app
    Go back to Heroku Website and in the settings tab click Reveal Config Vars and add IP and PORT vars from env.py file
    Install PostGres and run my models.py to create my database.
    Restart all dynos
    Last but not least, do an initial git commit and push to heroku
    
    **Since moving over to AWS Cloud9 my heroku commands don't want to work so I now deploy via the 
    option on heroku which if you have it linked to your GitHub, it'll download/clone the files across
    for you.

## Live Version of the App

https://autowraps-django-milestone.herokuapp.com/

# Acknowledgements

    Pencil - To draw my mock ups.
    Animated.css - https://daneden.github.io/animate.css/
    Postgres - Database hosted on Heroku
    SQL Schema - dbdiagram.io
    Django - Google/FullStack search results using snippets and amending for my purpose
    Images - Google Images, literally every image is found on here.
    CI Tutor - Helped with passing my travis with an issue no one could seem to figure until Micheal had a suggestion of rebuiling my table structure removing all the migrations filex except __init__ and then migrating. 
    Most of the time I ran through my ideas of what I wanted to achieve and found a solution after chatting "out loud" as it were.
