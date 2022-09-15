from django.shortcuts import render, get_object_or_404
from .forms import TinyPostForm
from .models import TinyPost, Post


def home_view(request):
    form = TinyPostForm()
    tinyposts = TinyPost.objects.all()
    froalaposts = Post.objects.all()
    return render(request, 'home.html', {'tinyposts':tinyposts, 'froalaposts':froalaposts, 'form':form})

def tpost_detail(request, pk):
    post = get_object_or_404(TinyPost, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

