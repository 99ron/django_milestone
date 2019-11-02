from django.conf.urls import url, include
from orders.views import view_order, delete_order

urlpatterns = [
    url(r'^view/$', view_order, name='orders'),
    url(r'^delete/(?P<order>\d+)(?P<user_id>\w+)/$', delete_order, name='delete'),
    ]
