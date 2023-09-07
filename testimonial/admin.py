from django.contrib import admin
from .models import Testimonial
# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Testimonial,TestimonialAdmin)
