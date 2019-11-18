from django.conf.urls import url, include
from gallery.views import view_gallery, add_review, review_more

# URLpatterns for the gallery app.
urlpatterns = [
    url(r'^view$', view_gallery, name='gallery'),
    url(r'^review_more/(?P<review_id>\d+)$', review_more, name="review_more"),
    url(r'^add_review/(?P<order_id>\d+)$', add_review, name="add_review"),
    ]