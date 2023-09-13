from django.urls import path, include
from .views import (
    HomeView,
    ArticleDetailView,
    AddPostView,
    UpdatePostView,
    DeletePostView,
    AddCategoryView,
    CategoryView,
    CategoryDetailView,
    LikeView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article_detail"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name="update_post"),
    path("article/delete/<int:pk>", DeletePostView.as_view(), name="delete"),
    path("add_category/", AddCategoryView.as_view(), name="add_category"),
    path("category/<str:pk>", CategoryDetailView.as_view(), name="category_detail"),
    path("category/", CategoryView.as_view(), name="category"),
    path("like_post/<int:pk>", LikeView, name="like_post"),
]
