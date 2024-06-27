from django.urls import path
from .views import (MessageView, SimpleStudentView, ClassRoomDetailView, 
                    StudentDetailView, ClassroomListView, StudentListView, 
                    ClassRoomDetailUsingSerView, StudentDetailUsingSerView, 
                    ClassRoomListUsingSerView, StudentListUsingSerView, ClassRoomView,
                    StudentView)


urlpatterns = [
    path("message/", MessageView.as_view()),
    path("simple-student/", SimpleStudentView.as_view()),
    path("classroom/<int:id>/", ClassRoomDetailView.as_view()),
    path("classroom-list/", ClassroomListView.as_view()),
    path("student-list/", StudentListView.as_view()),
    path("student/<int:id>/", StudentDetailView.as_view()),
]

urls_for_serializer_views = [
    path("classroom-using-serializer/<int:id>/", ClassRoomDetailUsingSerView.as_view()),
    path("student-using-serializer/<int:id>/", StudentDetailUsingSerView.as_view()),
    path("classroom-list-using-serializer/", ClassRoomListUsingSerView.as_view()),
    path("student-list-using-serializer/", StudentListUsingSerView.as_view()),

    path("classroom-model-ser/", ClassRoomView.as_view()),
    path("student-model-ser/", StudentView.as_view()),
]

urlpatterns += urls_for_serializer_views