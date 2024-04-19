from django.db import models

# Create your models here.

class Coach(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0.0)
    age = models.IntegerField(default=0)
    image = models.ImageField(upload_to = "coachs", blank=True, null=True)
    