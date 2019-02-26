from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="photos/realtors")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    ismvp = models.BooleanField(default=False)
    hiredate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
