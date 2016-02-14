from rest_framework import serializers

from pycave.apps.blog.models import BlogPost


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost


