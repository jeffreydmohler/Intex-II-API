from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    re_path(r'^.*/', include('client.urls')),
    re_path(r'', include('client.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
