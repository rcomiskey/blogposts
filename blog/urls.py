from django.conf.urls import url
from .views import getposts, add_post, viewpost, editpost

urlpatterns = [
    url(r'^$', getposts,  name='getposts'),
    url(r'^posts/add$', add_post,  name='addpost'),
    url(r'^posts/(\d+)', viewpost,  name='viewpost'),
    url(r'^posts/edit/(\d+)$', editpost,  name='editpost'),
]
