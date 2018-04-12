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

from exam_builder import views
from django.urls import path, include, re_path

urlpatterns = [
    path('add/', views.exam_buider, name='exam_builder'),
    path('list/', views.exam_list, name='exam_list'),
    re_path('show/(?P<exam_id>\d+)/', views.exam_show, name='exam_show'),
    re_path('choosegroup/(?P<exam_id>\d+)/', views.choose_group, name='choose_group'),
    re_path('settest/(?P<group_id>\d+)/(?P<exam_id>\d+)/', views.set_test, name='set_test'),

]