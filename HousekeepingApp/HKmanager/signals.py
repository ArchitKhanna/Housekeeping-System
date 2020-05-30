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
                    bathroom,
                    taskslivingRoom,
                    tasksKitchen,
                    tasksCorridor,
                    tasksBedroom,
                    tasksEnsuite,
                    livingRoomCheckList,
                    kitchenCheckList,
                    corridorCheckList,
                    bedroomCheckList,
                    ensuiteCheckList
                    )

#CREATING VARIOUS SUB-OBJECTS FOR EACH APARTMENT
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

#Create ensuite object for each bedroom
@receiver(post_save, sender=bedroom)
def create_ensuite(sender, instance, created, **kwargs):
    if created:
        ensuite.objects.create(apartment=instance.apartment, bedroom=instance)

@receiver(post_save, sender=bedroom)
def save_ensuite(sender, instance, **kwargs):
    instance.ensuite.save()

#CREATING CHECKLISTS FOR EACH APARTMENT AND SUB-OBJECTS
#Creating Living Room Checklist
@receiver(post_save, sender=livingRoom)
def create_livingRoomCheckList(sender, instance, created, **kwargs):
    if created:
        tasks = taskslivingRoom.objects.all()
        for task in tasks:
            livingRoomCheckList.objects.create(
                                               livingroom=instance,
                                               task=task
                                              )

#Creating Kitchen Checklist
@receiver(post_save, sender=kitchen)
def create_KitchenCheckList(sender, instance, created, **kwargs):
    if created:
        tasks = tasksKitchen.objects.all()
        for task in tasks:
            kitchenCheckList.objects.create(
                                            kitchen=instance,
                                            task=task
                                           )

#Creating Corridor Checklist
@receiver(post_save, sender=corridor)
def create_CorridorCheckList(sender, instance, created, **kwargs):
    if created:
        tasks = tasksCorridor.objects.all()
        for task in tasks:
            corridorCheckList.objects.create(
                                             corridor=instance,
                                             task=task
                                            )

#Creating Room Checklist (for each room)
@receiver(post_save, sender=bedroom)
def create_RoomCheckList(sender, instance, created, **kwargs):
    if created:
        tasks = tasksBedroom.objects.all()
        for task in tasks:
            bedroomCheckList.objects.create(
                                            bedroom=instance,
                                            task=task
                                           )

#Creating Ensuite Checklist (for each ensuite)
@receiver(post_save, sender=ensuite)
def create_EnsiteCheckList(sender, instance, created, **kwargs):
    if created:
        tasks = tasksEnsuite.objects.all()
        for task in tasks:
            ensuiteCheckList.objects.create(
                                            ensuite=instance,
                                            task=task
                                           )
