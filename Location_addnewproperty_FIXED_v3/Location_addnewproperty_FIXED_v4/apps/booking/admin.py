from django.contrib import admin

# Register your models here.
from .models import Booking, BookingItem

class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'place', 'phone')
    search_fields = ['first_name', 'phone', 'place']

class BookingItemAdmin(admin.ModelAdmin):

    search_fields = ['price']


admin.site.register(Booking, BookingAdmin)
admin.site.register(BookingItem, BookingItemAdmin)
