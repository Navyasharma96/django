from django.db import models

# Create your models here.

class register(models.Model):
    Name=models.CharField(max_length=40)
    Phno=models.BigIntegerField()
    DOB=models.DateField()
    Adress=models.CharField(max_length=70)
    Qualification=models.CharField(max_length=20)
    Email = models.CharField(max_length=40)
    Password = models.CharField(max_length=255)

    def __str__(self):
      return self.Name

class about(models.Model):
    INTREST=models.CharField(max_length=255)
    Hobbies=models.CharField(max_length=255)
    Bio=models.CharField(max_length=255)


class UserModel(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=225)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)