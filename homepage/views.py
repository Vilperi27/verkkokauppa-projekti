from django.shortcuts import render, HttpResponse
from homepage.models import Tuote



def home(request):
    
    if request.method == "POST":
        term = request.POST.get('search')
        tuotteet = Tuote.objects.filter(product_name__contains=term) | Tuote.objects.filter(id__contains=term)
        return render(request, 'home.html', {'product':tuotteet})

    tuotteet = Tuote.objects.all()
    return render(request, 'home.html', {'product':tuotteet})

def sort_products(request, term):

    if(term == "ID"):
        tuotteet = Tuote.objects.all().order_by('id')
        if request.method == "POST":
            term = request.POST.get('search')
            tuotteet = Tuote.objects.filter(product_name__contains=term) | Tuote.objects.filter(id__contains=term)
            tuotteet = tuotteet.order_by('id')
            return render(request, 'home.html', {'product':tuotteet})

    elif(term == "name"):
        tuotteet = Tuote.objects.all().order_by('product_name')
        if request.method == "POST":
            term = request.POST.get('search')
            tuotteet = Tuote.objects.filter(product_name__contains=term) | Tuote.objects.filter(id__contains=term)
            tuotteet = tuotteet.order_by('product_name')
            return render(request, 'home.html', {'product':tuotteet})

    elif(term == "price"):
        tuotteet = Tuote.objects.all().order_by('product_price')
        if request.method == "POST":
            term = request.POST.get('search')
            tuotteet = Tuote.objects.filter(product_name__contains=term) | Tuote.objects.filter(id__contains=term)
            tuotteet = tuotteet.order_by('product_price')
            return render(request, 'home.html', {'product':tuotteet})


    return render(request, 'home.html', {'product':tuotteet})
