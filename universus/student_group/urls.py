"""universus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from student_group import views
from django.urls import path, include, re_path

urlpatterns = [
    re_path('show/(?P<group_id>\d+)/', views.student_group, name='student_group'),
    re_path('add_student/(?P<group_id>\d+)/', views.add_student_to_group, name='add_student_to_group'),
    re_path('add_teacher/(?P<group_id>\d+)/', views.add_teacher_to_group, name='add_teacher_to_group'),
    re_path('add/(?P<department_id>\d+)/', views.add_student_group, name='add_student_group'),
    re_path('added_student/(?P<group_id>\d+)/(?P<student_id>\d+)/',
            views.added_student_to_group, name='added_student_to_group'),
    re_path('added_teacher/(?P<group_id>\d+)/(?P<teacher_id>\d+)/',
            views.added_teacher_to_group, name='added_teacher_to_group'),
    re_path('delete_student/(?P<group_id>\d+)/(?P<student_id>\d+)/',
            views.delete_student, name='delete_student'),
    re_path('leave/(?P<group_id>\d+)/',
            views.leave_group, name='leave_group'),
    re_path('mygroups/', views.my_groups, name='my_groups'),
]