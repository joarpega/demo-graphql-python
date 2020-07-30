from djongo import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
