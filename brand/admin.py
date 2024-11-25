from django.contrib import admin
from brand.models import BrandModel
# Register your models here.

# admin.site.register(BrandModel)

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('Brand_Name',)}
    list_display = ['Brand_Name', 'slug']
admin.site.register(BrandModel, BrandAdmin)