from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.


class BlogHome(ListView):
    model = BlogPost
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


class BlogPostDelete(DeleteView):
    model = BlogPost
    template_name = 'posts/blogpost_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts:home')


@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'content']


class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title', 'content', 'published']


class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = 'posts/blogpost_detail.html'
    context_object_name = 'post'
