"""
Definition of urls for FBLA_Database.
"""

from django.conf.urls import include, url
from django.contrib import admin

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^admin/', admin.site.urls),
    url(r'^', include('app.urls')),
    url(r'^index/', include('app.urls')),
    url(r'^search/', include('app.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
