from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','selling_price','discounted_price','category','brand')


@admin.register(Customer)
class CustomerAdimn(admin.ModelAdmin):
    list_display=('id','user','locality','city','state','pincode')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('id','user','product','quantity')


admin.site.register(Product,ProductAdmin)
admin.site.register(Brand_name)
admin.site.register(Category)
