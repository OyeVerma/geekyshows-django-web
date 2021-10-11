from django.db import models

# Create your models here.
class StudentRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    passw = models.CharField(max_length=50)