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


def update_classroom_view(request, id):
    classroom = Classroom.objects.get(id=id)
    print(classroom.name)
    print(classroom.section)
    if request.method == "POST":
        classroom_name = request.POST.get("classroom_name")  # This data from HTML form
        section = request.POST.get("classroom_section")  # This data from HTML form
        classroom.name = classroom_name  # set data to classroom object
        classroom.section = section  # set data to classroom object
        classroom.save()  # This actually commit / store data to the table
        return redirect("crud_classroom")
    return render(request, template_name="crud/update_classroom.html", context={"classroom": classroom})


def delete_classroom_view(request, id):
    classroom = Classroom.objects.get(id=id)
    if request.method == "POST":
        classroom.delete()
        return redirect("crud_classroom")
    return render(request, template_name="crud/delete_confirmation.html", context={"classroom": classroom})


def student_view(request):
    return render(request, template_name="crud/student_list.html", context={"students": Student.objects.all()})


def add_student_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        address = request.POST.get("address")
        Student.objects.create(name=name, age=age, email=email, address=address)
        return redirect("crud_student")
    return render(request, template_name="crud/add_student.html")
