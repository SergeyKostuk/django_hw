from django.urls import path
from .views import (
    home,
    new_record,
    remove_record,
    show,
    show_all,
    edit_record,
)

urlpatterns = [

    path('homepage/', home, name='home'),
    path('add/', new_record, name='new_record'),
    path('remove/<int:car_id>', remove_record, name='remove_record'),
    path('edit/<int:car_id>', edit_record, name='edit_record'),
    path('show/<str:brand>', show, name='show'),
    path('all/', show_all, name='all'),
]
