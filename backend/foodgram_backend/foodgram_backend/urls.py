from django.contrib import admin
from django.urls import path, include

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework import permissions


# Почему-то перестал работать. Исправлю...
schema_view = get_schema_view(  # Swagger
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    # url=f'{settings.APP_URL}/api/v3/',
    # patterns=[path('api/', include('foodgram_api.urls')), ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('foodgram_api.urls', namespace='foodgram_api')),


    path(  # Swagger
        'swagger-ui/',
        TemplateView.as_view(
            template_name='swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'),
    url(  # Swagger
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
]
