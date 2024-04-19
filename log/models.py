from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime



class User(AbstractUser):
    pass

class cList(models.Model):
    cOwner = models.CharField(max_length=32)
    cModel = models.CharField(max_length=32)
    cSerial = models.CharField(max_length=32)
    cBuyDate = models.DateField()

    def warrantyVoid(self):
        return (datetime.date.today() - self.cBuyDate).days > 730
        
    def remainingDays(self):
        return 730 - (datetime.date.today() - self.cBuyDate).days
        

    def __str__(self) -> str:
        return self.cOwner

class visitCategory(models.Model):
    visitReason = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.visitReason

class cVisit(models.Model):
    itemDetails = models.ForeignKey(cList, on_delete=models.Case, blank='True', null='True', related_name="details")
    visitReason = models.ForeignKey(visitCategory, on_delete=models.CASCADE, blank="True", null="True", related_name="vReason")
    visitDate = models.DateField()
    workingHours = models.IntegerField(default=0)
    loadHours = models.IntegerField(default=0)

    
    

