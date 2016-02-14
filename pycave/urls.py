"""pycave URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

from pycave.apps.blog import urls as blog_urls
from rest_framework import routers

from pycave.apps.blog.apis import PostViewSet
from pycave.views import home, project,about,contact,service
from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()
router.register(r'blog/post', PostViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^page/project$', project, name='project'),
    url(r'^page/about', about, name='about'),
    url(r'^page/contact', contact, name='contact'),
    url(r'^page/service', service, name='service'),
    url(r'^blog/', include(blog_urls, namespace='blog')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
