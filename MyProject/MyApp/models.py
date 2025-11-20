from django.db import models

# Create your models here.
class Student(models.Model):
    firstName=models.CharField(max_length=100)
    secondName=models.CharField(max_length=100)
    email=models.EmailField()
    regNo=models.CharField(max_length=100)
    age=models.IntegerField()



    def __str__(self):
        return self.firstName