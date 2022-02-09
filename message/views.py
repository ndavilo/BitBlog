from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView
from .models import Message
from .forms import MessageForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from urllib import request

# Create your views here.


def MessageView(request):
	messages 			= Message.objects.all()
	ordering			= ['-sent']
	context = {
		"messages": messages
	}
	return render(request, 'viewmessages.html', context)

class SendMessageView(CreateView):
	model 			= Message
	form_class		= MessageForm
	template_name	= 'sendmessage.html'
	success_url 	= reverse_lazy('message')

class DeleteMessageView(DeleteView):
	model 			= Message
	template_name	= 'delete_message.html'
	success_url 	= reverse_lazy('message')