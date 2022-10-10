from django.db import models

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    likes=models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "products"

class User(models.Model):
      pass
