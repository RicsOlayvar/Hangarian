from django.shortcuts import render

from django.views.generic.list import ListView
from Hangarin.models import Priority, Category, Task, Note, SubTask 

class HomePageView(ListView):
    model = Priority
    context_object_name = 'home'
    template_name = "home.html"

#LISTVIEW
class PriorityListView(ListView):
    model = Priority
    context_object_name = 'priority'
    template_name = 'prty_list.html'
    paginate_by = 5 

class CategoryList(ListView):
    model = Category
    context_object_name = 'category'
    template_name = "catgry_list.html"
    paginate_by = 5

class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = "task_list.html"
    paginate_by = 5

class NoteList(ListView):
    model = Note
    context_object_name = 'note'
    template_name = "note_list.html"
    paginate_by = 5

class SubTask(ListView):
    model = SubTask
    context_object_name = 'subtask'
    template_name = "stask_list.html"
    paginate_by = 5