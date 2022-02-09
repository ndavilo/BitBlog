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

class Cryptocoin(models.Model):
	bitcoin_value		= models.FloatField()
	etherem_value		= models.FloatField()
	tether_value		= models.FloatField()
	binance_value		= models.FloatField()
	date_time			= models.DateTimeField(auto_now=True)

	def __str__(self):
		return ' Bitcoin: ' +str(self.bitcoin_value) + ' | ' +str(self.date_time)

	def get_absolute_url(self):
		return reverse('home')
