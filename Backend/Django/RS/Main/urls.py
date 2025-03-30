from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('Projects/', views.ProjectList.as_view(), name='projects-list'),
    path('Projects/<slug:project_slug>/', views.projects_by_slug, name='project'),
    path('Analytics/', views.analytics, name='analytics'),
    path('Profile/<int:user_id>', views.users, name='users'),
    path('Logout/', views.logout_view, name='logout'),
]