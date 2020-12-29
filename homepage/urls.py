from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, {}),
    path('search/<term>', views.get_products, name="search"),
]