from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
      class Meta:
            model=Student
            fields="__all__"


class MarksSerializer(serializers.ModelSerializer):
      class Meta:
            model=Student
            fields="__all__"