from django.urls import path
from ..views import home_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home_views.home,name="home")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)