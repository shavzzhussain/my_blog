from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/new', views.AboutView.as_view(), name='about'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('about/', views.AboutView.as_view(), name='about'),
]
