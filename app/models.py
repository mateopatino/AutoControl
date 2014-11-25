from django.db import models

# Create your models here.

class DEPARTAMENTOS(models.Model):
	cdepa=models.AutoField(primary_key=True)
	ndepa=models.CharField(max_length=45)

	def __unicode__(self):
		return self.ndepa

class CIUDADES(models.Model):
	cdepa=models.AutoField(primary_key=True)
	cciuda=models.IntegerField()
	nciudad=models.CharField(max_length=45)

	def __unicode__(self):
		return self.nciudad

class TIPOVEHICULOS(models.Model):
	ctivehi=models.AutoField(primary_key=True)
	ntivehi=models.CharField(max_length=45)

	def __unicode__(self):
		return self.ntivehi

class TIPODEDOCU(models.Model):
	ctideid=models.AutoField(primary_key=True)
	ntideid=models.CharField(max_length=20)

	def __unicode__(self):
		return self.ntideid

class CLIENTES(models.Model):
	cclientes=models.AutoField(primary_key=True)
	nombres=models.CharField(max_length=45)
	#fnaci=models.DateField()
	cedula=models.IntegerField()
	ctideid=models.ForeignKey('TIPODEDOCU')
	cdepa=models.ForeignKey('DEPARTAMENTOS')
	cciudad=models.ForeignKey('CIUDADES')

	def __unicode__(self):
		return self.nombres

class VEHICULOS(models.Model):
	"""docstring for vehiculos"""
	placas=models.CharField(primary_key=True , max_length=10) #ESTA LINEA ME GENERO UN ERROR
	color=models.CharField(max_length=45)
	modelo=models.CharField(max_length=45)
	capacidadpersonas=models.IntegerField()
	cilindraje=models.CharField(max_length=45)
	cclientes=models.ForeignKey(CLIENTES)
	ctivehi=models.ForeignKey(TIPOVEHICULOS)

	def __unicode__(self):
		return str (self.pk)





