from django.shortcuts import render
from .models import Chart

# Create your views here.

def ChartView(request):
	charts 			= Chart.objects.all()
	context = {
		"charts": charts
	}
	return render(request, 'blog/chart_list.html', context)