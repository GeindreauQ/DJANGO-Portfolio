from django.contrib import admin
from django.urls import path, include
from .views import (
    homePage,
    projectsPage,
    projectDetail,
    search,
    handler404,
)

from django.conf import settings
from django.conf.urls.static import static


handler404 = handler404

urlpatterns = [

    path('', homePage, name='homePage'),
    path('projects/', projectsPage, name='projectsPage'),
    path('projects/<str:slug>/', projectDetail, name='projectDetail'),
    path('search/', search, name='search'),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
