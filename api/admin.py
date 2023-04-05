from django.contrib import admin
from .models import Customer,Product
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','customer_name','address','email','phone_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','product_name','price','quantity','sku','customer')
