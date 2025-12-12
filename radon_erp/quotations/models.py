from django.db import models

# Create your models here.

class Quotaion(models.Model):
    customer_name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    date=models.DateTimeField(max_length=10)