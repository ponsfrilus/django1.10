from django.db import models

# Create your models here.
from shortener.models import ShortURL

class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, ShortURL):
            obj, created = self.get_or_create(short_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    short_url = models.OneToOneField(ShortURL)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)  # every time the entry is saved
    timestamp = models.DateTimeField(auto_now_add=True)  # when entry was created

    objects = ClickEventManager()

    def __str__(self):
        return "{url} - {count}".format(url=self.short_url, count=self.count)
