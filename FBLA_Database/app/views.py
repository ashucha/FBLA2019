from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from app.models import Checkout
# from app.forms import SearchForm
from django.db.models import Q
# from .filters import SearchForm
import operator
from functools import reduce

class CheckoutListView(ListView):
    model = Checkout
    context_object_name = 'checkout_list'
    queryset = Checkout.objects.all().order_by('id')
    template_name = 'app/app.html'

    def get_queryset(self, **kwargs):
        result = super(CheckoutListView, self).get_queryset()
        
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                                   reduce(operator.and_, (Q(code__icontains=q) for q in query_list)) | 
                                   reduce(operator.and_, (Q(first_name__icontains=q) for q in query_list)) |
                                   reduce(operator.and_, (Q(last_name__icontains=q) for q in query_list))
                                   )
        
        return result

def index(request):
    return render(request, 'app/index.html')

def app(request):
    return render(request, 'app/app.html')
