from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model

class CustomUser(User):
    age = models.PositiveIntegerField(

    )

class Applications(models.Model):
    name = models.CharField(
        max_lenght = 50
    )
    email = models.EmailField(
        max_length=255,
        unique=True
    )
    phone = models.IntegerField(
        max_lenght = 50
    )
    date =  models.DateTimeField(
        auto_now=True
    )
