from django.conf.urls import url
from .views import getposts, add_post, viewpost, editpost

urlpatterns = [
    url(r'^$', getposts,  name='getposts'),
    url(r'^add$', add_post,  name='add post'),
    url(r'^posts/(\d+)', viewpost,  name='viewpost'),
    url(r'^edit/(\d+)$', editpost,  name='editpost'),
]
