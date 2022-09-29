from .models import Doctors
from rest_framework import serializers

class DoctorsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Doctors
        fields="__all__"