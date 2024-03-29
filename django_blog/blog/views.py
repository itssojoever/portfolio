from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, "blog/home.html",  context)

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]

class PostDetailView(DetailView):
    model = Post

def gallery(request):
    return render (request, "blog/gallery.html")