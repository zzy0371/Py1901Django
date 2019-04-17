from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
# Create your views here.

# 定义视图函数
def index(request):
    print("请求",request)
    return HttpResponse("首页")


def list(request):
    return HttpResponse("列表页")


def detail(request,id):
    try:
        book = BookInfo.objects.get(pk=int(id))
        return HttpResponse(book)
    except:
        return HttpResponse("请输入正确id")
"""
视图函数
将函数和路绑定
"""
