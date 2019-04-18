from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import BookInfo,HeroInfo
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
        # 使用render没有刷新请求url
        # return render(request, 'booktest/list.html', {"booklist": bl})
        # 重新向服务器发起请求 刷新url
        return HttpResponseRedirect('/booktest/list/',{"booklist": bl})
    except:
        return HttpResponse("删除失败")


def addhero(request, bookid):
    return render(request, 'booktest/addhero.html', {"bookid":bookid})

def addherohandler(request):
    bookid = request.POST["bookid"]
    hname = request.POST["heroname"]
    hgender = request.POST["sex"]
    hcontent = request.POST["herocontent"]
    # print(bookid,hname,hgender,hcontent)

    book = BookInfo.objects.get(pk=bookid)
    hero = HeroInfo()
    hero.hname = hname
    hero.hgender = True
    hero.hcontent = hcontent
    hero.hbook = book
    hero.save()
    return HttpResponseRedirect('/booktest/detail/'+str(bookid)+'/',{"book":book})
    # return HttpResponse("添加成功")
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