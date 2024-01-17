import task1 as task1
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import TodoForms
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


# Create your views here.


class TaskListview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'


class TaskDetailView(DetailView):
    model=Task
    template_name = 'details.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class TaskDeleteView(DeleteView):
    model=Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('cbvhome')


def add(request):
    task1=Task.objects.all()
    if request.method=='POST':
        name1=request.POST.get('task','')
        priority1=request.POST.get('priority','')
        date1=request.POST.get('date','')
        task=Task(name=name1,priority=priority1,date=date1)
        task.save()

    return render(request,'home.html',{'task1':task1})


def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    task=Task.objects.get(id=id)
    form1=TodoForms(request.POST or None,instance=task)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'f':form1,'task':task})






