from django.contrib import admin
from django.urls import path
from django.urls import include

from django.contrib import admin
from django.urls import path, include
from .views import vote, IndexView, ResultsView, IndexView, DetailView

app_name = "polls"
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('<int:pk>/', DetailView.as_view(), name="detail"),
    path('<int:pk>/results', ResultsView.as_view(), name="results"),
    path('<int:question_id>/vote', vote, name="vote"),
]
