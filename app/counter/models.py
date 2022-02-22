from django.db import models

# Create your models here.

class Count(models.Model):
    number_view = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)