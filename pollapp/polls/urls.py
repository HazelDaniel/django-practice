from django.contrib import admin
from django.urls import path
from django.urls import include

from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index)
]
