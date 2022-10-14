from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_articles, name="show_articles"),
    path(
        "remove-article/<int:pk>/",
        views.remove_article,
        name="remove_article"
    ),
    path(
        "delete-article/<int:pk>/",
        views.delete_article,
        name="delete_article"
    ),
    path(
        "restore-artile/<int:pk>/",
        views.restore_article,
        name="restore_article"
    ),
    path("restore-all/", views.restore_all, name="restore_all"),
    path("delete-all/", views.delete_all, name="delete_all"),
    path("recycle-bin/", views.recycle_bin, name="recycle_bin"),
]
