from django.conf import settings
from django_hosts import patterns, host

DEFAULT_HOST = getattr(settings, "DEFAULT_HOST", "www")

host_patterns = patterns('',
    host(DEFAULT_HOST, settings.ROOT_URLCONF, name=DEFAULT_HOST),
    host(r'(?!{}).*'.format(DEFAULT_HOST), 'shortme.hostsconf.urls', name='wildcard'),
)

''' probably future notation (to match Django's evolution)
from shortme.hostsconf import urls as redirect_urls
host_patterns = [
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', redirect_urls, name='wildcard'),
]
'''
