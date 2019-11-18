from django.conf.urls import url, include
from . import views

# URLpatterns for the home app.
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^about/$', views.about, name="about"),
]