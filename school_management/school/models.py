from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name

class Classroom(models.Model):
    school = models.ForeignKey(School, related_name='classrooms', on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    floor = models.IntegerField()

    def __str__(self):
        return f"{self.grade} - {self.school.name}"
    
class Teacher(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"