from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="نام")
    descrtiption = models.TextField(verbose_name="توضیحات")
    
