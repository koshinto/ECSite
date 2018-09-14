from django.shortcuts import render
from django.views.generic import ListView
from navigate.models import Item

def home(request):
    return render(request, 'home.html')

class ItemView(ListView):
    model = Item
    template_name = 'list.html'
    slug_url_kwarg = 'item_list'
