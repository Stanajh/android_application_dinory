from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey
from django.apps import apps

class Diary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    child = models.ForeignKey('Accounts.Child', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    img = models.CharField(max_length=255)
    year = models.IntegerField()
    month = models.IntegerField()
    date = models.IntegerField()


class Sentence(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    child = models.ForeignKey('Accounts.Child', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)


class Word(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    child = models.ForeignKey('Accounts.Child', on_delete=models.CASCADE)
    content = models.CharField(max_length=20)
    part = models.CharField(max_length=10)
    mean = models.CharField(max_length=50)


class WordToSentence(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    child = models.ForeignKey('Accounts.Child', on_delete=models.CASCADE)
    sentence = models.ForeignKey("Sentence", on_delete=models.CASCADE)
    word = models.ForeignKey("Word", on_delete=models.CASCADE)