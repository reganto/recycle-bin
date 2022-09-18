from django.utils import timezone
from celery import shared_task

from .models import Article


def days_after(deleted_date):
    """
    Calculate days passed from a record soft delete.
    """
    return (timezone.now() - deleted_date).seconds // 60 // 60 // 24


@shared_task()
def recycle_bin_find_and_delete_articles_monthly():
    inactive_articles = Article.objects.inactive_items()
    for article in inactive_articles:
        if days_after(article.deleted) >= 30:
            article.delete()
