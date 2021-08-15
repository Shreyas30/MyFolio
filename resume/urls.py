from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="ResumeHome" ),
    path('input/', views.inputData, name="Input"),
]