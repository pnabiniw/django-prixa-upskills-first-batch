from django.urls import path
from .views import (home_view, another_view, root_page_view, portfolio_view, 
                    learning_dtl_view, using_bootstrap_view)

urlpatterns = [
    path("home/", home_view),
    path("another/", another_view),
    path("my-portfolio/", portfolio_view, name="portfolio"),
    path("learning-dtl/", learning_dtl_view, name="learning_dtl"),
    path("using-bootstrap/", using_bootstrap_view, name="using_bootstrap"),
    path("", root_page_view, name="root_page")
]
