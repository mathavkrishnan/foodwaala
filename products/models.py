from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GEEKS_CHOICES =(
    ("1", "Breakfast"),
    ("2", "Lunch"),
    ("3", "Dinner"),
    ("4", "All"),
)

class Cart(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    images = models.URLField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Prod(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    rating  = models.IntegerField()
    foodtype = models.TextField(max_length=100,choices=GEEKS_CHOICES)
    images = models.ImageField(upload_to='my_picture',blank=True)

    def __str__(self):
        return self.title