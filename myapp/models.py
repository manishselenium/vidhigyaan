from datetime import date
from distutils.archive_util import make_zipfile
import email
from email.policy import default
from pyexpat import model
from unicodedata import name
from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12, default='9752324265')
    desc = models.TextField()
    date = models.DateField()

def __str__(self):
    return self.phone

class Payment(models.Model):
  name = models.CharField(max_length=122)
  amount = models.CharField(max_length=122) 
  orderId = models.CharField(max_length=122, blank=True)
  RazorPay_Payment_Id = models.CharField(max_length=122, blank=True)
  phone = models.CharField(max_length=12)
  paid = models.BooleanField(default=False)