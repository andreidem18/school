from django.shortcuts import render
from classes.models import Class

def all_classes(request):
    classes = Class.objects.all()
    return render(request, 'classes/all-classes.html', {'classes': classes})

def my_class(request, class_id):
    my_class = Class.objects.get(id=class_id)
    context = {
        'class': my_class,
        'students': list(my_class.student.values())
    }
    return render(request, 'classes/class.html', context)

def init(request):
    return render(request, 'init/init.html', {})