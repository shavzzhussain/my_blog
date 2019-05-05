from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
path('', views.PostListView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/new', views.PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail_post'),
    path('post/<int:pk>/edit', views.PostupdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete_post'),
    path('draft/', views.PostDraftView.as_view(), name='draft_post'),
    path('post/<int:pk>/publish', views.post_publish, name='publish_post'),
    path('post/<int:pk>/comment', views.add_comment_to_post, name='comment_post'),
    path('post/<int:pk>/remove', views.comment_remove, name='remove_post'),
    path('post/<int:pk>/approve', views.comment_approve, name='approve_post'),
]
