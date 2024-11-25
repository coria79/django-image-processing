from django.contrib import admin
from django.urls import path
from app_image_processing.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Route to access the Django admin panel
    path('admin/', admin.site.urls),
    
    # Route to the main view of the application
    path('', index, name='home'),  # Redirect '/' to the 'index' view
]

# Serve media files during development (only in DEBUG mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
