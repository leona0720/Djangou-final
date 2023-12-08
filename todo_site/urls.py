"""
URL configuration for todo_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.http import HttpResponseRedirect
from django.urls import include, path
from . import views


def redirect_home(_request):
    return HttpResponseRedirect("polls/")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.contact_list, name='contact_list'),
    path('create/', views.create_contact, name='create_contact'),
    path('create/', views.create_contact, name='create_contact'),
    path('contact/<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('contact/<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('delete-confirm/<int:contact_id>/', views.delete_confirm, name='delete_confirm'),
    path("", redirect_home),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
    # Add other URLs for update, delete, etc.
