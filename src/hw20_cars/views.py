from django.shortcuts import render, redirect
from .forms import CarInfo
from .models import Car


# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')


def new_record(request):
    if request.method == 'GET':
        context = {'form': CarInfo()}
        return render(request, 'add_car.html', context)
    elif request.method == 'POST':
        form = CarInfo(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Car.objects.create(
                brand=data.get('brand'),
                model=data.get('model'),
                color=data.get('color'),
                weight=data.get('weight'),
                owner_full_name=data.get('owner_full_name'),
                release_year=data.get('release_year'),
            )
            redirect('home.html')
        else:
            errors = form.errors

            return HttpResponse(f'{errors}')

    return HttpResponse('Wrong request method')
