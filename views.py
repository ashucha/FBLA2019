from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from app.models import Checkout
from app.forms import SearchForm

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

def query(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/search/')
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})