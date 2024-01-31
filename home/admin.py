from django.contrib import admin
from django.utils.safestring import mark_safe

from home.models import *


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: contain" />')

    get_image.short_description = 'Изображение'


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'phone', 'image')


class BoardOfTrusteesAdmin(admin.ModelAdmin):
    list_display = ('name',)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at', 'is_check')


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone')


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(BoardOfTrustees, BoardOfTrusteesAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Contacts, ContactsAdmin)
