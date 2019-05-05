from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,Comment
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from blog.forms import PostForm,PostComment
from django.views.generic import (TemplateView,ListView,CreateView,DeleteView,DetailView,UpdateView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
################################################## All Class based view ###############

class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostListView(ListView):
    model = Post
    #to get the post in descending order which are stored in database
    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostupdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class PostDraftView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('date')

#########################################
# function based view for comment adding ###
##########################################
@login_required
def post_publish(request):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return  redirect('detail_post',pk=pk)


@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostComment()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail_post',{'form':form})
    else:
        form = PostComment()
        return render('blog/post_detail.html',{'form': form})


@login_required()
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('detail_post', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('detail_post', pk=post_pk)

