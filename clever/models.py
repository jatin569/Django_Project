from django.db import models
class signup(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.CharField(max_length=40)
    Phone = models.CharField(max_length=40)
    Username = models.CharField(max_length=40)
    Password = models.CharField(max_length=40)
    DOB = models.CharField(max_length=40)
    City = models.CharField(max_length=40)
    State = models.CharField(max_length=40)
class login(models.Model):
    Name = models.CharField(max_length=40)
    Password = models.CharField(max_length=40)
    Submit = models.CharField(max_length=40)
class Test(models.Model):
    Questions=models.CharField(max_length=40)
    Answers=models.CharField(max_length=40)

class CPTest(models.Model):
    Questions=models.CharField(max_length=40)
    Answers=models.CharField(max_length=40)
# Create your models here.
