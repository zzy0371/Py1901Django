from haystack import indexes
from .models import Post
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    """
    索引类名
    """
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return Post
    def index_queryset(self, using=None):
        return self.get_model().objects.all()