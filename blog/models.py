from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
	name 		= models.CharField(max_length=50)
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')


class Post(models.Model):
	title 		= models.CharField(max_length=50)
	author 		= models.ForeignKey(User, on_delete=models.CASCADE)
	body		= models.TextField()
	date_time	= models.DateTimeField(auto_now=True)
	category	= models.CharField(max_length=50, default='Sell')
	likes		= models.ManyToManyField(User, related_name='blog_posts')

	def __str__(self):
		return self.title + ' | by:' +str(self.author)+ ' | ' +str(self.date_time)

	def get_absolute_url(self):
		return reverse('article_detail', args=(str(self.id)))

