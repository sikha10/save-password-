from unittest.util import _MAX_LENGTH
from django.db import models

class Profile_info(models.Model):
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    key = models.CharField(max_length=120, null=True)


class Saved_info(models.Model):
    user = models.CharField(max_length=120)
    password = models.CharField(max_length=120, null=True)
    name = models.CharField(max_length=120, null=True)
    key = models.CharField(max_length=120, null=True)