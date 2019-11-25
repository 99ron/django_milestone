from django.conf.urls import url, include
from accounts.views import index, logout, login, registration
from accounts import url_reset

# URLpatterns for the accounts app.
urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="register"),
    url('^password-reset/', include(url_reset)),
]