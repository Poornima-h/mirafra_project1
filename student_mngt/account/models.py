from django.db import models

# Create your models here.
class Student(models.Model):
      first_name=models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      email=models.EmailField(unique=True)
      password=models.CharField(max_length=100)
      department=models.CharField(max_length=50)

      class Meta:
            db_table = "Student"

class Marks(models.Model):
      student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
      maths=models.IntegerField(default=0)
      cse=models.IntegerField(default=0)
      DBMS=models.IntegerField(default=0)
      Web = models.IntegerField(default=0)
      class Meta:
            db_table="marks"



