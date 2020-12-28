from django.shortcuts import render, HttpResponse
from homepage.models import Tuote

# Create your views here.

def home(request):
    tuotteet = Tuote.objects.all()
    return render(request, 'home.html', {'product':tuotteet})