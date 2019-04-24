from django import template
from ..models import Post,Category,Tag
# 得到Django负责管理标签和过滤器的类
register = template.Library()

@register.simple_tag
def getlatestposts(num=3):
    """
    获取最新文章，默认显示3篇
    :param num:
    :return:
    """
    return Post.objects.all().order_by("-create_time")[:num]

@register.simple_tag
def getdatelist(num = 3):
    """
    返回最近月份
    :param num:
    :return:
    """
    return Post.objects.dates("create_time","month",order="DESC")[:num]

@register.simple_tag
def getcategorys():
    """
    返回分类
    :return:
    """
    return Category.objects.all()

@register.simple_tag
def gettags():
    """
    返回标签云
    :return:
    """
    return Tag.objects.all()

