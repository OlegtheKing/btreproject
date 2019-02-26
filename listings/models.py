from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=15)
    description = models.TextField(blank=True)  # blank = optional
    price = models.IntegerField()
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.PositiveSmallIntegerField(default=0)
    sqft = models.IntegerField()
    lotsize = models.DecimalField(max_digits=4, decimal_places=1)
    mainimg = models.ImageField(upload_to="photos/%Y/%m/%d/")
    secimg1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    secimg2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    secimg3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    secimg4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    secimg5 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    secimg6 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    ispublished = models.BooleanField(default=True)
    listdate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
