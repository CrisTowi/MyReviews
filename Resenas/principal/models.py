from django.db import models

# Create your models here.
class Usuario(models.Model):
	nombre = models.CharField(max_length= 50)
	edad = models.PositiveIntegerField()
	fechaNac = models.DateField()

	def __unicode__(self):
		return self.Nombre

class Resena(models.Model):
	texto = models.TextField()
	fechaPost = models.DateTimeField(auto_now_add = True, blank = True)
	usuario = models.ForeignKey(Usuario)

	def __unicode__(slef):
		return self.fechaPost

