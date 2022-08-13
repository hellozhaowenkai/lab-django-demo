from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from my_site.restful.routers import APIRouter
from my_app import views
from my_app.admin import my_admin_site


# Create your urls here.

like_router = APIRouter(views.Like)
history_router = APIRouter(views.History)
like_router.add_sub_routers(history_router)

urlpatterns = [
    # WEBs
    path("", views.index, name="index"),
    path("admin/", my_admin_site.urls, name="admin"),
    # APIs
    path("hi/", views.hi, name="hi"),
    path("error/", views.error, name="error"),
    *[
        router.urls
        for router in [
            like_router,
            history_router,
        ]
    ],
]

# https://docs.djangoproject.com/en/3.2/howto/static-files/
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
