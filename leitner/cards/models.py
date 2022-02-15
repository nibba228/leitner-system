from django.db import models
from django.conf import settings


class Folder(models.Model):
    title = models.CharField(max_length=29)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)


class CardSet(models.Model):
    title = models.CharField(max_length=30)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='card_set')


class Card(models.Model):
    card_set = models.ForeignKey(CardSet, related_name='cards', on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    correct_options = models.JSONField()
    options = models.JSONField()
