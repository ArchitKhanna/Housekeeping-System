from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

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

class apartment(models.Model):
    number = models.IntegerField(unique=True, null=False, blank=False)
    block = models.ForeignKey(block, on_delete=models.DO_NOTHING, null=False, blank=False)
    status = models.ForeignKey(status, on_delete=models.DO_NOTHING, null=False, blank=False)
    task = models.ForeignKey(task, on_delete=models.DO_NOTHING, null=False, blank=False)
    assignee = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    #def __str__(self):
    #    return self.assignee

    def get_absolute_url(self):
        return reverse('hk-ThomondVillage')
