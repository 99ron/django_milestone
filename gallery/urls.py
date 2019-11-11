from django.conf.urls import url, include
from gallery.views import view_gallery

urlpatterns = [
    url(r'^view$', view_gallery, name='gallery'),
    ]