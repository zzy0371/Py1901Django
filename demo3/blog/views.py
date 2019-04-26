from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from .models import Post,Tag,Category
from comment.forms import CommentForm
import markdown
from django.core.paginator import Paginator
# Create your views here.

def getpage(request,objectlist):
    # 分页器
    paginator = Paginator(objectlist,2)
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum
    page = paginator.page(pagenum)
    return page

def index(request):
    postlist = Post.objects.all()
    page = getpage(request,postlist)
    context = {
        # "postlist":postlist,
        "page":page,
    }
    return render(request,'blog/index.html',context)

def detail(request,id):
    post = get_object_or_404(Post,pk = id)
    post.increseview()

    # 第一种直接利用markdown生成html
    # post.body = markdown.markdown(post.body, extensions = [
    #     #     'markdown.extensions.extra',
    #     #     'markdown.extensions.codehilite',
    #     #     'markdown.extensions.toc'
    #     # ])

    md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc

    context = {
        "post":post,
        "form": CommentForm()
    }
    return render(request,'blog/single.html',context)

def archives(request,y,m):
    postlist = get_list_or_404(Post, create_time__year = y, create_time__month = m)
    page = getpage(request,postlist)
    context = {
        # "postlist":postlist,
        "page":page,
    }
    return render(request,'blog/index.html',context)

def category(request,id):
    postlist = get_object_or_404(Category,pk=id).post_set.all()
    page = getpage(request,postlist)
    context = {
        # "postlist":postlist,
        "page":page,
    }
    return render(request,'blog/index.html',context)

def tag(request,id):
    postlist = get_object_or_404(Tag,pk=id).post_set.all()
    page = getpage(request,postlist)
    context = {
        # "postlist":postlist,
        "page":page,
    }
    return render(request,'blog/index.html',context)


