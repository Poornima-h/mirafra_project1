from django.contrib import admin
from django.urls import path
from .views import ProductViewset

urlpatterns = [
    path('products',ProductViewset.as_view({
        "post": "create",
        "get" : "list",
         })),
    path('products/<str:pk>',ProductViewset.as_view({
        "put": "update",
        "get": "retrieve",
        "delete": "destroy"
    })),
]