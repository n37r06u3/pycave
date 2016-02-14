from rest_framework import viewsets
from pycave.apps.blog.models import BlogPost
from pycave.apps.blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-created')
    serializer_class = PostSerializer