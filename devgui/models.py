from django.db import models
from django.utils import timezone
from usergui.models import *

# Create your models here.
class Employee (models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Developer(Employee):
    phone = models.CharField(max_length=25)
    devices = models.TextField()
    first_workday = models.DateTimeField(default=timezone.now)

class Software(models.Model):
    name = models.CharField(max_length=100)
    scrum_master = models.ForeignKey(Employee, on_delete=models.CASCADE)
    qa = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Release(Software):
    suffix = models.CharField(max_length=100)
    release_date = models.DateTimeField(default=timezone.now)
    improvements = models.TextField()
    state = models.CharField(max_length=25)

    def __str__(self):
        return self.name + " " + self.suffix

class Ticket(Complaint):
    timestamp = models.DateTimeField(default=timezone.now)
    priority = models.IntegerField()
    id_developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    solved = models.BooleanField(default=False)
    implemented = models.BooleanField(default=False)

class Contract(models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_release = models.ForeignKey(Release, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    duration = models.DurationField()

    def __str__(self):
        return str(self.id_client) + " " + str(self.id_release)
