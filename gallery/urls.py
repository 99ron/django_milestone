from django.conf.urls import url, include
from gallery.views import view_gallery, add_review

urlpatterns = [
    url(r'^view$', view_gallery, name='gallery'),
    url(r'^add_review/(?P<order_id>\d+)$', add_review, name="add_review")
    ]