from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import TaskUpdateForm
from django.views import View
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/task_list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy('todo:task_list')
    template_name = 'todo/task_list.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)
    

    
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy("todo:task_list")
    form_class = TaskUpdateForm
    template_name = "todo/task_update.html"
    


class TaskCompleteView(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy('todo:task_list')

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get('pk'))
        object.complete = True
        object.save()
        return redirect(self.success_url)
    


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('todo:task_list')


    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
    