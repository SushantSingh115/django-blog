from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

'''
def home(request):
    posts = Post.objects.all()
    context = {'title': 'Home Page', 'posts': posts}
    return render(request, 'blog/home.html', context)
'''


def about(request):
    context = {'title': 'About'}
    return render(request, 'blog/about.html', context)


class PostList(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post-detail.html'


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog/create-post.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Post
    fields = ['title','content']
    template_name = "blog/post-update.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True