# core/urls.py

from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve

from .views import infoView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("polls.urls")),
    path("cbvpolls/", include("cbvpolls.urls")),
    path("info", infoView, name="info"),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root": settings.MEDIA_ROOT,
            },
        ),
    ]
