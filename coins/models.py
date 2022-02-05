from django.db import models

# Create your models here.

class Chart(models.Model):
	name 		= models.CharField(max_length=50)
	value		= models.FloatField()
	date_time	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name + ' | ' +str(self.value) + ' | ' +str(self.date_time)

	def get_absolute_url(self):
		return reverse('home')

class Bitcoin(models.Model):
	name 		=	"Bitcoin"
	value 		=	models.FloatField()
	date_time	= 	models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name + ' | ' +str(self.value) + ' | ' +str(self.date_time)

	def get_absolute_url(self):
		return reverse('home')

class Tether(models.Model):
	name 		=	"Tether"
	value 		=	models.FloatField()
	date_time	= 	models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name + ' | ' +str(self.value) + ' | ' +str(self.date_time)

	def get_absolute_url(self):
		return reverse('home')

class Ethereum(models.Model):
	name 		=	"Ethereum"
	value 		=	models.FloatField()
	date_time	= 	models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name + ' | ' +str(self.value) + ' | ' +str(self.date_time)

	def get_absolute_url(self):
		return reverse('home')

class Binance(models.Model):
	name 		=	"Binance"
	value 		=	models.FloatField()
	date_time	= 	models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name + ' | ' +str(self.value) + ' | ' +str(self.date_time)

	def get_absolute_url(self):
		return reverse('home')