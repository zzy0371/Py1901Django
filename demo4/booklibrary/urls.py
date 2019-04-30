from django.conf.urls import url
from . import views
app_name = 'booklibrary'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^readerlogin/$',views.readerlogin,name='readerlogin'),
    url(r'^readerregister/$',views.readerregister,name='readerregister'),
    url(r'^reader/$',views.reader,name='reader'),
    url(r'^readerlogout/$',views.readerlogout,name='readerlogout'),
    url(r'^readerquery/$', views.readerquery, name='readerquery'),
    url(r'^reader/book/(\d+)/$',views.book,name='book'),
    url(r'^reader/info/$',views.readerinfo,name='readerinfo'),
    url(r'^reader/modify/$',views.readermodify,name='readermodify'),
    url(r'^reader/history/$',views.readerhistory,name='readerhistory'),


    url(r'^upload/$', views.upload,name='upload'),

    # 富文本编辑器
    url(r'^edit/$', views.edit,name='edit'),

    url(r'^mail/$',views.mail,name='mail'),

    url(r'^active/(.*?)/$',views.active, name='active'),

    url(r'^ajax/$', views.ajax, name='ajax'),

    url(r'^ajaxajax/$', views.ajaxajax, name='ajaxajax'),

    url(r'^ajaxlogin/$',views.ajaxlogin,name='ajaxlogin'),
    url(r'^checkuser/$',views.checkuser,name='checkuser'),

    url(r'^verifycode/$',views.verifycode,name='verifycode'),

]