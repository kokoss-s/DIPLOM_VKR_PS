from django.urls import path

from . import views

app_name = 'fire'

urlpatterns = [
    path('', views.fire_form, name='fire_form'),
    path('list/', views.fire_list, name='fire_list'),
]
