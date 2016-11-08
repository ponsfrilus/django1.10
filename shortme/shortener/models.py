from django.db import models

from .utils import create_short_url

class ShortURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  # every time the entry is saved
    timestamp = models.DateTimeField(auto_now_add=True)  # when entry was created

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_short_url(self)
        super(ShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
