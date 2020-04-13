from django.urls import path
from . import views

urlpatterns = [
    path('random', views.random),
    path('generate', views.generate),
    path('reset_count', views.reset_count),
]