from django.urls import path
from .views import classroom_view, add_classroom_view


urlpatterns = [
    path("classroom/", classroom_view, name="crud_classroom"),
    path("add-classroom/", add_classroom_view, name="add_classoom")
]
