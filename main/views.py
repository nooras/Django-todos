from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from .models import Todo
from django.http import Http404
from .forms import  TodoForm
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class IndexView(ListView):
    queryset = Todo.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['today'] = datetime.now().date()
        ctx['app_name'] = 'Super Todos'
        return ctx

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    template = loader.get_template('main/index.html')
    context = {
        'todos' : todos,
        'today':datetime.now(),
        'app_name': "Super Todos"
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'main/index.html', context=context)


class TodoDetailView(DetailView):
    model = Todo

def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    '''
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        raise Http404("Todo with id: {} does not exist.".format(todo_id))
    '''
    context = {
        'todo': todo
    }
    return render(request, 'main/todo_detail.html', context=context)

class TodoCreateView( SuccessMessageMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'main/todo.html'
    success_url = reverse_lazy('index')
    success_message = 'Todo has been created successfully.'

class TodoUpdateView( SuccessMessageMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'main/todo.html'
    success_url = reverse_lazy('index')
    success_message = 'Todo has been updated successfully.'

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The todo was created successfully.')
            return redirect('index')
        else:
            return render(request, 'main/todo.html', {'form': form})
    return render(request, 'main/todo.html', {'form': TodoForm()})

def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'The todo was updated successfully.')
            return redirect('index')
        else:
            return render(request, 'main/todo.html', {'form': form})
    return render(request, 'main/todo.html', {'form': TodoForm(instance=todo)})
