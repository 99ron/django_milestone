from django.conf.urls import url, include
from .views import view_order, delete_order

urlpatterns = [
    url(r'^view/$', view_order, name='orders'),
    url(r'^delete/(?P<order_id>\d+)/$', delete_order, name='delete'),
    ]
