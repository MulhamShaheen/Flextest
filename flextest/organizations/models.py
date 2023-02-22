from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    
    
class user(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11}$',
                                 message="Не корректный формат номера телефона")
    
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    phone = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    icon = models.ImageField(upload_to="uploads/users/")
    organizations = models.ManyToManyField(Organization)
    

