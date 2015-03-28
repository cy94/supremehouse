from django.db.models.signals import post_delete
from django.db import models

from django.dispatch import receiver

import os

# returns the upload path for an image
# -> products/<product name>/<file name>
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

# deletes the image file when the object is deleted
@receiver(post_delete, sender=ProductImage)
def image_post_delete_handler(sender, **kwargs):
    image = kwargs['instance']
    storage, path = image.image.storage, image.image.path
    storage.delete(path)	

