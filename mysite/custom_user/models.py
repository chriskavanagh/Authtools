from __future__ import unicode_literals
from embed_video.fields import EmbedVideoField
from django.db import models

# Create your models here.
class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()