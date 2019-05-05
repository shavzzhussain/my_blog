from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/new', views.PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail_post'),
    path('post/<int:pk>/edit', views.PostupdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete_post'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete_post'),
]
