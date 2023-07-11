from django.contrib import admin
from . import models

admin.site.register(models.Notification)
admin.site.register(models.Project)
admin.site.register(models.Role)
admin.site.register(models.Tasks)