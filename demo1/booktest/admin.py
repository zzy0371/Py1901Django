from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.
admin.site.register(BookInfo)
admin.site.register(HeroInfo)

"""
通过少量代码实现强大的后台管理
需要将特定的数据模型注册 才能在后台管理
"""