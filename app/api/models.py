from django.db import models

# Create your models here.

class Count(models.Model):
    visit = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)