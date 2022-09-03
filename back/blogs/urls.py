from django.urls import path

from .views import BlogViewSet, BlogPostViewSet


blog_list = BlogViewSet.as_view({"post": "create_blog"})
blog_detail = BlogViewSet.as_view(
    {
        "get": "retrieve_blog",
        "patch": "update_blog",
    }
)

blog_post_list = BlogPostViewSet.as_view(
    {
        "get": "list_post",
        "post": "create_post",
    }
)
blog_post_detail = BlogPostViewSet.as_view(
    {
        "get": "retrieve_post",
        "patch": "update_post",
        "delete": "destroy_post",
    }
)

urlpatterns = [
    path("blog/", blog_list, name="blog list"),
    path("blog/<str:name>/", blog_detail, name="blog detail"),
    path(
        "blog/<str:name>/post",
        blog_post_list,
        name="blog post list",
    ),
    path(
        "blog/<str:name>/post/<int:post_id>/",
        blog_post_detail,
        name="blog post detail",
    ),
]
