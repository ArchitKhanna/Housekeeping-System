from django.contrib import admin

# Register your models here.

from .models import (
                    Announcement,
                    apartment,
                    block,
                    status,
                    task,
                    villages,
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

admin.site.register(Announcement)
admin.site.register(villages)
admin.site.register(apartment)
admin.site.register(block)
admin.site.register(status)
admin.site.register(task)
admin.site.register(numberOfRooms)
admin.site.register(livingRoom)
admin.site.register(kitchen)
admin.site.register(corridor)
admin.site.register(bedroom)
admin.site.register(ensuite)
admin.site.register(bathroom)
admin.site.register(taskslivingRoom)
admin.site.register(tasksKitchen)
admin.site.register(tasksCorridor)
admin.site.register(tasksBedroom)
admin.site.register(tasksEnsuite)
admin.site.register(livingRoomCheckList)
admin.site.register(kitchenCheckList)
admin.site.register(corridorCheckList)
admin.site.register(bedroomCheckList)
admin.site.register(ensuiteCheckList)
