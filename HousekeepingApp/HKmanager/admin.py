from django.contrib import admin

# Register your models here.

from .models import (
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
                    bathroom
                    )

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
