from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include, re_path

schema_view = get_schema_view(
    openapi.Info(
        title="Course API",
        default_version='v1',
        description="APIs for CourseApp",
        contact=openapi.Contact(email="2151053052quy@ou.edu.vn"),
        license=openapi.License(name="Nguyễn Thi Quý@2021"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('kltn.urls')),
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls',
namespace='oauth2_provider')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc')
]

CLIENT_ID = '5jPcCeaYo0s5VGjOCj6Vy4S2SUU8NPaqEPdl3FpN'
CLIENT_SECRET = 'XQ0j8PcB2hv3uY5MxFR5s7QLTGcghUPOKVYXnqVXqP5YObNnD8Dz8aviKiKYbGWWSV7cNDKyLNLzZNXTNqc4YqtHDPVfMrJvhuKsy0MZuFvwD6Yy9etHEB1QWvFdos7d'
