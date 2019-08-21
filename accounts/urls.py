from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile
from accounts import url_reset
from home.views import home

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="register"),
    url(r'^profile/$', user_profile, name="profile"),
    url('^password-reset/', include(url_reset)),
]