from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from app.models import Checkout
from app.forms import SearchForm
from django.db.models import Q

class CheckoutListView(ListView):
    model = Checkout
    context_object_name = 'checkout_list'
    queryset = Checkout.objects.all().order_by('id')
    template_name = 'app/app.html'

    def get_queryset(self, **kwargs):
        context = super(CheckoutListView, self).get_queryset()
        return context

def index(request):
    return render(request, 'app/index.html')

def app(request):
    return render(request, 'app/app.html')

class