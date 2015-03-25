import os
from django.db import models

def get_upload_path(instance, filename):
	path = os.path.join('services', instance.service.name, filename)
	return path

# Create your models here.
class Service(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()

class ProductImage(models.Model):
	service = models.ForeignKey(Service, related_name='images')
	image = models.ImaegField(upload_to=get_upload_path)