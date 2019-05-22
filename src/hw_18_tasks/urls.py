from django.urls import path
from hw_18_tasks.views import record
from hw_18_tasks.views import display_
from hw_18_tasks.views import clear


urlpatterns = [

    path('record/', record),
    path('display_/', display_),
    path('del/', clear),

]
