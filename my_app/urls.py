from django.urls import path
from my_site.restful.routers import APIRouter
from my_app import views


# Create your urls here.

urlpatterns = [
    path("hi/", views.hi, name="hi"),
    path("error/", views.error, name="error"),
    APIRouter("like/", views.LikeViewSet).urls,
]
