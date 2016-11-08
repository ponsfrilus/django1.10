from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def short_redirect_view(request, *args, **kwargs):  # Function Based View
    return HttpResponse("hello")

class ShortCBView(View):  # Class Based View
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello again")
