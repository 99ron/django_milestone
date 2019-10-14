from django.conf.urls import url, include
from .views import view_order, add_to_order, adjust_order

urlpatterns = [
    url(r'^view/$', view_order, name='view_order'),
    url(r'^add/(?P<id>\d+)', add_to_order, name="add_to_order"),
    url(r'^adjust/(?P<id>\d+)', adjust_order, name="adjust_order"),
    ]
