from django.conf.urls import url
from .views import index, view_post, add_post, edit_post, delete_post, delete_comment

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^view_post/(?P<post_id>\d+)$', view_post, name='view-post'),
    url(r'^add_post$', add_post, name='add-post'),
    url(r'^edit_post/(?P<post_id>\d+)$', edit_post, name='edit-post'),
    url(r'^delete_post/(?P<post_id>\d+)$', delete_post, name='delete-post'),
    url(r'^delete_comment/(?P<comment_id>\d+)$', delete_comment, name='delete-comment'),
]
