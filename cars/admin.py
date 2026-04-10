from django.contrib import admin
from .models import Car, Brand
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'year', 'model_year', 'price', 'plate', 'photo')
    search_fields = ('name','brand')
    list_filter = ('brand', 'year') 
    ordering = ('id',)

admin.site.register(Car, CarAdmin)



class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('id',)        
admin.site.register(Brand, BrandAdmin)
