from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def check_date(request):
    if request.method == "POST":
        datee =  request.POST.get('date')
        _date = list(map(int, datee.split('-')))
        if _date[1] == 1 and _date[2] == 1:
            return HttpResponse(f'С новым {_date[0]} годом')
        else:
            return HttpResponse(datee)
