from django.db import models
from django.utils import timezone
from devgui.models import *

# Create your models here.

class Client (models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class User (models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    creation_timestamp = models.DateTimeField(default=timezone.now)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Complaint (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_release = models.ForeignKey(Release, on_delete=models.CASCADE)
    creation_timestamp = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return str(self.id_user) + str(creation_timestamp)
