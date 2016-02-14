from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from pycave.apps.blog.models import BlogPost, BlogCategory


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogPost
        exclude = ['created']


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(BlogPost, PostAdmin)
admin.site.register(BlogCategory, CategoryAdmin)
