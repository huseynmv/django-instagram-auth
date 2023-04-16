from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), blank=True, unique=True)
    is_active = True
    followers = models.IntegerField(blank=True, null=True, default=0)
    following = models.IntegerField(blank=True, null=True, default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
