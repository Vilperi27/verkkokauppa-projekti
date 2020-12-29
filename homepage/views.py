from django.shortcuts import render, HttpResponse
from homepage.models import Tuote

# Create your views here.

def home(request):
    tuotteet = Tuote.objects.all()
    return render(request, 'home.html', {'product':tuotteet})

def get_products(request, term):
    tuotteet = Tuote.objects.filter(product_name__contains=term)
    return render(request, 'home.html', {'product':tuotteet})