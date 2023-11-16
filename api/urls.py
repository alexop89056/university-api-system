from django.urls import path
from .views.student import StudentView, StudentsView, CreateStudentView
from .views.course import CourseView, CoursesView, CreateCourseView
from .views.term import TermView, TermsView, CreateTermView
from .views.student_card import StudentCardView, StudentCardsView, CreateStudentCardView
from .views.teacher import TeacherView, TeachersView, CreateTeacherView
from .views.course_term import CourseTermView, CourseTermsView, CreateCourseTermView

urlpatterns = [
    path('students', StudentsView.as_view()),
    path('student/<int:pk>/', StudentView.as_view()),
    path('student/create', CreateStudentView.as_view()),

    path('courses', CoursesView.as_view()),
    path('course/<int:pk>/', CourseView.as_view()),
    path('course/create', CreateCourseView.as_view()),

    path('terms', TermsView.as_view()),
    path('term/<int:pk>/', TermView.as_view()),
    path('term/create', CreateTermView.as_view()),

    path('student-cards', StudentCardsView.as_view()),
    path('student-card/<int:pk>/', StudentCardView.as_view()),
    path('student-card/create', CreateStudentCardView.as_view()),

    path('teachers', TeachersView.as_view()),
    path('teacher/<int:pk>/', TeacherView.as_view()),
    path('teacher/create', CreateTeacherView.as_view()),

    path('course-terms', CourseTermsView.as_view()),
    path('course-term/<int:pk>/', CourseTermView.as_view()),
    path('course-term/create', CreateCourseTermView.as_view()),
]
