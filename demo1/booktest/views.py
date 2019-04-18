from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
from django.template import loader
# Create your views here.

# 定义视图函数
def index(request):
    # return HttpResponse("首页")

    # 加载模板
    # indextem = loader.get_template('booktest/index.html')
    # cont = {"username":"zzy"}
    # # 使用变量参数渲染模板
    # result = indextem.render(cont)
    # # 返回模板
    # return HttpResponse(result)

    return render(request,'booktest/index.html',{"username":'zzy'})


def list(request):
    # return HttpResponse("列表页")
    bl = BookInfo.objects.all()
    return render(request,'booktest/list.html',{"booklist":bl})


def detail(request,id):
    book = BookInfo.objects.get(pk=id)
    return render(request,'booktest/detail.html',{"book":book})


def delete(request,id):
    try:
        BookInfo.objects.get(pk=id).delete()
        bl = BookInfo.objects.all()
        return render(request, 'booktest/list.html', {"booklist": bl})
    except:
        return HttpResponse("删除失败")
"""
视图函数
将函数和路绑定
"""


"""
创建模板文件夹 templates 
配置模板目录  os.path.join(BASEDIR,'templates')
创建项目模板目录，创建模板 

加载模板  temp=loader.get_template()
使用变量渲染模板  result=temp.render({})
返回  HttpResponse(result)



"""