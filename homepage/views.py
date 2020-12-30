from django.shortcuts import render, HttpResponse
from homepage.models import Tuote

# Create your views here.

def home(request):

    if request.method == "POST":
        term = request.POST.get('search')
        tuotteet = Tuote.objects.filter(product_name__contains=term) | Tuote.objects.filter(product_id__contains=term)
        return render(request, 'home.html', {'product':tuotteet})

    tuotteet = Tuote.objects.all()
    return render(request, 'home.html', {'product':tuotteet})

def get_products(request, term):
    tuotteet = Tuote.objects.filter(product_name__contains=term)
    return render(request, 'home.html', {'product':tuotteet})