from django.db import models

# Create your models here.

class Describe(models.Model):
   name = models.TextField()
   text = models.TextField()