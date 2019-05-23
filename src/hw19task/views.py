from django.shortcuts import render
from .forms import AvioSaleForms
from django.http import HttpResponse


# Create your views here.
def salle(request):
    if request.method == 'GET':
        form = AvioSaleForms()
        context = {'form': AvioSaleForms()}
        return render(request, 'form_for_avioticket.html', context)
    if request.method == 'POST':
        form = AvioSaleForms(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            number_of_tickets = data.get('number_of_tickets')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
        if number_of_tickets == 1:
            print('стоимость 100$')
        elif number_of_tickets > 1:
            result_cost = 2 * number_of_tickets * 100


        return render(request, 'display_cost.html', {'result_cost': result_cost})
