from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from pycave.apps.blog.models import BlogPost

from django.conf import settings


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    paginate_by = getattr(settings, 'BLOGPOST_PAGINATE_BY', None)

    def get_queryset(self):
        queryset = super(BlogPostListView, self).get_queryset()
        return queryset
