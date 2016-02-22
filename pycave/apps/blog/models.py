# coding=utf-8
from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    modified = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('blog.BlogCategory', blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['-created']
        verbose_name = u'文章'

    @models.permalink
    def get_absolute_url(self):
        return ('blog:blogpost-detail', None, {'pk': self.pk})


class BlogCategory(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_category', None, {'slug': self.slug})
