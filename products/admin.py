from django.contrib import admin
from products.models import Product, ProductImage

# Register your models here.
class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 3

class ProductAdmin(admin.ModelAdmin):
	inlines = [ ProductImageInline, ]

admin.site.register(Product, ProductAdmin)