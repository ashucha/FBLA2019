from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Checkout

admin.site.site_header = 'BookTrack'
admin.site.site_title = admin.site.site_header
admin.site.register(Checkout)
