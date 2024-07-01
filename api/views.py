from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, \
UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from crud.models import Classroom, Student
from .serializers import ClassRoomSerializer, StudentSerializer, ClassRoomModelSerializer, StudentModelSerializer


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
            }, status=404)
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
            }, status=404)
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
    
    def post(self, *args, **kwargs):
        data = self.request.data
        name = data.get("name")
        section = data.get("section")
        classroom = Classroom.objects.create(name=name, section=section)  # ORM
        return Response({
            "message": "Classroom created successfully !",
            "id": classroom.id,
            "name": classroom.name,
            "section": classroom.section
        }, status=201)
    
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
            "classroom": student.classroom.id if student.classroom else None
        })
        return Response(response)
    
    def post(self, *args, **kwargs):
        name = self.request.data.get("name")
        age = self.request.data.get("age")
        email = self.request.data.get("email")
        address = self.request.data.get("address")
        student = Student.objects.create(name=name, age=age, email=email, address=address)
        return Response({
            "message": "Student created successfully !",
            "name": student.name,
            "age": student.age,
            "email": student.email,
            "address": student.address
        }, status=201)


class ClassRoomDetailUsingSerView(APIView):
    def get(self, *args, **kwargs):
        classroom_id = kwargs["id"]
        try:
            classroom = Classroom.objects.get(id=classroom_id)  # classroom object
        except:
            return Response({
                "message": "Invalid id"
            }, status=404)
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
            }, status=404)
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
    
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = ClassRoomSerializer(data=data)  # This is deserialization
        print(serializer.is_valid())
        if serializer.is_valid():
            validated_data = serializer.validated_data
            print(validated_data)
            name = validated_data.get("name")
            section = validated_data.get("section")
            Classroom.objects.create(name=name, section=section)
            return Response({
                "message": "Classroom created successfully",
                "data": serializer.data
            }, status=201)
        else:
            return Response(serializer.errors, status=400)
    

class StudentListUsingSerView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()  # queryset
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = StudentSerializer(data=data)  # This is deserialization
        print(serializer.is_valid())
        if serializer.is_valid():
            validated_data = serializer.validated_data
            print(validated_data)
            name = validated_data.get("name")
            age = validated_data.get("age")
            email = validated_data.get("email")
            address = validated_data.get("address")
            Student.objects.create(name=name, age=age, email=email, address=address)
            return Response({
                "message": "Student created successfully",
                "data": serializer.data
            }, status=201)
        else:
            return Response(serializer.errors, status=400)
        
    
class ClassRoomView(APIView):
    def get(self, *args, **kwargs):
        classrooms = Classroom.objects.all()
        serializer = ClassRoomModelSerializer(classrooms, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = ClassRoomModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Classroom created successfully !",
                "data": serializer.data
            }, status=201)
        return Response(serializer.errors, status=400)


class StudentView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many=True, 
                                            context={"request": self.request})
        return Response(serializer.data)
    
    def post(self, *args, **kwargs):
        ser = StudentModelSerializer(data=self.request.data, context={"request": self.request})
        if ser.is_valid():
            ser.save()
            return Response({
                "message": "Student created successfully !",
                "data": ser.data
            })
        return Response(ser.errors)
    

class ClassRoomGenericView(ListAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = Classroom.objects.all()


class ClassRoomGenericCreateView(CreateAPIView):
    serializer_class = ClassRoomModelSerializer


class ClassRoomListCreateView(ListCreateAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = Classroom.objects.all()


class ClassRoomUpdateGenericView(UpdateAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = Classroom.objects.all()


class ClassRoomUpdateDetailDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = Classroom.objects.all()


class ClassRoomViewset(ModelViewSet):
    serializer_class = ClassRoomModelSerializer
    queryset = Classroom.objects.all()
