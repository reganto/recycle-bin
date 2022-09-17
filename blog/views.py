from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Article

# Create your views here.


def show_articles(request: HttpRequest) -> HttpResponse:
    active_articles = Article.objects.active_items()
    return render(request, "blog/articles.html", {"articles": active_articles})


def recycle_bin(request: HttpRequest) -> HttpResponse:
    inactive_articles = Article.objects.inactive_items()
    return render(request, "blog/recycle_bin.html", {"articles": inactive_articles})


def remove_article(request: HttpRequest, pk) -> HttpResponse:
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect(reverse("blog:show_articles"))


def restore_article(request: HttpRequest, pk) -> HttpResponse:
    article = Article.objects.get(pk=pk)
    article.deleted = None
    article.save()
    return redirect(reverse("blog:recycle_bin"))
