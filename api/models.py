from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return f'<Student {self.id}, {self.name}>'


class StudentCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'<StudentCard for Student {self.student.id}>'


class Course(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return f'<Course {self.id}>'


class Term(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return f'<Term {self.id}>'


class CourseTerm(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)

    def __str__(self):
        return f'<CourseTerm {self.id}>'


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    rank = models.CharField(max_length=40)

    def __str__(self):
        return f'<Teacher {self.id}, {self.name}>'
