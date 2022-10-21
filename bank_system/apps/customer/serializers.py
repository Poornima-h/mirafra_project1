from .models import User,Bank
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bank
        fields="__all__"