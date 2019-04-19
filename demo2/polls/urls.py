from django.conf.urls import url
from . import views
app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^vote/$',views.vote, name='vote')
]