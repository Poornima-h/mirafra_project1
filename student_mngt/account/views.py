from django.shortcuts import render
from rest_framework.response import Response
from .models import Student,Marks
from .serializers import StudentSerializer,MarksSerializer
from rest_framework import status,viewsets
from core.response_messages import CREATED
from django.shortcuts import get_object_or_404


class SignupAPI(viewsets.ViewSet):
      no_student=0
      def create(self,request):
          serializer=StudentSerializer(data=request.data)
          if serializer.is_valid(raise_exception=True):
             SignupAPI.no_student +=1
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)

      def login(self, request):
          data=request.data
          user = get_object_or_404(Student, email=data['email'], password=data['password'])
          if user:
              return Response(user.first_name, status=status.HTTP_200_OK)

class ResultAPI(viewsets.ViewSet):
      def add_marks(self,request):
          print(request.data)
          serializer = MarksSerializer(data=request.data,many=True)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









