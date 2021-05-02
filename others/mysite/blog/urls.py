from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from . templates.blog.sitemaps import PostSitemap
from . templates.blog.feeds import LatestPostFeed 


sitemaps = {
    'posts': PostSitemap
}


app_name = 'blog'
urlpatterns = [
    # post views
    #path('', views.post_list, name = 'post_list'),
    #path('', views.PostListView.as_view(), name = 'post_list'),
    path('', views.post_list, name = 'post_list' ),
    path('tag/<slug:tag_slug>/', views.post_list, name = 'post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    views.post_detail,
    name = 'post_detail'),
    path('<int:post_id>/share/', views.post_share, name = 'post_share'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    name = 'django.contrib.sitemaps.views.sitemap'),
    path('feed/', LatestPostFeed(), name = 'post_feed'),
    path('search/', views.post_search, name = 'post_search'),
]
