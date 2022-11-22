from django.db import models

# Create your models here.

class Entry(models.Model):
    date = models.DateField()
    author = models.CharField(max_length=255)
    post_text = models.CharField(max_length=255)