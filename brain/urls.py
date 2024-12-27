from django.urls import path
from brain.views import *
app_name='brain'
urlpatterns=[
    path('doctor/',doctor,name='doctor'),
    path('doctor1/',doctor1,name='doctor1'),
]