from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(User)
    comment = models.CharField(max_length=200)