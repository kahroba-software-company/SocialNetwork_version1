from django.apps import AppConfig
from tweets.models import Tweet
from django.contrib import admin

admin.site.register(Tweet)

class TweetsConfig(AppConfig):
    name = 'tweets'

