from django.db import models


class SoftDeleteQuerySet(models.QuerySet):
    def active_items(self):
        return self.filter(deleted__isnull=True)

    def inactive_items(self):
        return self.filter(deleted__isnull=False)


class CustomManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db)


CustomManager = CustomManager.from_queryset(SoftDeleteQuerySet)
