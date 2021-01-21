from django.urls import path
from my_app import views


# Create your views here.


urlpatterns = [
    path("hi/", views.hi, name="hi"),
]
