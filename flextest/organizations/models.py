from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from PIL import Image
import os



class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    
    
class User(AbstractUser):
    
    
    def path_and_rename(instance, filename):
        
        ext = filename.split('.')[-1]

        filename = '{}.{}'.format(instance.pk, ext)

        return os.path.join("uploads/users/", filename)

    
    
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
    icon = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    organizations = models.ManyToManyField(Organization, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    def save(self,*args, **kwargs):
        super().save()  
        
        if(self.icon):
            
            img = Image.open(self.icon.path) 

            if img.height > 200 or img.width > 200:
                new_img = (200, 200)
                img.thumbnail(new_img)
                img.save(self.icon.path)
                
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    
        

