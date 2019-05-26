from django.urls import path
from .views import home, new_record


urlpatterns = [

    path('homepage/', home, name='home'),
    path('add/', new_record, name='new_record'),
]
