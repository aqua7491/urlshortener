from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def kirr_redirect_view(request, *args, **kwargs):  # function based view
    return HttpResponse("Hello pizduk")


class KirrCBView(View):  # class based view
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello again")
