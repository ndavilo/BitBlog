from django import forms
from .models import Post, Category, Comment

choices	=	Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model 	= Post
		fields 	= ('category', 'title', 'author', 'body', 'attached_image')

		widgets 	= {
			'category'		:	forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'title'			:	forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TYPE OF COIN AND VALUE'}),
			'author'		:	forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'userid', 'type':'hidden'}),
			'body'			:	forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'SELL OR BUY 0.1 BITCOIN'}),

		} 

class EditForm(forms.ModelForm):
	class Meta:
		model 	= Post
		fields 	= ('category', 'title', 'body')

		widgets 	= {
			'category'		:	forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'title'			:	forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SELL OR BUY COIN'}),
			'body'			:	forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'SELL OR BUY 0.1 BITCOIN'}),

		} 

class AddCommentForm(forms.ModelForm):
	class Meta:
		model 		=	Comment
		fields 		=	('body','name')
		widgets 	=	{
				'body'			:	forms.Textarea(attrs={'class': 'form-control'}),
				'name'			:	forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'userid', 'type':'hidden'}),
		}

class EditCommentForm(forms.ModelForm):
	class Meta:
		model 		=	Comment
		fields 		=	('body',)
		widgets 	=	{
				'body'			:	forms.Textarea(attrs={'class': 'form-control'})
		}

		