from django.db import models

# Create your models here.
class DbForm(models.Model):
    Id = 'UP28349457'
    First_name = models.CharField(max_length=30 , primary_key=True)
    Last_name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Phone = models.IntegerField()
    Password = models.CharField(max_length=30)

    # def __str__(self) -> str:
    #     return self.First_name
class User(models.Model):
    name = models.CharField(max_length=50)
    site = models.URLField( max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

class rabel(models.Model):
    name = models.CharField(max_length=50)