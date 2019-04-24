from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from .models import Post,Tag,Category
# Create your views here.

def index(request):
    postlist = Post.objects.all()
    print(postlist)
    return HttpResponse("首页")

def detail(request,id):
    post = get_object_or_404(Post,pk = id)
    print(post)
    return HttpResponse("详情页")

def archives(request,y,m):
    postlist = get_list_or_404(Post, create_time__year = y, create_time__month = m)
    return HttpResponse("首页")

def category(request,id):
    postlist = get_object_or_404(Category,pk=id).post_set.all()
    print(postlist)
    return HttpResponse("首页")

def tag(request,id):
    postlist = get_object_or_404(Tag,pk=id).post_set.all()
    print(postlist)
    return HttpResponse("首页")
