from django.urls import path, re_path, include
from my_site.rest.routers import APIRouter
from my_app import views


# Create your urls here.

urlpatterns = [
    path("hi/", views.hi, name="hi"),
    path("error/", views.error, name="error"),
    APIRouter("like/").register(views.LikeListView, views.LikeDetailView),
]
