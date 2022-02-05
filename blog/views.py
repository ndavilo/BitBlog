from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, AddCommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from coins.models import Chart

class HomeView(ListView):
	model 			= Post
	template_name 	= 'home.html'
	ordering		= ['-date_time']

	def get_context_data(self, *args, **kwargs):
		cat_menu			= Category.objects.all()
		context 			= super(HomeView, self).get_context_data(*args, **kwargs)
		charts 				= Chart.objects.all()
		context["charts"]	= charts
		context["cat_menu"]	= cat_menu
		return context


class ADetailView(DetailView):
	model 			= Post
	template_name 	= 'details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu				= Category.objects.all()
		context 				= super(ADetailView, self).get_context_data(*args, **kwargs)
		stuff 					= get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes				= stuff.total_likes()

		liked					= False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked				= True

		context["cat_menu"]		= cat_menu
		context["total_likes"]	= total_likes
		context["liked"]		= liked
		return context


class AddPostView(CreateView):
	model 			= Post
	form_class		= PostForm
	template_name	= 'add_post.html'
	success_url 	= reverse_lazy('home')

class AddCommentView(CreateView):
	model 			= Comment
	form_class		= AddCommentForm
	template_name	= 'add_comment.html'
	success_url 	= reverse_lazy('home')

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

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

def LikeView(request, pk):
	post 			= get_object_or_404(Post, id = request.POST.get('post_id'))
	liked			= False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked			= False

	else:
		post.likes.add(request.user)
		liked		= True

	return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))



