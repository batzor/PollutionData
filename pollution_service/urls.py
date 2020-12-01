from django.urls import path

from . import views

urlpatterns = [
    path('recommendation/', views.recommendation, name='recommendation'),
    path('', views.home, name='home'),
]
