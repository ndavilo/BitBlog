from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
	model 			= Post
	template_name 	= 'home.html'
	ordering		= ['-date_time']

	def get_context_data(self, *args, **kwargs):
		cat_menu			= Category.objects.all()
		context 			= super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"]	= cat_menu
		return context


class ADetailView(DetailView):
	model 			= Post
	template_name 	= 'details.html'


class AddPostView(CreateView):
	model 			= Post
	form_class		= PostForm
	template_name	= 'add_post.html'
	success_url 	= reverse_lazy('home')
	
class UpdatePostView(UpdateView):
	model 			= Post
	template_name	= 'add_post.html'
	form_class		= EditForm
	success_url 	= reverse_lazy('home')

class DeletePostView(DeleteView):
	model 			= Post
	template_name	= 'delete_post.html'
	success_url 	= reverse_lazy('home')

def CategoryView(request, cats):
	category_posts	= Post.objects.filter(category=cats.replace('-', ' '))
	return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})
