from .models import taskmodel
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy
from datetime import timedelta
from django.shortcuts import get_object_or_404, redirect

class taskList(ListView):
    template_name='tasklist.html'
    model=taskmodel
    
class taskCreate(CreateView):
    template_name='taskcreate.html'
    model=taskmodel
    fields=('lecture','number','limit','repeat','repeat_interval')
    success_url=reverse_lazy('list')
    
class taskUpdate(UpdateView):
    template_name='taskupdate.html'
    model=taskmodel
    fields=('lecture','number','limit','repeat','repeat_interval')
    success_url=reverse_lazy('list')
    

def delete_repeat_task(request,pk):
 
    task = get_object_or_404(taskmodel,pk=pk)

    lecture = task.lecture
    number=task.number+1
    limit = task.limit
    repeat = task.repeat
    repeat_interval = task.repeat_interval
  
    task.delete()

    if repeat:
        if repeat_interval == 'daily':
            next_limit = limit + timedelta(days=1)
        elif repeat_interval == 'weekly':
            next_limit = limit + timedelta(weeks=1)
        else:
            next_limit = None

        if next_limit:
            taskmodel.objects.create(
                lecture=lecture,
                number=number,
                limit=next_limit,            
                repeat=repeat,
                repeat_interval=repeat_interval,
            )
            
    return redirect('list') 

class alldelete_confirm(TemplateView):
    template_name ='alldeleteconfirm.html'

class allDelete(DeleteView):
    template_name ='alldelete.html'
    model=taskmodel
    success_url=reverse_lazy('list')
    
    def get_object(self, queryset=None):
        return taskmodel.objects.all()
    
        

