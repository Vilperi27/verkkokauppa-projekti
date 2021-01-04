from django.shortcuts import render, HttpResponse
from homepage.models import Tuote



def home(request):
    
    if request.method == "POST":
        term = request.POST.get('search')
        tuotteet = Tuote.objects.filter(product_name__contains=term) | Tuote.objects.filter(product_id__contains=term)
        return render(request, 'home.html', {'product':tuotteet})

    tuotteet = Tuote.objects.all()[:10]
    return render(request, 'home.html', {'product':tuotteet})

def product_id(request):
    
    tuotteet = Tuote.objects.all().order_by('product_id')[:10]

    return render(request, 'home.html', {'product':tuotteet})

def product_name(request):

    tuotteet = Tuote.objects.all().order_by('product_name')[:10]

    return render(request, 'home.html', {'product':tuotteet})

def product_price(request):

    tuotteet = Tuote.objects.all().order_by('product_price')[:10]

    return render(request, 'home.html', {'product':tuotteet})