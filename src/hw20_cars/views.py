from django.shortcuts import render, redirect,HttpResponse
from .forms import CarInfo
from .models import Car


# Create your views here.

def home(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        brand_list=[]

        for car in cars:
            brand_list.append(car.brand)
        brand_set = set(brand_list)

        context = {'brand_set': brand_set}
        return render(request, 'home.html', context)
def show_all(request):
    if request.method == 'GET':
        cars = Car.objects.all()

        context = {'cars': cars}
        return render(request, 'show_all.html', context)
def show(request, brand):
    if request.method == 'GET':

        one_brand = Car.objects.filter(brand=brand)
        context = {'one_brand': one_brand}
        return render(request, 'show.html', context)
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
            return redirect('home')
        else:
            errors = form.errors

            return HttpResponse(f'{errors}')
    else:
        return HttpResponse('Wrong request method')


def remove_record(request,car_id):

    car = Car.objects.get(id=car_id)


    car.delete()
    return redirect('home')
