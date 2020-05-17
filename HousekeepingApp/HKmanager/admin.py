from django.contrib import admin

# Register your models here.

from .models import apartment, block, status, task

admin.site.register(apartment)
admin.site.register(block)
admin.site.register(status)
admin.site.register(task)
