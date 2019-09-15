from django.conf.urls import url, include
from profiles.views import user_profile

urlpatterns = [
    url(r'^profile/$', user_profile, name="profile"),
]
