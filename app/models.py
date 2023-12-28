from typing import Any
from django.db import models
import os
from django.conf import settings
from easy_thumbnails.fields import ThumbnailerImageField


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    file = models.FileField(upload_to='books')



    photo = ThumbnailerImageField(upload_to='photo')
    cover = models.ImageField(upload_to='book_covers')

    def __str__(self):
        return self.title
