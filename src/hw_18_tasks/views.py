from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.

def record(request):
    if request.method == 'GET':
        template = loader.get_template('name_sname_age.html')

        return HttpResponse(template.render({}, request))
    if request.method == 'POST':
        name = request.POST.get('name')
        sname = request.POST.get('sname')
        age = request.POST.get('age')
        with open('test.txt', 'a') as my_file:
            my_file.write(f'{name} {sname} {age}\n')
        template = loader.get_template('name_sname_age.html')
        return HttpResponse(template.render({}, request))


def display_(request):
    if request.method == 'GET':
        template = loader.get_template('display_list.html')
        with open('test.txt') as my_file:
            my_list = my_file.readlines()

        return HttpResponse(template.render({'my_list': my_list}, request))


def delete_and_go_to_record(request):
    if request.method == 'GET':
        with open('test.txt', 'w') as my_file:
            pass
        template = loader.get_template('name_sname_age.html')

        return HttpResponse(template.render({}, request))
