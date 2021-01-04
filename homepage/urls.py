from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, {}),
    path("id/", views.product_id),
    path("name/", views.product_name),
    path("price/", views.product_price),
]