from django.contrib import admin

from .models import Student, Course, CourseTerm, Term, Teacher, StudentCard


admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CourseTerm)
admin.site.register(Term)
admin.site.register(Teacher)
admin.site.register(StudentCard)

# Register your models here.
