from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.BlogCategory', blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.title


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
