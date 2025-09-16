from django.shortcuts import render
from myApp.models import *

def index(request):
    
    
    
    return render(request, 'index.html', {
        'students': Student.objects.all(),
        'teachers': Teacher.objects.all(),
        'employees': Employee.objects.all(),
    })
    
