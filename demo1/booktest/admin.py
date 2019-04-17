from django.contrib import admin
from .models import BookInfo,HeroInfo

class HeroInfoInlines(admin.StackedInline):
    model = HeroInfo
    extra = 1


# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle']
    # 将书和主角绑定添加
    inlines = [HeroInfoInlines,]



admin.site.register(BookInfo,BookInfoAdmin)


class HeroInfoAdmin(admin.ModelAdmin):
    # 后台显示控制
    # 显示对象指定列 列名一致
    list_display = ['name', 'sex', 'skill']
    # 显示过滤规则 列名一致
    list_filter = ['hname','hgender']
    # 显示搜索字段 支持模糊查询
    search_fields = ['hname', 'hcontent']
    # 分页 每页显示个数
    list_per_page = 3

# 注册模型类
admin.site.register(HeroInfo,HeroInfoAdmin)

"""
通过少量代码实现强大的后台管理
需要将特定的数据模型注册 才能在后台管理
"""


"""
list_display=[]
list_filter = []
search_fileds = []
list_per_page = 10
inlines = HeroInfoInlines:StackedInline


"""