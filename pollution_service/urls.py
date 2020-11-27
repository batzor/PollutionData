from django.urls import path

from . import views

urlpatterns = [
    path('recommendation/', views.recommendation, name='recommendation'),
    path('search/', views.search, name='search'),
    path('', views.home, name='home'),
]
