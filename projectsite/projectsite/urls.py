"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from Hangarin.views import HomePageView, PriorityListView, CategoryList, TaskList, NoteList, SubTask

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('priority_list',PriorityListView.as_view(), name='priority-list' ),
    path('category_list',CategoryList.as_view(), name='category-list' ),
    path('task_list',TaskList.as_view(), name='task-list' ),
    path('note_list',NoteList.as_view(), name='note-list' ),
    path('subtask_list',SubTask.as_view(), name='subtask-list' ),
    
    
    
]
