from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post

class LatestPostFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    describtion = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]
    
    def item_title(self, item):
        return item.title

    def item_describtion(self, item):
        return truncatewords(item.body, 30)
    