from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','selling_price','discounted_price','category','brand')


admin.site.register(Product,ProductAdmin)
admin.site.register(Brand_name)
admin.site.register(Category)
