from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import DoctorsSerializers
from .models import Doctors

class DoctorsAPI(ModelViewSet):
     """ doctors related api's"""
     def post(self,request):
         try:
             data=request.data
             query=DoctorsSerializers(data=data,many=True)
             if query.is_valid():
                 query.save()
                 return Response({"message":"data created"})
             return Response({"message": "invalid data"})
         except:
             return Response({"message": "error occurred try, again later"})

     def get(self,request):
         try:
             queryset=Doctors.objects.all()
             query=DoctorsSerializers(data=queryset,many=True)
             if query.is_valid():
                return Response({"data":query.data})
             return Response({"data":query.data})
         except Exception as e:
             print(e)
             return Response({"message": "error occurred try, again later"})

     def update(self,request,id):
         try:
             data=request.data
             queryset=Doctors.objects.get(id=id)
             query=DoctorsSerializers(data=queryset,partial=True)
             if query.is_valid():
                 query.save()
                 return Response({"message":"data created"})
             return Response({"message":"data not found"})
         except:
             return Response({"message": "error occurred try, again later"})

     def delete(self, request, id):
         try:
             data = request.data
             queryset = Doctors.objects.get(id=id)
             queryset.delete()
             return Response({"message": "data deleted"})
         except:
             return Response({"message": "error occurred try, again later"})
