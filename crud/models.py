from django.db import models


class Classroom(models.Model):  # Here Model class of Django is inherited
    name = models.CharField(max_length=20)  # One
    section = models.CharField(max_length=5)


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()  # a@a.com, abcd
    address = models.CharField(max_length=50)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="classroom_students", 
                                  null=True, blank=True)

