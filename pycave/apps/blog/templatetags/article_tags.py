from django import template

from ..models import BlogPost

register = template.Library()


@register.assignment_tag
def recent_articles(limit=10, exclude=None):
    """Returns list of latest article"""
    queryset = BlogPost.objects.order_by('-created')[:limit]
    if exclude:
        if hasattr(exclude, '__iter__'):
            queryset = queryset.exclude(pk__in=exclude)
        else:
            queryset = queryset.exclude(pk=exclude)
    return queryset
