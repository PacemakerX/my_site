from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


def landing_page(request):
    return render(request, "my_site/landing_page.html")

def handle_404(request,resource):
    return render(request,'404.html')