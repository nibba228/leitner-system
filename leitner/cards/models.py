from django.db import models
from django.conf import settings


class Folder(models.Model):
    """Папка с карточками"""

    title = models.CharField(max_length=29)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Card(models.Model):
    """Карточка"""

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    correct_options = models.JSONField()
    options = models.JSONField()
