from django.conf.urls import url

from .views import BlogPostDetailView, BlogPostListView

urlpatterns = [
    url('^$', BlogPostListView.as_view(), name='home'),
    # url('^article/(?P<slug>[a-z0-9-]+)/$',
    #     BlogPostDetailView.as_view(), name='blogpost-detail'),
    url('^post/(?P<pk>\d+)/$',
        BlogPostDetailView.as_view(), name='blogpost-detail'),
]
