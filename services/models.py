import os
from django.db import models

def get_upload_path(instance, filename):
	path = os.path.join('services', instance.service.name, filename)
	return path

# Create your models here.
class Service(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()

class ServiceImage(models.Model):
	service = models.ForeignKey(Service, related_name='images')
	image = models.ImageField(upload_to=get_upload_path)

	def image_tag(self):
	    return u'<img src="%s" />' % self.url
	image_tag.short_description = 'Image'
	image_tag.allow_tags = True