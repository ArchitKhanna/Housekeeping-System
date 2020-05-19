from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class apartment(models.Model):
    number = models.IntegerField(unique=True, null=False, blank=False)
    block = models.TextField(null=False, blank=False)
    status = models.TextField(null=False, blank=False)
    task = models.TextField(null=False, blank=False)
    assignee = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    #def __str__(self):
    #    return self.assignee

class block(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

class status(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

class task(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
