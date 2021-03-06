"""autowrap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from home import urls as urls_home
from contactus import urls as urls_contactus
from profiles import urls as urls_profiles
from products import urls as urls_products
from orders import urls as urls_orders
from payment import urls as urls_payment
from gallery import urls as urls_gallery
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(urls_home)),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^contact/', include(urls_contactus)),
    url(r'^user/', include(urls_profiles)),
    url(r'^services/', include(urls_products)),
    url(r'^orders/', include(urls_orders)),
    url(r'^checkout/', include(urls_payment)),
    url(r'^gallery/', include(urls_gallery)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
