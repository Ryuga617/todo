from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def get_database():
    form = TodoForm()
    forms = Todo.objects.all()
    items = {'form': form, 'forms': forms}
    return items

def top(request):
    items = get_database()

    return render(request, 'price/top.html',items)

def add_task(request):
    task = request.POST['task']
    deadline = request.POST['deadline']
    new_task = Todo(task=task, deadline=deadline)
    new_task.save()
        
    return redirect('top')


def delete(request, form_id):
    delete_task = Todo.objects.get(pk=form_id)
    delete_task.delete()
    
    return redirect('top')

def sort(request):
    form = TodoForm()
    forms= Todo.objects.all().order_by('deadline')
    
    items = {'form' :form, 'forms': forms}
    return render(request, 'price/top.html',items)
    