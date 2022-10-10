from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import DoctorsSerializers

from .models import Doctors

class DoctorsAPI(ModelViewSet):
     """ doctors related api's"""
     def post(self,request):
         serializer=DoctorsSerializers(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data)

     def get(self,request):
         queryset=Doctors.objects.all()
         serializer=DoctorsSerializers(queryset)
         return Response(serializer.data)


     def update(self,request,id):
         queryset=get_object_or_404(id=id)
         serializer=DoctorsSerializers(data=queryset,partial=True)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data)


     def delete(self, request, id):
         try:
             data = request.data
             queryset = Doctors.objects.get(id=id)
             queryset.delete()
             return Response({"message": "data deleted"})
         except:
             return Response({"message": "error occurred try, again later"})
