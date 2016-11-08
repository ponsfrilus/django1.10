from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import ShortURL

# Create your views here.
def short_redirect_view(request, shortcode=None, *args, **kwargs):  # Function Based View
    obj = get_object_or_404(ShortURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)

class ShortCBView(View):  # Class Based View
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        return HttpResponse("hello again %s -> %s" % (shortcode, obj.url))
