from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='blog'),
    path('post/<int:pk>/', views.ShowNewsDetailView.as_view(), name='blog_post'),
    path('contacts/', views.contacts, name='contacts'),
]
