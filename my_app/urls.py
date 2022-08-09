from django.urls import path, re_path, include
from my_site.restful.routers import APIRouter
from my_app import views
from my_app.admin import my_admin_site


# Create your urls here.

like_router = APIRouter(views.Like)
history_router = APIRouter(views.History)
like_router.add_sub_routers(history_router)

urlpatterns = [
    path("hi/", views.hi, name="hi"),
    path("error/", views.error, name="error"),
    path("admin/", my_admin_site.urls, name="admin"),
    *[
        router.urls
        for router in [
            like_router,
            history_router,
        ]
    ],
]
