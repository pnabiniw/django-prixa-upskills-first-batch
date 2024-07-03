from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import (MessageView, SimpleStudentView, ClassRoomDetailView, 
                    StudentDetailView, ClassroomListView, StudentListView, 
                    ClassRoomDetailUsingSerView, StudentDetailUsingSerView, 
                    ClassRoomListUsingSerView, StudentListUsingSerView, ClassRoomView,
                    StudentView, ClassRoomGenericView, ClassRoomGenericCreateView, 
                    ClassRoomListCreateView, ClassRoomUpdateGenericView, ClassRoomUpdateDetailDeleteView,
                    ClassRoomViewset, LoginView)

router = DefaultRouter()  # object of default router
router.register("classroom-viewset", ClassRoomViewset, basename="classroom")  # classroom_destroy

urlpatterns = [
    path("message/", MessageView.as_view(), name="simple-message"),
    path("simple-student/", SimpleStudentView.as_view()),
    path("classroom/<int:id>/", ClassRoomDetailView.as_view()),
    path("classroom-list/", ClassroomListView.as_view()),
    path("student-list/", StudentListView.as_view()),
    path("student/<int:id>/", StudentDetailView.as_view()),
    # path("login/", obtain_auth_token, name="api_login"),
    path("login/", LoginView.as_view(), name="api_login"),
]

urls_for_serializer_views = [
    path("classroom-using-serializer/<int:id>/", ClassRoomDetailUsingSerView.as_view()),
    path("student-using-serializer/<int:id>/", StudentDetailUsingSerView.as_view()),
    path("classroom-list-using-serializer/", ClassRoomListUsingSerView.as_view()),
    path("student-list-using-serializer/", StudentListUsingSerView.as_view()),

    path("classroom-model-ser/", ClassRoomView.as_view()),
    path("student-model-ser/", StudentView.as_view()),
]

urls_for_generic_views = [
    path("classroom-generic-view/", ClassRoomGenericView.as_view()),
    path("classroom-generic-create-view/", ClassRoomGenericCreateView.as_view()),
    path("classroom-list-create/", ClassRoomListCreateView.as_view()),

    path("classroom-update/<int:pk>/", ClassRoomUpdateGenericView.as_view()),
    path("classroom-detail-update-delete/<int:pk>/", ClassRoomUpdateDetailDeleteView.as_view()),
]

urlpatterns += urls_for_serializer_views + urls_for_generic_views + router.urls