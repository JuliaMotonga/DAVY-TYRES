"""davytyres URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from bookings import views as booking_views
from davyhome import views as basic_views
from django.conf.urls import url


from davyhome import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^sometest/', views.test_view, name='sometest'),
    url(r'^catalogue/', views.catalogue),
    url(r'^activate/(?P<activation>\w+)/(?P<email>\w+)/$', views.activate),
    url(r'unimplemented/', views.unimplemented)
]

authentication = [
    url(r'^logindenied/$', views.logindenied),
    url(r'^authview/$', views.auth_view),
    url(r'^loggedin/$', views.loggedin),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^register/$', basic_views.register),
    url(r'^register/(?P<redirect>\w+)?/?$', basic_views.register),
]

services = [
    url(r'^services/$', booking_views.services),
    url(r'^services/detail/$', booking_views.service_detail),
    url(r'^services/bookings/$', booking_views.show_active_bookings),
    url(r'^services/bookings/(?P<cancel>\w+)?/?$', booking_views.show_active_bookings),
]

urlpatterns += authentication + services