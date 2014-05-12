from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
#Modelos controlan los datos. Hay que tener cuidado.
class signUp(models.Model):
	"""Modelo para un login sencillo"""
	#Null, blank, son para dejarlos en blanco en la db y la pagina.
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_unicode(self.email)