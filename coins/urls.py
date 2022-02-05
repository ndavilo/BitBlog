from django.urls import path
from . import views
from .views import ChartView


urlpatterns = [
    path('charts/', ChartView, name = 'charts'),

]