from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(auto_now_add=True)

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=50)
    # 外键 第一个参数为表名 第二个参数代表删除类型
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)



"""
 django MVT  M
 ORM 对象中O 
 需要定义实体类 
 
 
 定义模型：继承models.Model
 配置数据库：默认sqlite
 将应用名添加到应用列表 installed_apps
 
 
 python manage.py makemigrations 生成迁移文件
 python manage.py migrate 执行迁移
 
 
"""
