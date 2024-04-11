from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class cList(models.Model):
    cOwner = models.CharField(max_length=32)
    cModel = models.CharField(max_length=32)
    cSerial = models.CharField(max_length=32)
    cBuyDate = models.DateField