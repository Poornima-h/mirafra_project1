from django.contrib import admin
from django.urls import path
from .views import DoctorsAPI

urlpatterns = [
    path('add-doctors/',DoctorsAPI.as_view({'post':'post'})),
    path('get-doctors/',DoctorsAPI.as_view({'get':'get'})),
    path('update-doctors/',DoctorsAPI.as_view({'update':'get'})),
    path('delete-doctors/',DoctorsAPI.as_view({'delete':'delete'}))
    ]