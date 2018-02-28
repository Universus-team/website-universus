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
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('singup/', include('singup.urls')),
    path('exambuilder_body/', include('exam_builder.urls')),
    path('profile_body/', include('user_profile.urls')),
    path('error/', include('pages_error.urls')),
    path('about_body/', include('about.urls')),
    path('university_body/', include('university.urls')),
    path('chat_body/', include('chat.urls')),
    path('timetable_body/', include('timetable.urls')),

    # must be at the end
    re_path('(^[a-zA-Z]+_$|^[a-zA-Z]+_/[a-zA-Z_]+$)', include('main.urls')),
]
