from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "header_image", "author", "category", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control "}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(
                attrs={
                    "type": "hidden",
                    "id": "author_form",
                    "value": "",
                    "placeholder": "",
                }
            ),
            "category": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "title_tag", "category", "body"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
