from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer
from core.response_messages import DELETED,ERROR
from django.shortcuts import get_object_or_404


# Create your views here.
class ProductViewset(viewsets.ViewSet):
    def list(self,request):#/api/products/
        try:
            products=Products.objects.all()
            serializer=ProductSerializer(products,many=True)
            return Response(serializer.data)
        except:
            return Response(ERROR)

    def create(self,request,pk=None):#/api/products/
        try:
            serializer=ProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except:
            return Response(EXCEPTION)

    def retrieve(self,request,pk=None):#/api/products/<str:id>/
        product=get_object_or_404(Products,id=pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    def update(self,request,pk=None):#/api/products/<str:id>/
        try:
            product = get_object_or_404(Products,id=pk)
            serializer = ProductSerializer(product,data=request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except:
            return Response(EXCEPTION)

    def destroy(self,request,pk=None):#/api/products/<str:id>/
        try:
            product = get_object_or_404(Products,id=pk)
            product.delete()
            return Response(DELETED,status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(ERROR)




