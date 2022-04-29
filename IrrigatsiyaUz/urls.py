from email.policy import default
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf.urls.i18n import i18n_patterns
from decouple import config

from my_works import views as my_works_views
from django.conf.urls import handler404, handler500
from django.views.generic import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="API Docs",
        default_version='v1',
        description="API urls description",
        terms_of_service="https://www.myblogs.com/policies/terms/",
        contact=openapi.Contact(email="aahmadov271101@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(

    path('', include('my_works.urls')),
    path('tests/', include('Tests.urls')),
    path('me/', include('accounts.urls')),
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),

    #    re_path('\w+/', TemplateView.as_view(template_name='404.html'), name='404'),
)



urlpatterns += static(settings.STATIC_URL,
                document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = config(
    "ADMIN_SITE_HEADER", default="Administration Desktop")
admin.site.site_title = config("ADMIN_SITE_TITLE", default="Administration")
admin.site.index_title = 'Administration page'
