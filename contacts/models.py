from django.db import models
from datetime import datetime

class Contact(models.Model):
    listing = models.CharField(max_length=150)
    listingid = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    contactdate = models.DateTimeField(default=datetime.now, blank=True)
    userid = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return self.name