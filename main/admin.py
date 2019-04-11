from django.contrib import admin
from main.models import *


class PropertyImageInline(admin.TabularInline):
    model = Pics
    extra = 1


class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline, ]

admin.site.register(Glava, PropertyAdmin)


admin.site.register(Author)
admin.site.register(Tags)
#admin.site.register(Glava)
admin.site.register(Pics)
admin.site.register(Manga)







