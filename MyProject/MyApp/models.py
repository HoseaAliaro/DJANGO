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
    

class Person(models.Model):
    name=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to='profile/',null=True,blank=True)
    cv=models.FileField(upload_to='document/',null=True,blank=True)