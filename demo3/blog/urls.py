from django.conf.urls import url
from . import views
from .feed import PostFeed
app_name = "blog"
urlpatterns = [
    # 进入首页显示
    url(r'^$', views.index, name='index'),
    # 进入文章详情页，需要传入文章id
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    # 点击归档项目，需要传入年份，月份，跳转到首页
    url(r'archives/(\d+)/(\d+)/', views.archives, name='archives'),
    # 点击分类项目，需要传入分类id，跳转到首页
    url(r'category/(\d+)/', views.category, name='category'),
    # 点击标签项目，需要传入标签id，跳转到首页
    url(r'tag/(\d+)/', views.tag, name='tag'),
    url(r'^rss/$', PostFeed(),name='rss'),

]
