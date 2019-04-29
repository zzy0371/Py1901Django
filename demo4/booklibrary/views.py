from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse
from .models import StudentUser,Book,History,HotPic,MessageInfo
from django.db.models import Q
from datetime import datetime,timedelta
from django.core.mail import send_mail,send_mass_mail
from django.conf import settings
# Create your views here.
def index(request):

    messageinfos = MessageInfo.objects.all()
    return render(request,'booklibrary/index.html',{"messageinfos":messageinfos})

def readerlogin(request):
    if request.method == "GET":
        return render(request,'booklibrary/reader_login.html')
    else:
        error = None
        un = request.POST.get("username")
        pwd = request.POST.get("password")
        try:
            user = StudentUser.objects.get(username = un)
            if user.check_password(pwd):
                request.session["username"] = un
                return redirect(reverse('booklibrary:reader'))
            else:
                error = "密码不正确"
        except:
            error = "用户名不存在"

        return render(request, 'booklibrary/reader_login.html', {"error":error})

def readerregister(request):
    if request.method == "GET":
        return render(request,'booklibrary/reader_register.html')
    else:
        try:
            un = request.POST.get("username")
            pwd = request.POST.get("password")
            email = request.POST.get("email")
            StudentUser.objects.create_user(un, password=pwd, is_active = False)
            id = StudentUser.objects.get(username = un).id

            # TODO 需要进行序列化加密
            send_mail("点击激活账户", " <a href = 'http://127.0.0.1:8000/booklibrary/active/%s'> 点击我激活账户</a> "%(id,),settings.DEFAULT_FROM_EMAIL,[email])

        except Exception as e:
            return render(request, 'booklibrary/reader_register.html', {"error":e})

        return redirect(reverse('booklibrary:readerlogin'))

def reader(request):
    username = request.session.get("username")
    return render(request,'booklibrary/reader.html',{"username":username})




def readerlogout(request):
    request.session.flush()
    return redirect(reverse('booklibrary:readerlogin'))

def readerquery(request):
    if request.method == "GET":
        return render(request,'booklibrary/reader_query.html')
    else:
        error = None
        item = request.POST.get("item")
        query = request.POST.get("query")
        books = None
        if query:
            if item == "author":
                books = Book.objects.filter(author = query)
            else:
                books = Book.objects.filter(name=query)
        else:
            error = "请输入查询内容"

        return render(request, 'booklibrary/reader_query.html',{"books":books,"error":error})

def book(request,id):
    book = get_object_or_404(Book, pk=id)
    reader = History.objects.filter(book_id=id).filter(status =0) .first()
    error = None
    if request.method == "POST":
        if reader:
            error = 'The book has already borrowed.'
        else:
            history = History()
            history.book = book
            history.studentuser = StudentUser.objects.get(username = request.session.get("username"))
            history.date_borrow = datetime.now()
            history.date_return = datetime.now()+timedelta(days=30)
            history.status = False
            history.save()
            return redirect(reverse('booklibrary:book',args=(id,)))

    return render(request, 'booklibrary/reader_book.html', {"book": book, "reader": reader, "error":error})

def readerinfo(request):
    user = get_object_or_404(StudentUser, username = request.session.get("username"))
    return render(request,'booklibrary/reader_info.html',{"user":user})

def readermodify(request):
    error = None
    if request.method == 'POST':
        if not request.POST['username']:
            error = 'You have to input your name'
        else:
            user = StudentUser.objects.get(username = request.session.get("username"))
            user.username = request.POST['username']
            college = request.POST['college']
            user.college = college
            num = request.POST['number']
            if num:
                user.num = num
            email = request.POST['email']
            if email:
                user.email = email
            pwd = request.POST['password']
            if pwd:
                user.set_password(pwd)
            user.save()
            request.session['username'] = user.username
            return redirect(reverse('booklibrary:readerinfo'))
    return render(request,'booklibrary/reader_modify.html',{"error":error})

def readerhistory(request):
    user = get_object_or_404(StudentUser, username = request.session.get("username"))
    histroys = History.objects.filter(studentuser_id = user.id)
    return render(request,'booklibrary/reader_histroy.html',{"histroys":histroys})


def upload(request):
    """
    上传图片
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request,'booklibrary/reader_upload.html')
    elif request.method == "POST":
        # 文件数据需要使用FILES 获取  enctype = "multipart/form-data"
        hp = HotPic(index = request.POST["index"], pic = request.FILES["pic"])
        hp.save()
        return redirect(reverse('booklibrary:index'))

def edit(request):
    """
    富文本编辑
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request,'booklibrary/edit.html')
    elif request.method == "POST":
        title = request.POST["title"]
        message = request.POST["message"]
        msg = MessageInfo(title=title,message =message)
        msg.save()
        return redirect(reverse('booklibrary:index'))

def mail(request):
    """发送邮件"""

    try:
        send_mail("Django发送邮件", "Django自带邮件功能，<a src = 'http://127.0.0.1:8000/booklibrary/'> 百度</a> 你可以使用sendmail 或者sendmassmail 发送",
                  settings.DEFAULT_FROM_EMAIL, ["496575233@qq.com", "zhangzhaoyu@qikux.com"]
                  )
        # send_mass_mail((("Django发送邮件1", "Django自带邮件功能，你可以使用sendmail 或者sendmassmail 发送",
        #           settings.DEFAULT_FROM_EMAIL, ["496575233@qq.com", "zhangzhaoyu@qikux.com"]
        #           ),("Django发送邮件2", "Django自带邮件功能，你可以使用sendmail 或者sendmassmail 发送",
        #           settings.DEFAULT_FROM_EMAIL, ["496575233@qq.com", "zhangzhaoyu@qikux.com"]
        #           ),("Django发送邮件3", "Django自带邮件功能，你可以使用sendmail 或者sendmassmail 发送",
        #           settings.DEFAULT_FROM_EMAIL, ["496575233@qq.com", "zhangzhaoyu@qikux.com"]
        #           )))
    except:
        return HttpResponse("发送失败")

    return HttpResponse("发送成功")

def active(request,id):
    """
    用户激活用户 id为用户id
    :param request:
    :param id:
    :return:
    """
    user = StudentUser.objects.get(pk = id)
    user.is_active = True
    user.save()
    return redirect(reverse('booklibrary:readerlogin'))


