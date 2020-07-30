from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Vendor(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    date_added=models.DateField(auto_now_add=True)
    

 class User(AbstractBaseUser):
    email = models.EmailField(
        user_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) 
    # a admin user; non super-user
    admin = models.BooleanField(default=False) 
    # a superuser
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
   

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Vendor_detail", kwargs={"pk": self.pk})

# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    date_added = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=75, blank=False, null=False)
    review = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.TextField(null= True, blank=True)


