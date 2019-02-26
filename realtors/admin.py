from django.contrib import admin
from . import models

class RealtorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "hiredate",)
    list_display_links = ("id", "name",)
    search_fields = ("name",)
    list_per_page = 20

admin.site.register(models.Realtor, RealtorAdmin)
