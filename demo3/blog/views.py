from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from .models import Post,Tag,Category
from comment.forms import CommentForm
# Create your views here.

def index(request):
    postlist = Post.objects.all()
    context = {
        "postlist":postlist,
    }
    return render(request,'blog/index.html',context)

def detail(request,id):
    post = get_object_or_404(Post,pk = id)
    context = {
        "post":post,
        "form": CommentForm()
    }
    return render(request,'blog/single.html',context)

def archives(request,y,m):
    postlist = get_list_or_404(Post, create_time__year = y, create_time__month = m)
    context = {
        "postlist":postlist,
    }
    return render(request,'blog/index.html',context)

def category(request,id):
    postlist = get_object_or_404(Category,pk=id).post_set.all()
    context = {
        "postlist":postlist,
    }
    return render(request,'blog/index.html',context)

def tag(request,id):
    postlist = get_object_or_404(Tag,pk=id).post_set.all()
    context = {
        "postlist":postlist,
    }
    return render(request,'blog/index.html',context)
