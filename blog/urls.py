from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.ShowPostView.as_view(), name='blog'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='blog_detail'),
    path('post/<int:pk>/update', views.UpdatePostView.as_view(), name='blog_update'),
    path('post/<int:pk>/delete', views.DeletePostView.as_view(), name='blog_delete'),
    path('post/add/', views.CreatePostView.as_view(), name='blog_add'),
    path('contacts/', views.contacts, name='contacts'),

]
