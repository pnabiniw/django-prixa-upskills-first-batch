from django.urls import path
from .views import (classroom_view, add_classroom_view, update_classroom_view, delete_classroom_view, 
student_view, add_student_view)


urlpatterns = [
    path("classroom/", classroom_view, name="crud_classroom"),
    path("student/", student_view, name="crud_student"),
    path("add-classroom/", add_classroom_view, name="add_classoom"),
    path("add-student/", add_student_view, name="add_student"),
    path("update-classroom/<int:id>/", update_classroom_view, name="update_classroom"),
    path("delete-classroom/<int:id>/", delete_classroom_view, name="delete_classroom"),
]
