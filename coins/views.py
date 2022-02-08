from django.shortcuts import render
from .models import Cryptocoin

# Create your views here.

def ChartView(request):
	coins 			= Cryptocoin.objects.all()
	context = {
		"coins": coins
	}
	return render(request, 'blog/chart_list.html', context)