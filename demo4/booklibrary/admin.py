from django.contrib import admin
from .models import StudentUser,Book,History,HotPic,MessageInfo
# Register your models here.
admin.site.register(StudentUser)
admin.site.register(Book)
admin.site.register(History)
admin.site.register(HotPic)
admin.site.register(MessageInfo)

