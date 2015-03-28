from django.contrib import admin
from services.models import Service, ServiceImage

# Register your models here.
class ServiceImageInline(admin.TabularInline):
	model = ServiceImage
	extra = 3

class ServiceAdmin(admin.ModelAdmin):
	inlines = [ ServiceImageInline, ]
	list_display = ['name']

admin.site.register(Service, ServiceAdmin)
