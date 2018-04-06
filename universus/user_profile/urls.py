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

from user_profile import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.show_profile, name='show_profile'),
    re_path('show/(?P<account_id>\d+)/', views.show_profile_by_id, name='show_profile_by_id'),
    re_path('delete/(?P<account_id>\d+)/', views.delete_user_profile, name='delete_user_profile'),
]