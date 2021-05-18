from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    quantity = models.CharField(max_length=10)

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
