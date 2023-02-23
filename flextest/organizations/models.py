from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    
    

    
class User(AbstractUser):
    object = CustomUserManager()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11}$',
                                 message="Не корректный формат номера телефона")
    
    username = None    
    email = models.EmailField(
            verbose_name='email address',
            max_length=255,
            unique=True,
    )
    phone = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    icon = models.ImageField(upload_to="uploads/users/", blank=True)
    organizations = models.ManyToManyField(Organization, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    # def get_organizations(self):
        

