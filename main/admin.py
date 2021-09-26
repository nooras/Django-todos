from django.contrib import admin

# Register your models here.
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'done')
    list_filter = ('done', 'due_date')
    ordering = ('due_date',)

admin.site.register(Todo, TodoAdmin)
