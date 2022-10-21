from .views import SignupAPI,ResultAPI
from django.urls import path

urlpatterns= [
path('',SignupAPI.as_view({
        "post": "create",
        "get" :'login'
         })),

path('marks/',ResultAPI.as_view  ({
    "post": "add_marks"})),
]
