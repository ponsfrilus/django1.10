from django.core.management.base import BaseCommand, CommandError
from shortener.models import ShortURL

class Command(BaseCommand):
    help = "Dump all URL -> shortcode"

    # def add_arguments(self, parser):
    #     parser.add_argument("arg_name", nargs="+", type=int)

    def handle(self, *args, **kwargs):
        for u in ShortURL.objects.all():
            print("%s -> %s" % (u.shortcode, u.url))
