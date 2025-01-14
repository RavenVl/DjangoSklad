from django.urls import path
from . import views

app_name = 'sklad'

urlpatterns = [
    path('', views.index, name='index'),
]
