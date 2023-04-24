from django.db import models

# Create your models here.

class Student(models.Model):
    Sid=models.IntegerField(primary_key=True)
    Sname=models.CharField(max_length=100)
    Sage=models.IntegerField()
    Semail=models.EmailField()
    Sadd=models.CharField(max_length=100)
