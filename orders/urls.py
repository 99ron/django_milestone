from django.conf.urls import url, include
from .views import view_order

urlpatterns = [
    url(r'^view/$', view_order, name='view_order'),
    ]
