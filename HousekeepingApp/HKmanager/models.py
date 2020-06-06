from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import get_template
# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('hk-Home')

class villages(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

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
        return reverse('hk-villagepanel')

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):

            if apartment.objects.filter(pk=self.pk).exists():

                apt = apartment.objects.get(pk=self.pk)
                sender = apt.assignee

                temp = get_template('email1.html')

                details = {
                            'sender': sender,
                            'to': self.assignee.first_name,
                            'apartment': self,
                          }

                html_content = temp.render(details)

                send_mail(
                            'Apartment Assignment Notification',
                            html_content,
                            'housekeeper.cls@gmail.com',
                            [self.assignee.email],
                            fail_silently=False,
                            html_message=html_content,
                         )
            else:

                temp = get_template('email2.html')

                details = {
                            'to': self.assignee.first_name,
                            'apartment': self,
                          }

                html_content = temp.render(details)

                send_mail(
                            'Apartment Assignment Notification',
                            html_content,
                            'housekeeper.cls@gmail.com',
                            [self.assignee.email],
                            fail_silently=False,
                            html_message=html_content,
                         )

            super(apartment, self).save(*args, **kwargs)


class livingRoom(models.Model):
    apartment = models.OneToOneField(apartment, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(livingRoom, self).save(*args, **kwargs)

class taskslivingRoom(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.description)

    def save(self, *args, **kwargs):
        super(taskslivingRoom, self).save(*args, **kwargs)

class livingRoomCheckList(models.Model):
    livingroom = models.ForeignKey(livingRoom, on_delete=models.CASCADE)
    task = models.ForeignKey(taskslivingRoom, on_delete=models.DO_NOTHING)
    checked = models.BooleanField(default=False)
    callback = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(livingRoomCheckList, self).save(*args, **kwargs)

class kitchen(models.Model):
    apartment = models.OneToOneField(apartment, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(kitchen, self).save(*args, **kwargs)

class tasksKitchen(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False)

    def save(self, *args, **kwargs):
        super(tasksKitchen, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.description)

class kitchenCheckList(models.Model):
    kitchen = models.ForeignKey(kitchen, on_delete=models.CASCADE)
    task = models.ForeignKey(tasksKitchen, on_delete=models.DO_NOTHING)
    checked = models.BooleanField(default=False)
    callback = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(kitchenCheckList, self).save(*args, **kwargs)

class corridor(models.Model):
    apartment = models.OneToOneField(apartment, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(corridor, self).save(*args, **kwargs)

class tasksCorridor(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False)

    def save(self, *args, **kwargs):
        super(tasksCorridor, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.description)

class corridorCheckList(models.Model):
    corridor = models.ForeignKey(corridor, on_delete=models.CASCADE)
    task = models.ForeignKey(tasksCorridor, on_delete=models.DO_NOTHING)
    checked = models.BooleanField(default=False)
    callback = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(corridorCheckList, self).save(*args, **kwargs)

class bedroom(models.Model):
    apartment = models.ForeignKey(apartment, on_delete=models.CASCADE, default=0)
    number = models.IntegerField(null=False, blank=False, default=0)

class tasksBedroom(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False)

    def save(self, *args, **kwargs):
        super(tasksBedroom, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.description)

class bedroomCheckList(models.Model):
    bedroom = models.ForeignKey(bedroom, on_delete=models.CASCADE)
    task = models.ForeignKey(tasksBedroom, on_delete=models.DO_NOTHING)
    checked = models.BooleanField(default=False)
    callback = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(bedroomCheckList, self).save(*args, **kwargs)

class ensuite(models.Model):
    apartment = models.ForeignKey(apartment, on_delete=models.CASCADE)
    bedroom = models.OneToOneField(bedroom, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(ensuite, self).save(*args, **kwargs)

class tasksEnsuite(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False)

    def save(self, *args, **kwargs):
        super(tasksEnsuite, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.description)

class ensuiteCheckList(models.Model):
    ensuite = models.ForeignKey(ensuite, on_delete=models.CASCADE, default=0)
    task = models.ForeignKey(tasksEnsuite, on_delete=models.DO_NOTHING)
    checked = models.BooleanField(default=False)
    callback = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(ensuiteCheckList, self).save(*args, **kwargs)

class bathroom(models.Model):
    apartment = models.OneToOneField(apartment, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(bathroom, self).save(*args, **kwargs)
