from django.forms import ModelForm
from .models import Comment
class CommentForm(ModelForm):
    """
    评论模型对应的表单类
    """
    class Meta():
        model = Comment
        fields = ['name','email','url','text']