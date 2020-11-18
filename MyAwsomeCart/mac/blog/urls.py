# This file has been created by Nins Gosai

from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="BlogHome"),
]
