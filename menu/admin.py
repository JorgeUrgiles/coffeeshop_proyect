from django.contrib import admin
from .models import Category, Menu
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Category,CategoryAdmin)

class MenuAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Menu,MenuAdmin)

