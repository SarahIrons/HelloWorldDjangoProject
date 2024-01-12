from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:pk>/details/', views.details, name="details"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('submitOrDeleteProfile/', views.delete, name="submitOrDeleteProfile"),
    path('createProfile/', views.createRecord, name="createProfile"),
]
