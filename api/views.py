from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from crud.models import Classroom, Student
from .serializers import ClassRoomSerializer, StudentSerializer


class MessageView(APIView):
    def get(self, *args, **kwargs):
        # Response by default returns JSONResponse
        return Response({
            "message": "This is my first API"
        })


class SimpleStudentView(APIView):
    def get(self, *args, **kwargs):
        return Response({
            "name": "Jon",
            "age": 25,
            "address": "KTM"
        })


class ClassRoomDetailView(APIView):
    def get(self, *args, **kwargs):
        classroom_id = kwargs["id"]
        try:
            classroom = Classroom.objects.get(id=classroom_id)
        except:
            return Response({
                "message": "Invalid id"
            })
        return Response({
            "id": classroom.id,
            "name": classroom.name,
            "section": classroom.section
        })


class StudentDetailView(APIView):
    def get(self, *args, **kwargs):
        student_id = kwargs["id"]
        try:
            student = Student.objects.get(id=student_id)
        except:
            return Response({
                "message": "Invalid id"
            })
        return Response({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "email": student.email,
            "address": student.address,
            "classroom": student.classroom.id
        })
    

class ClassroomListView(APIView):
    def get(self, *args, **kwargs):
        classrooms = Classroom.objects.all()
        response = []
        for classroom in classrooms:
            response.append({
            "id": classroom.id,
            "name": classroom.name,
            "section": classroom.section
        })

        # [{}, {}, {}]
        return Response(response)
    
class StudentListView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        response = []
        for student in students:
            response.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "email": student.email,
            "address": student.address,
            "classroom": student.classroom.id
        })
        return Response(response)


class ClassRoomDetailUsingSerView(APIView):
    def get(self, *args, **kwargs):
        classroom_id = kwargs["id"]
        try:
            classroom = Classroom.objects.get(id=classroom_id)  # classroom object
        except:
            return Response({
                "message": "Invalid id"
            })
        serializer = ClassRoomSerializer(classroom)  # This is serialization
        return Response(serializer.data)


class StudentDetailUsingSerView(APIView):
    def get(self, *args, **kwargs):
        student_id = kwargs["id"]
        try:
            student = Student.objects.get(id=student_id)
        except:
            return Response({
                "message": "Invalid id"
            })
        serializer = StudentSerializer(student)  # This is serialization
        return Response(serializer.data)


class ClassRoomListUsingSerView(APIView):
    def get(self, *args, **kwargs):
        query_dict = self.request.GET   # {"search": "A", "a": 1, "b": 2}
        search = query_dict.get("search")
        section = query_dict.get("section")
        if search and section:
            classrooms = Classroom.objects.filter(name__startswith=search, section=section)  # queryset
        elif search:
            classrooms = Classroom.objects.filter(name__startswith=search)
        elif section:
            classrooms = Classroom.objects.filter(section=section)
        else:
            classrooms = Classroom.objects.all()
        serializer = ClassRoomSerializer(classrooms, many=True)

        # response = []
        # for classroom in classrooms:
        #     ser = ClassRoomSerializer(classroom)
        #     response.append(ser.data)
        return Response(serializer.data)
    

class StudentListUsingSerView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()  # queryset
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

