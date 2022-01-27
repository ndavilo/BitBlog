

from django.urls import path
from .views import HomeView, ADetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, LikeView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('article/<int:pk>', ADetailView.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'update'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name = 'delete'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name = 'add_comment'),

]