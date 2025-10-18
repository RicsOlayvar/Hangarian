from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from Hangarin.forms import PriorityForm, CategoryForm, TaskForm, NoteForm, SubTaskForm
from django.urls import reverse_lazy
from Hangarin.models import Priority, Category, Task, Note, SubTask 
from django.db.models import Q
from django.utils import timezone

class HomePageView(ListView):
    model = Priority
    context_object_name = 'home'
    template_name = "home.html"

#LISTVIEW
class PriorityListView(ListView):
    model = Priority
    context_object_name = 'priorities'
    template_name = 'prty_list.html'
    paginate_by = 5 

    
    def get_queryset(self):
        query = self.request.GET.get('q')
        
        if query:
            return Priority.objects.filter(name__icontains=query)
        return Priority.objects.all()


    


class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = "catgry_list.html"
    paginate_by = 5


    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset
    

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "task_list.html"
    paginate_by = 5
    ordering = ["Title"]

    def get_ordering(self):
        allowed = ["Title", "task_category__name", "task_priority__name", "deadline", "status"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "Title"


    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(Title__icontains=query) |
                Q(task_category__name__icontains=query) |
                Q(task_priority__name__icontains=query)
            )
        return qs


    

class NoteList(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = "note_list.html"
    paginate_by = 5
    ordering = ["created_at"]

    def get_ordering(self):
        allowed = ["created_at", "updated_at", "related_task__Title"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "created_at"

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
            Q(related_task__Title__icontains=query)
            )

        return qs



    

class SubTaskList(ListView):
    model = SubTask
    context_object_name = 'subtasks'
    template_name = "stask_list.html"
    paginate_by = 5
    ordering = ["title", "parent_task__title"]

    def get_ordering(self):
        allowed = ["title", "parent_task__title", "status", "created_at"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "title"

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(status__icontains=query)
            )
        return qs





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


#UPDATE 
class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'prty_form.html'
    success_url = reverse_lazy('priority-list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catgry_form.html'
    success_url = reverse_lazy('category-list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'stask_form.html'
    success_url = reverse_lazy('subtask-list')

#DELETE
class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'prty_del.html' 
    success_url = reverse_lazy('priority-list') 


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'catgry_del.html' 
    success_url = reverse_lazy('category-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html' 
    success_url = reverse_lazy('task-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html' 
    success_url = reverse_lazy('note-list')

class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'stask_del.html' 
    success_url = reverse_lazy('subtask-list')