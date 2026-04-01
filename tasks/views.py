from django.views.generic import ListView
from .models import Task

# Create your views here.
class TaskListView(ListView):
    template_name = 'task_list.html'
    model = Task
