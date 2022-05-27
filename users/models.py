from django.db import models

class Users(models.Model):
    title = models.CharField(max_length=120)