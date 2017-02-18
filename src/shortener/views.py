from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import KirrURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shortener/home.html', {})

    def post(self, request, *args, **kwargs):
        print(request.POST.get("url"))
        return render(request, 'shortener/home.html', {})


class KirrCBView(View):  # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL.objects, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
