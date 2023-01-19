from django.urls import path
from server.apps.posts.views import posts_list,  posts_retrieve, posts_create, posts_delete, posts_update

urlpatterns = [
    path("", posts_list ),
    path("posts/<int:pk>", posts_retrieve),
    path("posts/create", posts_create),
    path("posts/<int:pk>/delete", posts_delete),
    path("posts/<int:pk>/update", posts_update)
]