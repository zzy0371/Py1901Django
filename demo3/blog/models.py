from django.db import models
# 使用Django自带用户系统
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    """
    文章分类表
        name : 分类命名
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    文章标签表
        name: 标签命名
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    文章表
        title： 标题
        summary： 摘要
        body： 主体
        views： 文章阅读数
        create_time： 文章默认创建时间
        modified_time： 文章最后更改时间
        category： 文章分类，与文章之间为一对多的关系
        tags： 文章标签，与文章之间为多对多关系
        author： 文章作者，使用Django自带用户系统
    """
    title = models.CharField(max_length=20)
    summary = models.CharField(max_length=200,blank=True,null=True)
    body = models.TextField()
    views = models.PositiveIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def increseview(self):
        self.views += 1
        self.save()

