from django.contrib import admin

# Register your models here.
from .models import Category, Property
from django.contrib import admin
from .models import PropertyImage
from PIL import Image

class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'display_thumbnail')
    readonly_fields = ('display_thumbnail',)

    def display_thumbnail(self, obj):
        return obj.get_thumbnail_html()

    display_thumbnail.short_description = 'Thumbnail Preview'

admin.site.register(PropertyImage, PropertyImageAdmin)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'price')
    list_filter = ('category',)



admin.site.register(Category)
admin.site.register(Property, PropertyAdmin)
