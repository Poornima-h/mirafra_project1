from django.contrib import admin
from django.urls import path
from .views import ProductViewset

urlpatterns = [
    path('products',ProductViewset.as_view({
        "post":"list",
        "get":"list"
         })),
]