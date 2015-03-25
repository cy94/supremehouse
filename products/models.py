import os
from django.db import models

def get_upload_path(instance, filename):
	path = os.path.join('products', instance.product.name, filename)
	return path

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()

class ProductImage(models.Model):
	product = models.ForeignKey(Product, related_name='images')
	image = models.ImageField(upload_to=get_upload_path)