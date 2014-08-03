from django.db import models
from django_autoslug.fields import AutoSlugField




class Contact(models.Model):
	name = models.CharField(max_length=100)
	phone = models.IntegerField(max_length=10)
	email = models.EmailField()
	slug = AutoSlugField(populate_from='name')

	def __unicode__(self):
		return self.name
