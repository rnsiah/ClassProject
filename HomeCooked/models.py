from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, AbstractUser
)
from phonenumber_field.modelfields import PhoneNumberField



class Kitchn(models.Model):
    legal_name = models.CharField(max_length=50, blank=False, null=True)
    date_added=models.DateField(auto_now_add=True)
    vendor_email=models.EmailField(max_length=254, blank=False, null=True)
    address = models.CharField(max_length=200, blank=False, null =True)
    phone_number=PhoneNumberField(null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Vendor_detail", kwargs={"pk": self.pk})

    
# Create your models here.

#Changed the description to a text field because it doesn't limit the meals description
class Meal(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField(blank=False, null=False)
    review = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.TextField(null= True, blank=True)


    def __str__(self):
        return self.name
    


