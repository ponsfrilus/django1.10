from django.db import models

class ShortURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)  # every time the entry is saved
    timestamp = models.DateTimeField(auto_now_add=True)  # when entry was created

    def __str__(self):
        return str(self.url)
