from django.urls import path
from . import views

urlpatterns = [
    path("resume/", views.resume, name="resume"),
    path("index/", views.book, name="Book"),
]
