from django.contrib import admin
from volunteers import models

# Register your models here.
admin.site.register(models.Institution)
admin.site.register(models.Program)
admin.site.register(models.VolunteerRegistry)
