from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    # Blog
    path('blog/', include('blog.urls', namespace='blog')),
    path('portfolio/', include('portfolio.urls')),
    # Other
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
