from operator import mod
from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)