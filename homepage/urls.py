from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, {}),
    path("sort/<term>", views.sort_products),
]