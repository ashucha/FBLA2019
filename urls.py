from django.conf.urls import url, include
from django.views.generic import ListView
from . import views
from app.models import Checkout
from app.views import CheckoutListView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^app/', views.CheckoutListView.as_view(), name='checkouts'),
    url(r'^search/', views.query, name='search'),
]