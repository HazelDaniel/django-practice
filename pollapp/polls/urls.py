from django.contrib import admin
from django.urls import path
from django.urls import include

from django.contrib import admin
from django.urls import path, include
from .views import index, detail, results, vote

app_name = "polls"
urlpatterns = [
    path('', index),
    path('<int:question_id>/', detail, name="detail"),
    path('<int:question_id>/results', results, name="results"),
    path('<int:question_id>/vote', vote, name="vote"),
]
