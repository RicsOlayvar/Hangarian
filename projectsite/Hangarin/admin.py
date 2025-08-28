from django.contrib import admin

from .models import Priority, Category, Task, Note, SubTask

admin.site.register(Priority)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Note)
admin.site.register(SubTask)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'category', 'deadline')
    list_filter =  ('status', 'priority', 'category')
    search_fields = ('title', 'description')

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'parent_task_name')
    def parent_task_name(self, obj):
        return obj.parent_task.Title if obj.parent_task else "—"
    parent_task_name.short_description = 'Parent Task'
    list_filter =  ('status')
    search_fields = ('title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)         
    search_fields = ('name',) 

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name',)         
    search_fields = ('name',) 

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('Title', 'status', 'created_at')
    list_filter = ('created_at',) 
    search_fields = ('Content')
