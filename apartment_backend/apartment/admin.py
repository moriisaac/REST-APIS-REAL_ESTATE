from django.contrib import admin

from .models import Apartment, Land, Realtor, Offices


# Register your models here.
class ApartmentListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'apart_name', 'is_published', 'cost', 'list_date', 'realtor')
    list_display_links = ('id', 'apart_name')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('apart_name', 'description', 'address', 'city', 'cost')
    list_per_page = 10


class OfficeListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'office_name', 'is_published', 'cost', 'list_date', 'realtor')
    list_display_links = ('id', 'office_name')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('office_name', 'description', 'address', 'city', 'cost')
    list_per_page = 10


class LandListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'land_name', 'is_published', 'cost', 'list_date', 'realtor')
    list_display_links = ('id', 'land_name')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('land_name', 'description', 'address', 'city', 'cost')
    list_per_page = 10


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
admin.site.register(Apartment, ApartmentListingAdmin)
admin.site.register(Land, LandListingAdmin)
admin.site.register(Offices, OfficeListingAdmin)
# admin.site.register(UserProfile)
