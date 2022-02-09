from django.urls import path
from . import views
from .views import MessageView, SendMessageView, DeleteMessageView


urlpatterns = [
    path('message/', MessageView, name = 'message'),
    path('send_message/', SendMessageView.as_view(), name = 'send_message'),
    path('message/<int:pk>/delete', DeleteMessageView.as_view(), name = 'deleteM'),

]