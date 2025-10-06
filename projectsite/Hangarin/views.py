from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from Hangarin.forms import OrganizationForm
from django.urls import reverse_lazy
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

class SubTaskList(ListView):
    model = SubTask
    context_object_name = 'subtask'
    template_name = "stask_list.html"
    paginate_by = 5


#CREATEVIEW
class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'prty_form.html'
    success_url = reverse_lazy('priority-list')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catgry_form.html'
    success_url = reverse_lazy('category-list')

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'stask_form.html'
    success_url = reverse_lazy('subtask-list')