from django.contrib import admin
from . import models

class ListingAdmin(admin.ModelAdmin):  # overriding base output to admin panel
    list_display = ("id", "title", "ispublished", "price", "listdate", "realtor",)
    list_display_links = ("id", "title",)
    list_filter = ("realtor",)
    list_editable = ("ispublished", )
    search_fields = ("title", "address", "city", "state", "zipcode", "price")
    list_per_page = 20

admin.site.register(models.Listing, ListingAdmin)
