from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.aboutUs, name = 'aboutUs'),
    path('results',views.results, name = 'results')
]