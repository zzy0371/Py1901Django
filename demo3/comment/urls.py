from django.conf.urls import url
from . import views
app_name = 'comment'
urlpatterns = [
    url(r'^commitcomment/(\d+)/$',views.commitcomment,name='commitcomment')
]