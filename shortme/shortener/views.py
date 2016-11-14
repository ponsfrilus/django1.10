from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import ShortURL

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        context = {
            "title": "Submit an URL",
            "form": form,
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Submit an URL",
            "form": form,
        }
        template = "shortener/home.html"
        if form.is_valid():
            url = form.cleaned_data.get("url")
            obj, created = ShortURL.objects.get_or_create(url=url)
            context["object"] = obj
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return render(request, template, context)

class ShortView(View):  # Class Based View
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        return HttpResponse("hello again %s -> %s" % (shortcode, obj.url))
