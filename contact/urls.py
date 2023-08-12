from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sunny", views.sunny, name="sunny"),
]