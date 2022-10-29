from ssl import create_default_context
from turtle import title
from django.db import models

# Create your models here.

class App1(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    hits=models.PositiveIntegerField(default = 0)#조회 수 
