from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Glow Beauty API',
        default_version='v1',
        description='API documentation for glow beauty',
        contact=openapi.Contact(email="umidgaybullayev955@gmail.com"),
        license=openapi.License(name='Glow Beauty Licence'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/account/', include('apps.account.urls')),
    path("api/", include("apps.base.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)