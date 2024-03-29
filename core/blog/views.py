from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post, Category
from .forms import PostForm, UpdatePostForm, CategoryForm
from django.http import HttpResponseRedirect


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-publicated"]

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        categories = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context["categories"] = categories
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        post = Post.objects.get(id=self.kwargs["pk"])
        total_likes = post.count_likes()

        context = super().get_context_data(**kwargs)
        context["total_likes"] = total_likes
        context["liked"] = False
        if post.likes.filter(id=self.request.user.id):
            context["liked"] = True

        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "edit_post.html"
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "add_category.html"
    success_url = reverse_lazy("home")


# def CategoryView(request, pk):
#     category_posts = Post.objects.filter(category=pk)
#     return render(request, 'category.html', {'category': pk, 'category_posts': category_posts})


class CategoryDetailView(ListView):
    model = Post
    template_name = "category_details.html"
    context_object_name = "category_posts"

    def get_queryset(self):
        category_id = self.kwargs["pk"].replace("-", " ")
        queryset = Post.objects.filter(category=category_id)
        return queryset


class CategoryView(ListView):
    model = Category
    template_name = "category.html"


def LikeView(request, pk):
    post = Post.objects.get(id=pk)
    if post.likes.filter(id=request.user.id):
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(
        reverse(
            "article_detail",
            args=[
                str(pk),
            ],
        )
    )
