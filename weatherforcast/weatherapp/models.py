from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class RecentSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1,)
    weather = models.CharField(max_length=200)
    temperature = models.CharField(max_length=200)
    humidity = models.CharField(max_length=200)
