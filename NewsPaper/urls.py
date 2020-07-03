from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),

    # ALL AUTH URLS
    path('accounts/', include('allauth.urls')),

    # APPS
    path('', include('pages.urls')),
    path('', include('users.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
