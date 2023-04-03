from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "realtor" ,"is_published", "price",)
    list_display_links = ("id", "title",)
    list_filter = ("realtor",)
    list_editable = ("is_published",)
    search_fields = ("realtor", "title", "description", "city", "state", "price", "address")  
    list_per_page = 25
    
admin.site.register(Listing, ListingAdmin)