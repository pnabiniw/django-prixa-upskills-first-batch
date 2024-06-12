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

def learning_dtl_view(request):
    c = {"name": "Prixa Academy", "student": "Jane"}
    s = [
        {"name": "Jon", "age": 30, "display": True},
        {"name": "Alex", "age": 21, "display": False},
        {"name": "Hary", "age": 23, "display": True},
        {"name": "Arya", "age": 24, "display": False},
    ]
    c.update(students=s)  # {"name": "Prixa Academy", "student": "Jane", "students": []}
    # Context should always be a dictionary
    return render(request, template_name="myapp/dtl.html", context=c)


# Features from DTTL
# 1. {% load static %}
# 2. {% url 'home' %}
# 3. {% static 'stati/path' %}
# 4. {{name}}
# 5. For Loop => {% for each in data %}{% endfor %}
# 6. If Conditions => {% if condition %}{% endif %}
#  {% if condition %} {%else%} {% endif %}
#  {% if condition %} {% elif condition} {%else%} {% endif %}


def using_bootstrap_view(request):
    s = [
        {"name": "Jon", "age": 30, "email": "jon@email.com", "address": "KTM", "display": True},
        {"name": "Alex", "age": 21, "email": "alex@email.com", "address": "PKR", "display": False},
        {"name": "Hary", "age": 23, "email": "hary@email.com", "address": "BKT", "display": True},
        {"name": "Arya", "age": 24, "email": "arya@email.com", "address": "LTP", "display": False},
    ]
    return render(request, template_name="myapp/using_bootstrap.html", context={"students": s})