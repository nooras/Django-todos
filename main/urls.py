from django.urls import path
from .views import index, todo_detail, todo_create, todo_update, TodoCreateView, TodoUpdateView, IndexView, TodoDetailView

urlpatterns = [
    #path('index', index, name='index'),
    path('', IndexView.as_view(), name='index'),
    #path('todo/<int:todo_id>/', todo_detail, name='todo_detail'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    #path('todo/', todo_create, name='todo_create'), 
    path('todo/', TodoCreateView.as_view(), name='todo_create'), #For class
    #path('todo/<int:todo_id>/update', todo_update, name='todo_update'),
    path('todo/<int:pk>/update', TodoUpdateView.as_view(), name='todo_update'),
]