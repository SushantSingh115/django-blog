from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.PostList.as_view(), name='blog-home'),
    path(r'post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path(r'post/new/', views.CreatePost.as_view(), name='add-post'),
    path(r'post/<int:pk>/update/', views.UpdatePost.as_view(), name= 'update-post'),
    path(r'post/<int:pk>/delete/', views.PostDelete.as_view(), name= 'delete-post'),
    path(r'about/', views.about, name='blog-about'),
]