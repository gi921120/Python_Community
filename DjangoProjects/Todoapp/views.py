from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoviewer(request):
    all_todo_items = TodoItem.objects.all()
    return render(request,'todoapp.html',
    {'all_items': all_todo_items})

def addTodo(request):
    new_item =TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/Todoapp/')

def deleteTodo(request, Todoapp_id):
    item_delete=TodoItem.objects.get(id=Todoapp_id)
    item_delete.delete()
    return HttpResponseRedirect('/Todoapp/')
# Create your views here.
