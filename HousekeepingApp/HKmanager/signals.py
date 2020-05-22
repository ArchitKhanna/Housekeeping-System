from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import (
                    apartment,
                    numberOfRooms,
                    livingRoom,
                    kitchen,
                    corridor,
                    bedroom,
                    ensuite,
                    bathroom
                    )

#Create Living Room object for each Apartment
@receiver(post_save, sender=apartment)
def create_livingRoom(sender, instance, created, **kwargs):
    if created:
        livingRoom.objects.create(apartment=instance)

@receiver(post_save, sender=apartment)
def save_livingRoom(sender, instance, **kwargs):
    instance.livingroom.save()

#Create kitchen object for each Apartment
@receiver(post_save, sender=apartment)
def create_kitchen(sender, instance, created, **kwargs):
    if created:
        kitchen.objects.create(apartment=instance)

@receiver(post_save, sender=apartment)
def save_kitchen(sender, instance, **kwargs):
    instance.kitchen.save()

#Create corridor object for each Apartment
@receiver(post_save, sender=apartment)
def create_corridor(sender, instance, created, **kwargs):
    if created:
        corridor.objects.create(apartment=instance)

@receiver(post_save, sender=apartment)
def save_corridor(sender, instance, **kwargs):
    instance.corridor.save()

#Create bedroom objects for each Apartment
@receiver(post_save, sender=apartment)
def create_bedroom(sender, instance, created, **kwargs):
    if created:
        x = instance.rooms.capacity
        for i in range(x):
            bedroom.objects.create(apartment=instance, number=i+1)
            #bedroom.objects.save()

#@receiver(post_save, sender=apartment)
#def save_bedroom(sender, instance, **kwargs):
#    instance.bedroom.save()
