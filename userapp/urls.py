from django.conf import settings
from django.conf.urls.static import static
from baton.autodiscover import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('api/', include('api.urls')),
    path('auth/', include('rest_auth.urls')),
    path('token/', obtain_auth_token, name='api_token_auth')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
