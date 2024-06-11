from django.urls import path
from .views import home_view, another_view, root_page_view, portfolio_view

urlpatterns = [
    path("home/", home_view),
    path("another/", another_view),
    path("my-portfolio/", portfolio_view, name="portfolio"),
    path("", root_page_view)
]
