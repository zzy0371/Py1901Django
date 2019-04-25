from django.db import models
# Create your models here.
from blog.models import Post
class Comment(models.Model):
    """
    评论模型
    name 评论用户名
    email 用户邮件
    url 用户个人主页
    text 评论内容
    create_time 评论时间
    post 文章
    """
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)
    url = models.URLField(blank=True,null=True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)