from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField 



class Category(models.Model):
	name 		= models.CharField(max_length=50)
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')


class Post(models.Model):
	title 		= models.CharField(max_length=50)
	author 		= models.ForeignKey(User, on_delete=models.CASCADE)
	body		= RichTextField(blank=True, null=True)
	date_time	= models.DateTimeField(auto_now=True)
	category	= models.CharField(max_length=50, default='Sell')
	likes		= models.ManyToManyField(User, related_name='blog_posts')
	attached_image 	= models.ImageField(null=True, blank=True, upload_to='images/')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title + ' | by:' +str(self.author)+ ' | ' +str(self.date_time)

	def get_absolute_url(self):
		return reverse('article_detail', args=(str(self.id)))

class Comment(models.Model):
	post 		=	models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name 		=	models.CharField(max_length=100)
	body		=	models.TextField()
	date_added 	=	models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.post.title + ' | by:' +str(self.name)


class Profile(models.Model):
	user 			= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	Phone 			= models.CharField(max_length=50, null=True, blank=True,)
	bio				= models.TextField()
	profile_pic	 	= models.ImageField(null=True, blank=True, upload_to='images/profile/')

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('home')
