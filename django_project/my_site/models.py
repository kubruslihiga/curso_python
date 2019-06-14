from django.db import models


# Create your models here.
class URLCoder(models.Model):
    url = models.CharField(max_length=255, default="https://www.google.com")
