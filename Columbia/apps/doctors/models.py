from django.db import models

# Create your models here.
class Doctors(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    department=models.CharField(max_length=100)