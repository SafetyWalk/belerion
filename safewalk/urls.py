# [START gaestd_py_django_local_static]
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    # Authentication & Admin Service
    path("admin/", admin.site.urls),
    path('api/v1/authentication/', include('authentication.urls')),
    # SafeWalk Service
    path('api/v1/contact/', include('contact.urls')),
    path('api/v1/maps/', include('maps.urls')),
    path('api/v1/profile/', include('user_profile.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# [END gaestd_py_django_local_static]