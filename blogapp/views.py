from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post
from . forms import CommentForm


# Create your views here.
@login_required(login_url='login')
def home(request):
    all_post = Post.newmanager.all()
    return render(request, 'index.html', {'posts': all_post})

@login_required(login_url='login')
def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'single.html', {'post': post})


