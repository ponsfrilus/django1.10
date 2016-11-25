import os
import sys

from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError


EXPECTED_ADMINS = (
    "bancal",
)


class Command(BaseCommand):
    help = "Initialize the ShortMe admins"

    def handle(self, *args, **kwargs):
        now = timezone.now()
        for adm_name in EXPECTED_ADMINS:
            u, created = User.objects.get_or_create(username=adm_name)
            u.is_superuser = True
            u.is_staff = True
            u.is_active = True
            if created:
                u.date_joined = now
            u.save()
            print("Set user '{0}' as admin.".format(adm_name))
