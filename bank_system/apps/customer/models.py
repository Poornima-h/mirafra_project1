from django.db import models

# Create your models here.

class User(models.Model):
     name=models.CharField(max_length=100)
     age=models.IntegerField()
     gender=models.CharField(max_length=10)

     class Meta:
         db_table='user'


class Bank(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    class Meta:
        db_table = 'bank'
