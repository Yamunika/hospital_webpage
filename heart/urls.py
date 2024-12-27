from django.urls import path
from heart.views import *
app_name='heart'
urlpatterns=[
    path('specalist/',specalist,name='specialist'),
    path('specalist1/',specalist1,name='specialist1'),

]
