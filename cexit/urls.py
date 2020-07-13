
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from student import views as student_views
from teacher import views as teacher_views
from teacher.views import QuestionCreateView,QuestionUpdateView,QuestionDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name="student/login.html"),name='login'),
    path('student/home',student_views.home,name='student-home'),
    path('teacher/home',teacher_views.home,name='teacher-home'),
    path('logout/',auth_views.LogoutView.as_view(template_name="student/logout.html"),name='logout'),
    path('redirectingurl',student_views.redirectingview,name='redirectingurl'),
    path('teacher/course/<int:id>/questions',teacher_views.show_questions,name='show_questions'),
    path('teacher/course/<int:id>/charts',teacher_views.show_charts,name='show_charts'),
    path('teacher/course/<int:id>/questions/create',QuestionCreateView.as_view(),name='create_questions'),
    path('teacher/course/<int:id>/questions/<int:pk>/update',QuestionUpdateView.as_view(),name='update_questions'),
    path('teacher/course/<int:id>/questions/<int:pk>/delete',QuestionDeleteView.as_view(),name='delete_questions'),
    path('student/course/<int:id>/questions',student_views.show_questions,name='show_questions_students'),
    path('teacher/course/<int:id>/questions/<int:pk>/responses',teacher_views.show_responses,name='show_responses'),
    path('changepassword',student_views.change_password,name="changepassword"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='course/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='course/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='course/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='course/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
   