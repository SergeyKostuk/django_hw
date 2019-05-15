from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        texts = [request.POST.get('text1'), request.POST.get('text2'), request.POST.get('text3')]
        return HttpResponse('longest word is {}'.format(max(texts, key=len)))
