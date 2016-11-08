from django.db import models

from .utils import create_short_url

class ShortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(ShortURLManager, self).all(*args, **kwargs)
        return qs.filter(active=True)

    def regenerate_all_shortcodes(self):
        qs = ShortURL.objects.filter(id__gte=1)
        for q in qs:
            q.shortcode = create_short_url(q)
            q.save()

class ShortURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  # every time the entry is saved
    timestamp = models.DateTimeField(auto_now_add=True)  # when entry was created
    active = models.BooleanField(default=True)

    # Overwrite ShortURL.objects !
    objects = ShortURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_short_url(self)
        super(ShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)