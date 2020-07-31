from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):

    # add additional fields in here

    def __str__(self):
        return self.email
