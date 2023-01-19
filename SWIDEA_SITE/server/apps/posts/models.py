from django.db import models

import os
import django

# environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# Create your models here.


class Devtool(models.Model):
    name = models.CharField(max_length=64, blank=True)
    kind = models.CharField(max_length=64, blank=True)
    content = models.CharField(max_length=64, blank=True)

class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    interest = models.CharField(max_length=16)
    price = models.IntegerField()
    image = models.ImageField(blank = True, upload_to='posts/%Y%m%d')
    tool = models.ForeignKey(Devtool, on_delete=models.CASCADE, related_name="Post_tool")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)