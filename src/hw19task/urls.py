from django.urls import path
from .views import salle


urlpatterns = [

    path('ticket/', salle, name='ticket'),


]
