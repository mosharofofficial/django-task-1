from django.shortcuts import render
from myApp.models import *


def index(request):

    return render(request, 'index.html', {
        'students': Student.objects.filter(age__gte=20),
        'teachers': Teacher.objects.all(),
        'employees': Employee.objects.all(),
    })
