from django.contrib import admin
from . import models

admin.site.register(models.Video)
admin.site.register(models.Category)
admin.site.register(models.Like)
admin.site.register(models.Comment)
