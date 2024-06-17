from django.shortcuts import render, redirect
from .models import Classroom, Student

def classroom_view(request):
    return render(request, template_name="crud/classroom.html", 
                  context={"classrooms": Classroom.objects.all()})


def add_classroom_view(request):
    if request.method == "POST":
        print(request.POST)
        classroom_name = request.POST.get("classroom_name")
        section = request.POST.get("classroom_section")
        Classroom.objects.create(name=classroom_name, section=section)
        return redirect("crud_classroom")
    return render(request, template_name="crud/add_classroom.html")
