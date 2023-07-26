from django.db import models
from django.contrib.auth.models import User

class Daily(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food = models.IntegerField()
    transport = models.IntegerField()
    entertain = models.IntegerField()
    stationary = models.IntegerField()
    misc = models.IntegerField()

class Monthly(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent = models.IntegerField()
    utilities = models.IntegerField()
    personal_care = models.IntegerField()
    communication = models.IntegerField()
    health = models.IntegerField()

class income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inc=models.IntegerField()