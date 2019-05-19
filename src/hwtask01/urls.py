from django.urls import path
from hwtask01.views import record
from hwtask01.views import display_
from hwtask01.views import delete_and_go_to_record

urlpatterns = [

    path('record/', record),
    path('display_/', display_),
    path('del/', delete_and_go_to_record),

]
