from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model

class CustomUser(User):
    age = models.PositiveIntegerField(

    )

class Applications(models.Model):
    name = models.CharField(
        max_length = 255
    )
    email = models.EmailField(
        max_length=255,
        unique=True
    )
    phone = models.IntegerField(
    )
    date =  models.DateTimeField(
        auto_now=True
    )
