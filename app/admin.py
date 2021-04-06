from django.contrib import admin
from .models import *
# Register your models here.

class ImageInline(admin.StackedInline):
    model = Image
    
class ImageAdmin(admin.ModelAdmin):
    list_filter = ['product']

class OrderInline(admin.StackedInline):
    model = Order

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_filter = ['category' ,'orders','orders__quantity']

class OrderUserAdmin(admin.ModelAdmin):
    inlines = [OrderInline]
    list_filter = ['orders__accepted', 'orders__quantity', 'orders__product']

class ProductInline(admin.StackedInline):
    model = Product

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_filter = ['accepted', 'quantity', 'order_user', 'product']
    search_fields = ['order_user__email', 'product__title']

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_filter = ['main_category', 'products__title']
    search_fields = ['title']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderUser, OrderUserAdmin)