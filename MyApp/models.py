from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    quantity = models.CharField(max_length=10)

class Bill(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    payment = models.CharField(max_length=50)
    cardname = models.CharField(max_length=50)
    cardnumber = models.BigIntegerField()

    def register(self):
        self.save()

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
