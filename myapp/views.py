from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("<h1>This is from home page</h1>")


def another_view(request):
    return HttpResponse("<h1>This is from another page</h1>")

def root_page_view(request):
    return render(request, template_name="myapp/root_page.html")


def portfolio_view(request):
    return render(request, template_name="portfolio/index.html")