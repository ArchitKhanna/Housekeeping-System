from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class villages(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

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

class numberOfRooms(models.Model):
    capacity = models.IntegerField(unique=True, null=False, blank=False)

    def __str__(self):
        return str(self.capacity)

class apartment(models.Model):
    number = models.IntegerField(unique=True, null=False, blank=False)
    rooms = models.ForeignKey(numberOfRooms, on_delete=models.DO_NOTHING, null=False, blank=False, default=0)
    block = models.ForeignKey(block, on_delete=models.DO_NOTHING, null=False, blank=False)
    status = models.ForeignKey(status, on_delete=models.DO_NOTHING, null=False, blank=False)
    task = models.ForeignKey(task, on_delete=models.DO_NOTHING, null=False, blank=False)
    assignee = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        return reverse('hk-ThomondVillage')

    def __str__(self):
        return str(self.number)

class livingRoom(models.Model):
    apartment = models.OneToOneField(apartment, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(livingRoom, self).save(*args, **kwargs)

class kitchen(models.Model):
    apartment = models.OneToOneField(apartment, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(kitchen, self).save(*args, **kwargs)

class corridor(models.Model):
    apartment = models.OneToOneField(apartment, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(corridor, self).save(*args, **kwargs)

class bedroom(models.Model):
    apartment = models.ForeignKey(apartment, on_delete=models.CASCADE, default=0)
    number = models.IntegerField(null=False, blank=False, default=0)

class ensuite(models.Model):
    apartment = models.OneToOneField(apartment, on_delete=models.CASCADE)
    bedroom = models.OneToOneField(bedroom, on_delete=models.CASCADE)

class bathroom(models.Model):
    apartment = models.OneToOneField(apartment, on_delete=models.CASCADE)
