from django.db import models
from datetime import datetime
from data.models import Data
from platforms.choices import status_choices

# Create your models here.
class Platform(models.Model):
    data= models.ForeignKey(Data, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    # category=models.CharField(choices=status_choices, max_length=3)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=20)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    minprice=models.IntegerField()
    maxprice=models.IntegerField()
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published=models.BooleanField(default=True)
    invest_date=models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
      return self.title