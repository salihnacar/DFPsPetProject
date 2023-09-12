import django.contrib.auth.urls 
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
# Django admin
path("admin/", admin.site.urls),
# User management
path("accounts/", include("allauth.urls")), # new
# Local apps
path("", include("pages.urls")),

path("books/", include("books.urls")), # new
]+ static(
settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # !!! FIX IN PRODUCTION  !!!

if settings.DEBUG: # new
    import debug_toolbar
    urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

