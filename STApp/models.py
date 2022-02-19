from distutils.command.upload import upload
from email.mime import image
from django.db import models


# Create your models here.

class GalaryModel(models.Model):
    pics = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=30)
    price = models.IntegerField()