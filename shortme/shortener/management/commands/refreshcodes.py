from django.core.management.base import BaseCommand, CommandError
from shortener.models import ShortURL

class Command(BaseCommand):
    help = "Regenerates all shortcode"

    # def add_arguments(self, parser):
    #     parser.add_argument("arg_name", nargs="+", type=int)

    def handle(self, *args, **kwargs):
        return ShortURL.objects.regenerate_all_shortcodes()
