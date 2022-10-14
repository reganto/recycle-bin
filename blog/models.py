from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomManager

# Create your models here.


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating created and modified fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Article(TimeStampedModel):
    title = models.CharField(
        max_length=1025,
        unique=True,
        verbose_name=_("Title"),
        help_text=_("Title of the article"),
    )
    body = models.TextField(
        verbose_name=_("Body"),
        help_text=_("Body of the article")
    )
    deleted = models.DateTimeField(editable=False, null=True)

    objects = CustomManager()

    def soft_delete(self):
        self.deleted = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title}"
