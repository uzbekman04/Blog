from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


# Create your views here.
class HomeView(generic.ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'


class DetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail_post.html'
    context_object_name = 'post'


class NewPostView(generic.CreateView):
    model = Post
    template_name = 'posts/new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')


class EditPostView(generic.UpdateView):
    model = Post
    template_name = 'posts/edit_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('home')
