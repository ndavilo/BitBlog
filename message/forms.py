from django import forms
from .models import Message
from django.contrib.auth.models import User

my_user = User.objects.all().values_list('username', 'username')
choice_list = []

for item in my_user:
	choice_list.append(item)

class MessageForm(forms.ModelForm):
	class Meta:
		model 	= Message
		fields 	= ('recipient', 'sender', 'body')

		widgets 	= {
			'recipient'		:	forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'sender'		:	forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'userid', 'type':'hidden'}),
			'body'			:	forms.Textarea(attrs={'class': 'form-control'}),

		} 
