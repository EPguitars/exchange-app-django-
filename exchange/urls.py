from django.urls import path
from . import views

urlpatterns = [
    path('', views.exchange, name='main'),
    path('test', views.test, name='test')
]